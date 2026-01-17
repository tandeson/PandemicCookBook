#!/usr/bin/env python
#*****************************************************************************
#
"""
    Build up a cook book by pulling together all the pieces
"""
#
#*****************************************************************************
#   Use of the software source code and warranty disclaimers are
#   identified in the Software Agreement associated herewith.
#*****************************************************************************

#*  Imports ******************************************************************
import os
import time
import ast
import json

import git

import sys
import importlib

from pathlib import Path
import pickle

## Custom objects
from IngredientList import C_INGREDIENTS
from scripts.i18n import get_language_pack
from scripts.translate import OpenAITranslator, LocalMapTranslator, CompositeTranslator
from scripts.translation_runtime import set_translator

## For rendering options
from scripts.CreateHtmlOut import genHtmlOut
from scripts.CreateLaTexOut import genLaTexOut
from scripts import myRecipe

#*  Constants ****************************************************************
C_DATETIME_STR_FMT_RULES = "%I:%M%p on %B %d, %Y" 

# Exit codes - "no error" must be 0
EXIT_OK, EXIT_ERR, EXIT_CTRL_C = range(3)

#=============================================================================
def main(argv=None):
    """
    Parse arguments, report start & stop time, and run the test.
    """
    
    # Handle command line arguments
    if argv is None:
        argv = sys.argv

    args = parseCommandLine( argv[1:] )
    
    #Debug for now - may make an option or remove later.
    args.cache_primary_photos = True
    
    try:
        print( "Start date & time is " + time.strftime("%c") )

        # Do the work
        mainControl(args)

    except KeyboardInterrupt:
        # Assume Control-C is intentional, and just exit w/o alerts
        return EXIT_CTRL_C

    print( "End date & time is " + time.strftime("%c") )
    return EXIT_OK


#=============================================================================
def parseCommandLine(args = sys.argv[1:]):
    """
    Parse command-line options. Returns arguments.

    """

    ## Documentation: https://docs.python.org/2/howto/argparse.html
    import argparse

    ## Parse Input Options.
    parser = argparse.ArgumentParser(description='Cookbook builder')
    
    ## -- Common Options
    parser.add_argument(
        '-i','--input_directory',
        action='store', default="recipes_for_book_input",
        help = "root directory where recipes are stored.")
    
    parser.add_argument(
        '-n','--name',
        action='store', default='Pandemic_Cookbook',
        help = 'Name of the cookbook being built.')
    
    parser.add_argument(
        '-o','--output_directory',
        action='store', default="output",
        help = "root directory where recipes documents are generated.")

    parser.add_argument(
        '-l','--language',
        action='store', default='en',
        help = "Output language for labels and templates (e.g. 'en', 'bg').")

    parser.add_argument(
        '--recipe-number',
        action='store', type=int, default=None,
        help = "Generate PDF for a single recipe by its 1-based number in sorted order.")

    parser.add_argument(
        '--translate',
        action='store_true',
        help = "Translate recipe content using OpenAI and cache results.")

    parser.add_argument(
        '--translation-cache',
        action='store', default=os.path.join('translations', 'translation_cache.json'),
        help = "Path to translation cache JSON file.")

    parser.add_argument(
        '--translation-model',
        action='store', default='gpt-4o',
        help = "OpenAI model for translation (default: gpt-4o).")

    parser.add_argument(
        '--refresh-translations',
        action='store_true',
        help = "Re-translate even if cache entries exist.")
    
    parser.add_argument(
        '-v','--verbose',
        action='store_true',
        help = "Verbose progress messages. Progress messages are "
                "not displayed by default except for system error messages.")
    
    ## Parse the options
    args = parser.parse_args()

    return (args)

#=============================================================================
def mainControl(args):
    """
    Main routine for the Cookbook Builder.

    Find all the recipe files, build a cookbook!
    """
    
    ## Holder for all data at this is build up..
    cookbookData = {
        'Recipes': {
            # Input objects from files
            'inputObjects': {},
            
            # Sorted name list
            'sorted_names': [],
            
            # html helpers
            'html': {},
            'html_date_format': C_DATETIME_STR_FMT_RULES,
            },
        
        'ingredients': {
            ## Tree of {'name': 'xxxx', html: 'xxxx',  'children': {} }
            'text_tree': {}
            
            },
        'errors': {
            'dirMissingScripts': [],
            }
        }
    
    ##------------------------------
    ## For now Verbose always on
    ##------------------------------
    args.verbose = True
    
    ##------------------------------
    ## Helper for single-recipe selection
    ##------------------------------
    def _extract_recipe_name_from_file(py_path):
        try:
            source = py_path.read_text(encoding='utf-8')
        except OSError:
            return None
        try:
            tree = ast.parse(source, filename=str(py_path))
        except SyntaxError:
            return None
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            if isinstance(func, ast.Name):
                func_name = func.id
            elif isinstance(func, ast.Attribute):
                func_name = func.attr
            else:
                continue
            if func_name != 'MyRecipe' or not node.args:
                continue
            name_node = node.args[0]
            if isinstance(name_node, ast.Str):
                return name_node.s
            if isinstance(name_node, ast.Constant) and isinstance(name_node.value, str):
                return name_node.value
        return None

    def _extract_recipe_name_via_import(pythonModuleFile):
        try:
            module_path = pythonModuleFile.with_suffix("")
            strModulePath = str(module_path).replace("\\", ".").replace("/", ".")
            result = importlib.import_module(strModulePath)
            temp_ingredients = []
            newRecipe = result.makeRecipe(
                os.path.dirname(pythonModuleFile.absolute()),
                temp_ingredients,
            )
            return newRecipe.getName()
        except Exception:
            return None

    def _warn_localization_mismatch(message):
        if args.verbose:
            sys.stderr.write("Localization warning: %s\n" % message)

    def _map_translation_entry(mapping, source_text, translated_text, label):
        if not source_text or translated_text is None:
            return
        if source_text in mapping and mapping[source_text] != translated_text:
            _warn_localization_mismatch(
                "%s has conflicting translations for '%s'." % (label, source_text)
            )
            return
        mapping[source_text] = translated_text

    def _merge_translation_map(mapping, new_map):
        for source_text, translated_text in (new_map or {}).items():
            _map_translation_entry(mapping, source_text, translated_text, "translation")
        return mapping

    def _map_steps_translation(mapping, english_steps, localized_steps):
        for idx, english_step in enumerate(english_steps):
            if idx >= len(localized_steps):
                _warn_localization_mismatch("Step count mismatch in localized file.")
                break
            localized_step = localized_steps[idx]
            if isinstance(localized_step, dict):
                localized_text = localized_step.get('text')
                localized_children = localized_step.get('substeps', [])
            else:
                localized_text = localized_step
                localized_children = []
            _map_translation_entry(
                mapping,
                english_step.info.get('inText'),
                localized_text,
                "step"
            )
            english_children = english_step.info.get('childStep', [])
            if english_children:
                if not isinstance(localized_children, list):
                    localized_children = []
                for child_idx, english_child in enumerate(english_children):
                    if child_idx >= len(localized_children):
                        _warn_localization_mismatch("Substep count mismatch in localized file.")
                        break
                    localized_child = localized_children[child_idx]
                    if isinstance(localized_child, dict):
                        localized_child_text = localized_child.get('text')
                        localized_grandchildren = localized_child.get('substeps', [])
                    else:
                        localized_child_text = localized_child
                        localized_grandchildren = []
                    _map_translation_entry(
                        mapping,
                        english_child.info.get('inText'),
                        localized_child_text,
                        "substep"
                    )
                    grand_children = english_child.info.get('childStep', [])
                    if grand_children:
                        _map_steps_translation(mapping, grand_children, localized_grandchildren)

    def _build_local_translation_map(recipe_obj, localized_data):
        mapping = {}
        _map_translation_entry(mapping, recipe_obj.getName(), localized_data.get('name'), "recipe name")
        _map_translation_entry(mapping, recipe_obj.getSection(), localized_data.get('section'), "recipe section")
        _map_translation_entry(mapping, recipe_obj.info.get('description'), localized_data.get('description'), "description")

        english_todo = recipe_obj.getToDoNotes()
        localized_todo = localized_data.get('todo', [])
        if len(english_todo) != len(localized_todo):
            _warn_localization_mismatch("TODO count mismatch in localized file.")
        for english_item, localized_item in zip(english_todo, localized_todo):
            _map_translation_entry(mapping, english_item, localized_item, "todo")

        english_notes = [note.get('txt') for note in recipe_obj.info.get('notes', [])]
        localized_notes = localized_data.get('notes', [])
        if english_notes and len(english_notes) != len(localized_notes):
            _warn_localization_mismatch("Notes count mismatch in localized file.")
        for english_item, localized_item in zip(english_notes, localized_notes):
            _map_translation_entry(mapping, english_item, localized_item, "note")

        english_groups = recipe_obj.info.get('ingredientsGrpOrder', [])
        localized_groups = localized_data.get('ingredients', [])
        if len(english_groups) != len(localized_groups):
            _warn_localization_mismatch("Ingredient group count mismatch in localized file.")
        for group_idx, group_name in enumerate(english_groups):
            if group_idx >= len(localized_groups):
                break
            localized_group = localized_groups[group_idx]
            _map_translation_entry(mapping, group_name, localized_group.get('group'), "ingredient group")
            english_items = recipe_obj.info['ingredients'].get(group_name, [])
            localized_items = localized_group.get('items', [])
            if len(english_items) != len(localized_items):
                _warn_localization_mismatch("Ingredient item count mismatch in localized file.")
            for item_idx, item in enumerate(english_items):
                if item_idx >= len(localized_items):
                    break
                localized_item = localized_items[item_idx]
                _map_translation_entry(
                    mapping,
                    item['ingredients'].getName(),
                    localized_item.get('name'),
                    "ingredient"
                )
                _map_translation_entry(
                    mapping,
                    item.get('units'),
                    localized_item.get('unit'),
                    "unit"
                )

        english_steps = recipe_obj.info.get('steps', [])
        localized_steps = localized_data.get('steps', [])
        if len(english_steps) != len(localized_steps):
            _warn_localization_mismatch("Step count mismatch in localized file.")
        _map_steps_translation(mapping, english_steps, localized_steps)
        return mapping

    def _load_localized_recipe_json(recipe_dir, language_slug):
        language_keys = []
        if language_slug:
            language_keys.append(language_slug.lower())
        if args.language:
            language_keys.append(args.language.lower())
        language_name = language_pack.get('language_name', '')
        if language_name:
            language_keys.append(language_name.lower())

        seen = set()
        for key in language_keys:
            if not key or key in seen:
                continue
            seen.add(key)
            candidates = sorted(Path(recipe_dir).glob("%s_*.json" % key))
            if not candidates:
                continue
            try:
                return json.loads(candidates[-1].read_text(encoding='utf-8'))
            except Exception as exc:
                _warn_localization_mismatch(
                    "Could not read localized file %s: %s" % (candidates[-1], exc)
                )
                return None
        return None

    ##------------------------------
    ## Read in data
    ##------------------------------
         
    # Sample of handling errors.
    if not os.path.isdir( args.input_directory ):
        sys.stderr.write("Directory '%s' does not exist.\n" % args.input_directory)
        sys.exit(1)
    else:
        inDirRootPath = Path( os.path.join(".", args.input_directory) )
        
        # Find all the dir inside the input directory - ensure each has at least one recipe.
        inDirList = next( os.walk(inDirRootPath) )[1]

        # Find all the python files
        pythonFiles = list( inDirRootPath.rglob("*.[pP][yY]"))
        
        total_recipe_count = None
        if args.recipe_number is not None:
            def _parse_dir_prefix(dir_name):
                parts = dir_name.split('_', 1)
                if parts and parts[0].isdigit():
                    return int(parts[0])
                return None

            recipe_dirs = []
            for dir_name in inDirList:
                prefix = _parse_dir_prefix(dir_name)
                if prefix is None:
                    continue
                recipe_dirs.append((prefix, dir_name))

            recipe_dirs.sort(key=lambda item: item[0])
            total_recipe_count = len(recipe_dirs)
            if args.recipe_number < 1 or args.recipe_number > total_recipe_count:
                raise Exception(
                    "Recipe number %s is out of range (1-%s)." % (
                        args.recipe_number,
                        total_recipe_count
                    )
                )

            selected_dir = recipe_dirs[args.recipe_number - 1][1]
            selected_dir_path = inDirRootPath / selected_dir
            selected_py = list(selected_dir_path.rglob("*.[pP][yY]"))
            if not selected_py:
                raise Exception(
                    "No recipe python script found in %s." % selected_dir_path
                )
            pythonFiles = [selected_py[0]]
        
        ## Check for missing dir info
        if args.recipe_number is None:
            for dirName in inDirList:
                if(args.verbose):
                    print( " Checking: %s" % dirName )
                didFind = False
                for fileDir in pythonFiles:
                    if(dirName in str(fileDir)):
                        didFind = True
                        break
                if( False == didFind):
                    cookbookData['errors']['dirMissingScripts'].append(dirName)
            if (args.verbose):
                if (len(cookbookData['errors']['dirMissingScripts'] ) ):
                    print("\n** Warning - the following directories do not have a recipe python script. **")
                    for i in cookbookData['errors']['dirMissingScripts']:
                        print(i)
                    print('\n')
                
        ## for dir with info - run them
        for pythonModuleFile in pythonFiles:
            module_path = pythonModuleFile.with_suffix("")
            # Normalize path separators so importlib works on Windows and POSIX.
            strModulePath = str(module_path).replace("\\", ".").replace("/", ".")
            
            result = importlib.import_module(strModulePath)

            newRecipe = result.makeRecipe( 
                os.path.dirname( pythonModuleFile.absolute() ), 
                C_INGREDIENTS )
            
            cookbookData['Recipes']['inputObjects'][ newRecipe.getName() ] = newRecipe
            
    ##------------------------------
    ## Post Process
    ##------------------------------
    
    # -- Get out Recipe list - and sort
    cookbookData['Recipes']['sorted_names'] = list( cookbookData['Recipes']['inputObjects'].keys() )
    cookbookData['Recipes']['sorted_names'].sort()

    if args.recipe_number is not None and total_recipe_count is None:
        if args.recipe_number < 1 or args.recipe_number > len(cookbookData['Recipes']['sorted_names']):
            raise Exception(
                "Recipe number %s is out of range (1-%s)." % (
                    args.recipe_number,
                    len(cookbookData['Recipes']['sorted_names'])
                )
            )
    
    # -- Get out Ingredients
    for inGred in C_INGREDIENTS:
        if inGred.getGroup() not in cookbookData['ingredients']['text_tree'].keys():
            cookbookData['ingredients']['text_tree'][inGred.getGroup()] = {}
        cookbookData['ingredients']['text_tree'][inGred.getGroup()][inGred.getName()] = {'ingred': inGred, 'children': {} }
    
    ##------------------------------
    ## Generate outputs
    ##------------------------------

    language_pack = get_language_pack(args.language)
    if args.translate and args.language != 'en':
        language_slug = language_pack.get('latex', {}).get('language')
        if not language_slug:
            language_slug = language_pack.get('language_name', '').lower()
        language_slug = language_slug.lower()

        local_mapping = {}
        localized_by_recipe = {}
        for recipe in cookbookData['Recipes']['inputObjects'].values():
            localized_data = _load_localized_recipe_json(recipe.getPathLoc(), language_slug)
            if localized_data:
                localized_by_recipe[recipe.getName()] = localized_data
                recipe_map = _build_local_translation_map(recipe, localized_data)
                _merge_translation_map(local_mapping, recipe_map)

        local_translator = None
        if local_mapping:
            local_translator = LocalMapTranslator(local_mapping, language_pack['language_name'])

        api_key = os.environ.get('OPENAI_API_KEY')
        openai_translator = None
        if api_key:
            openai_translator = OpenAITranslator(
                api_key=api_key,
                model=args.translation_model,
                target_language=language_pack['language_name'],
                cache_path=args.translation_cache,
                refresh=args.refresh_translations,
            )

        if local_translator and openai_translator:
            set_translator(CompositeTranslator([local_translator, openai_translator]))
        elif local_translator:
            set_translator(local_translator)
        elif openai_translator:
            set_translator(openai_translator)
        else:
            set_translator(None)

        if not openai_translator:
            if not localized_by_recipe:
                raise Exception(
                    "No localized recipe files found for language '%s'." % args.language
                )
            filtered = {}
            for name, recipe in cookbookData['Recipes']['inputObjects'].items():
                if name in localized_by_recipe:
                    filtered[name] = recipe
            cookbookData['Recipes']['inputObjects'] = filtered
            cookbookData['Recipes']['sorted_names'] = list(filtered.keys())
            cookbookData['Recipes']['sorted_names'].sort()
            if args.recipe_number is not None and not cookbookData['Recipes']['sorted_names']:
                raise Exception(
                    "No localized recipe file found for selected recipe number %s." % args.recipe_number
                )
            filtered_names = set(cookbookData['Recipes']['sorted_names'])
            for ingredient in C_INGREDIENTS:
                recipe_list = ingredient.info.get('recipeList', {})
                ingredient.info['recipeList'] = {
                    name: recipe for name, recipe in recipe_list.items()
                    if name in filtered_names
                }
    
    ## build up Git info
    gitRepo = git.Repo(search_parent_directories=True)
    
    ## Build up Path info
    outAbsPath = Path( os.path.join( '.', args.output_directory ) )
    outAbsPath.mkdir(parents=True, exist_ok=True)
        
    # -- HTML        
    genHtmlSample = False
    if genHtmlSample:
        genHtmlOut(args, outAbsPath, cookbookData, gitRepo)
        
    # -- LaTex
    getLaTexOut = True
    if getLaTexOut:
        myRecipe.set_latex_output_dir(outAbsPath / 'LaTex')
        genLaTexOut(args, outAbsPath, cookbookData, gitRepo)

    # -- Photo List
    if args.cache_primary_photos:
        pkl_photo_name = args.name.replace(' ','') + '_primaryPhots.pkl'
        pkl_photo_dic = []
        
        for iRecipeName in cookbookData['Recipes']['inputObjects']:
            iRecipe = cookbookData['Recipes']['inputObjects'][iRecipeName]
            if iRecipe.info['primaryPic'] is not None:
                primaryPic =iRecipe.getPicturePrimary()
                pkl_photo_dic.append( {'path':primaryPic['path_orig'] } )
        
        with open( Path( os.path.join(outAbsPath, 'img', pkl_photo_name)), 'wb') as handle:
            pickle.dump(pkl_photo_dic, handle, protocol=pickle.HIGHEST_PROTOCOL)

    
    return True

#*  Main Code Path ***********************************************************

if __name__ == "__main__":
    # Exit code is main() return value
    # (see http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
    sys.exit(main())


#*****************************************************************************
#*****************************************************************************
