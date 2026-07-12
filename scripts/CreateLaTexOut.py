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
import re
import math

import datetime
import sys

from CookbookConst import C_BOOK_SECTIONS

from pathlib import Path

from PIL import Image, ImageDraw

## For rendering options
from pylatex import Document, Section, Subsection, LargeText, SmallText, \
                    Command, Tabular, Center, \
                    Foot, Head, PageStyle, NewPage, NewLine, \
                    Package
from pylatex.utils import NoEscape, italic, bold
from pylatex.section import Chapter
from scripts.i18n import get_language_pack
from scripts.translation_runtime import translate_text

#*  Constants ****************************************************************
RECIPE_HEADER_NEEDSPACE_LINES = 16
RECIPE_STANDARD_MAX_LINES = 46
RECIPE_COMPACT_MAX_LINES = 34
RECIPE_LONG_MIN_SPACE_LINES = 28
RECIPE_PORTRAIT_MAX_HEIGHT = '3.15in'
RECIPE_LANDSCAPE_MAX_HEIGHT = '2.65in'
RECIPE_COMPACT_MAX_HEIGHT = '2.05in'

#=============================================================================
def genLaTexOut(args, outAbsPath, cookbookData, gitRepo):
    
    outLaTexAbsPath = Path( os.path.join( outAbsPath, 'LaTex') )
    outLaTexAbsPath.mkdir(parents=True, exist_ok=True)
    
    book_name = args.name + '_' + (args.language or 'en')
    outLaTexAbsFilePath =  Path( os.path.join( outLaTexAbsPath, book_name) )
    language_pack = get_language_pack(args.language)
    labels = language_pack['labels']
    latex_settings = language_pack['latex']
    
    ### --- Build LaTex Document / Object  ---
    if(args.verbose):
        print("formatting data for LaTex file: %s" % (outLaTexAbsFilePath) )
        
        # Basic document
    doc = Document(
        documentclass='book',
        document_options = [
            '11pt',
            'twoside',
            ],
        geometry_options = {
            'head': '40pt',
            'margin': '0.5in',
            'bottom': '0.6in',
            'includeheadfoot': True
            }
         )

    if latex_settings.get('use_polyglossia'):
        doc.preamble.append(Package('fontspec'))
        doc.preamble.append(Package('polyglossia'))
        doc.preamble.append(NoEscape(r'\setdefaultlanguage{%s}' % latex_settings['language']))
        doc.preamble.append(NoEscape(r'\setmainfont{%s}' % latex_settings['main_font']))
    
    ## Setup Syle for Recipe pages
    strNameBookStyle = 'styleBookContents'
    styleBookContents = PageStyle(strNameBookStyle)
    
    ## Setup Headers
    with styleBookContents.create( Head("RO") ) as docFooter:
        docFooter.append( NoEscape(r'\thepage\ ') )
    with styleBookContents.create( Head("LE") ) as docFooter:
        docFooter.append( NoEscape(r'\thepage\ ') )
    
    with styleBookContents.create( Foot("RO") ) as docFooter:
        docFooter.append( NoEscape(r'\rightmark') )
    with styleBookContents.create( Foot("LE") ) as docFooter:
        docFooter.append( NoEscape(r'\rightmark') )
          
    doc.preamble.append(styleBookContents)
    doc.preamble.append(Package('tabularx'))
    doc.preamble.append(Package('needspace'))
    doc.preamble.append(Package('graphicx'))
    doc.preamble.append(Package('enumitem'))
    doc.preamble.append(Package('multicol'))
    doc.preamble.append(NoEscape(
        r'\setlist[enumerate,1]{leftmargin=*,label=\arabic*.,labelsep=0.55em,'
        r'itemsep=3pt,topsep=3pt,parsep=0pt,partopsep=0pt}'
    ))
    doc.preamble.append(NoEscape(
        r'\setlist[itemize]{leftmargin=*,label=--,labelsep=0.5em,'
        r'itemsep=2pt,topsep=2pt,parsep=0pt,partopsep=0pt}'
    ))
    doc.preamble.append(NoEscape(r'\raggedbottom'))
    doc.preamble.append(NoEscape(r'\setlength{\emergencystretch}{1em}'))
    
    # Don't show chapter, section, etc numbering ( like 1.1.1..)
    doc.preamble.append( Command('setcounter', ['secnumdepth', NoEscape(r'-1')]) )
                         
    ## Override the Table Of Conents to use Header/Footer formating.
    doc.preamble.append(Command( 'AtBeginDocument', 
            [ 
            Command('addtocontents',
                ['toc', 
                NoEscape(r'\protect\thispagestyle{' + strNameBookStyle + '}')]
            )
        ])
    )

    ## --------------------
    ## Build Up the Recipe Book Structure
    genTitlePage(doc, labels)
    
    genCopyrightPage(doc, gitRepo, labels)
    
    # Add in the Table of Contents
    doc.append( Command('tableofcontents') )
    
    # Add in the Recipes
    doc.change_document_style("styleBookContents")
    with doc.create( Chapter(labels['recipes']) ):
        doc.append( Command('thispagestyle', [ strNameBookStyle]) )
        doc.append( 
            italic(
                labels['intro'])
            )
        doc.append( NewPage())
        
        recipeList = list( cookbookData['Recipes']['inputObjects'].keys() )
        recipeList.sort()

        if args.recipe_number is not None:
            if len(recipeList) == 1:
                selected_recipe = recipeList[0]
            else:
                recipe_index = args.recipe_number - 1
                selected_recipe = recipeList[recipe_index]
            recipeList = [selected_recipe]
            outLaTexAbsFilePath = Path(
                os.path.join(
                    outLaTexAbsPath,
                    "%s_%s" % (book_name, util_sanitize_label(selected_recipe))
                )
            )
        
        first_section = True
        for grpSectionName in C_BOOK_SECTIONS:
            if (args.verbose):
                    print( "Building LaTex Code for Section:%s" % ( grpSectionName ) )
            if args.recipe_number is not None:
                if cookbookData['Recipes']['inputObjects'][recipeList[0]].getSection() != grpSectionName:
                    continue
            if not first_section:
                doc.append( NewPage() )
            doc.append( NoEscape(r'\begingroup\centering') )
            doc.append( Section(translate_text(grpSectionName)) )
            doc.append( NoEscape(r'\par\endgroup') )
                
            ## TODO - any info on this sections..
            doc.append( NoEscape(r'\par') )
            first_section = False
            
            for iRecipe in recipeList:
                if (args.verbose):
                    print( "-Building LaTex Code for Recipe:%s" % ( iRecipe ) )
                if (cookbookData['Recipes']['inputObjects'][iRecipe].getSection() == grpSectionName):
                    genRecipe(
                        doc,
                        iRecipe,
                        cookbookData['Recipes']['inputObjects'][iRecipe],
                        outLaTexAbsPath,
                        labels,
                    )
    
        if args.recipe_number is None:
            with doc.create( Chapter(labels['index']) ):
                doc.append( Command('thispagestyle', [ strNameBookStyle]) )
                
                doc.append( Command(
                    'twocolumn ',
                    [],
                    [NoEscape(r'\section{%s} \label{sec:ByIngredient}' % labels['by_ingredient'])]
                ))
                getLateByIngredientIndex( doc, cookbookData)
                
                
                doc.append( Command('onecolumn ') )
            
    ## --------------------
    ## Do the generation
    if(args.verbose):
        print("Building LaTex file: %s" % (outLaTexAbsFilePath) )
    
    compiler = latex_settings.get('compiler')
    passes = max(1, int(latex_settings.get('passes', 1)))
    for idx in range(passes):
        clean = (idx == (passes - 1))
        if compiler:
            doc.generate_pdf(
                outLaTexAbsFilePath,
                clean_tex=False,
                clean=clean,
                compiler=compiler)
        else:
            doc.generate_pdf(
                outLaTexAbsFilePath,
                clean_tex=False,
                clean=clean)
    
    if(args.verbose):
        print("Finished Building LaTex file: %s" % (outLaTexAbsFilePath) )


#=============================================================================
def genTitlePage(latexDoc, labels):
    """
    Build the Title Page
    """
    latexDoc.preamble.append(Command('title', labels['title']))
    latexDoc.preamble.append(Command('author', NoEscape(r'Bilyana Yakova \and Thomas Anderson')))
    latexDoc.preamble.append(Command('date', NoEscape(r'\today')))
    latexDoc.append(NoEscape(r'\maketitle'))

#=============================================================================
def genCopyrightPage(latexDoc, gitRepo, labels):
    """
    Add in a Copyright page
    """
    now = datetime.datetime.now()
    V_SPACE_SIZE = '20pt'
    
    with latexDoc.create(Center()) as centered:
        centered.append( Command('vspace', ['80pt']))
        centered.append( NoEscape(
            labels['copyright'] + ' ' +
            '\copyright' +
            ' ' +
            str(now.year) +
            ' ' +
            labels['by'] +
            ' Thomas Anderson and Bilyana Yakova' ))
        
    with latexDoc.create(Center()) as centered:
        centered.append( Command('vspace', [V_SPACE_SIZE]))
        centered.append(labels['all_rights_reserved'])
        
    with latexDoc.create(Center()) as centered:
        centered.append( Command('vspace', [V_SPACE_SIZE]))
        centered.append(labels['published_by'])
        centered.append(NoEscape(r'\\'))
        centered.append( 'www.lulu.com' )
        
    with latexDoc.create(Center()) as centered:
        centered.append( Command('vspace', ['80pt']))
        centered.append(labels['git_info'])
        centered.append(NoEscape(r'\\')) 
        centered.append( '%s:%s' % (labels['commit'], gitRepo.commit().hexsha) )
        centered.append(NoEscape(r'\\')) 
        centered.append( '%s:%s' % (labels['clean_commit'], str(not gitRepo.is_dirty()).strip()) )
        
    latexDoc.append( NewPage() )

#=============================================================================
def genRecipe(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels):
    """
    Render a recipe with an adaptive, orientation-aware layout.

    Standard recipes are held together and may share a page with another
    short recipe.  Recipes estimated to be taller than a page use a breakable
    long form whose directions can continue at step boundaries.
    """
    metrics = util_recipe_layout_metrics(recipeData)
    fmt = recipeData.getRecipeFormat()
    force_long = fmt == 'FORCE_LONG'
    force_standard = fmt == 'FORCE_STANDARD'
    use_long = force_long or (
        not force_standard and metrics['estimated_lines'] > RECIPE_STANDARD_MAX_LINES
    )

    if use_long:
        genRecipeFormatAdaptiveLong(
            latexDoc, recipeName, recipeData, outLaTexAbsPath, labels, metrics
        )
    elif metrics['compact_lines'] <= RECIPE_COMPACT_MAX_LINES:
        genRecipeFormatAdaptiveCompact(
            latexDoc, recipeName, recipeData, outLaTexAbsPath, labels, metrics
        )
    else:
        genRecipeFormatAdaptiveStandard(
            latexDoc, recipeName, recipeData, outLaTexAbsPath, labels, metrics
        )

#=============================================================================
# Helpers
#=============================================================================

#=============================================================================
def util_FancyBuildHeader( latexDoc, recipeName  ):
    '''
    Fancy Head build
    '''
    label = 'subsec:%s' % (util_sanitize_label(recipeName))
    # The center environment is list-based and can produce a missing-item
    # error when it follows needspace.  Grouped centering has the same visual
    # result without introducing a list environment.
    latexDoc.append(NoEscape(r'\begingroup\centering'))
    latexDoc.append(Subsection(
        "%s" % translate_text(recipeName), label=label
    ))
    latexDoc.append(NoEscape(r'\par\endgroup'))
    latexDoc.append(Command('hrule'))
    latexDoc.append(NoEscape(r'\par\vspace{6pt}'))

#=============================================================================
def util_reserve_recipe_header_space(latexDoc, lines=RECIPE_HEADER_NEEDSPACE_LINES):
    latexDoc.append(NoEscape(r'\needspace{%s\baselineskip}' % lines))
    latexDoc.append(NoEscape(r'\nopagebreak[4]'))

#=============================================================================
def util_injectNotes(latexDoc, recipeData, labels):
    latexDoc.append( Command('vspace', ['10pt'] ) )
    latexDoc.append( LargeText( bold(labels['notes'])) )
    latexDoc.append( NewLine()  )
    latexDoc.append(
            SmallText( italic( recipeData.GetDescription() ))
        )
#=============================================================================
def util_addPicNotInFig(latexDoc, strPicPath, widthNum, outLaTexAbsPath=None):
    '''
    Helper to put picture in that isn't in a figure.
    '''
    imgPath = strPicPath
    if outLaTexAbsPath is not None:
        imgPath = util_tex_image_path(strPicPath, outLaTexAbsPath)
    latexDoc.append( Command(
        'includegraphics',
        NoEscape( imgPath ),
        NoEscape(r'width=' + widthNum + r'\columnwidth'))
    )
    latexDoc.append( NoEscape(r'\par') )

#=============================================================================
def util_refRecipePageNum( strRecipeName):
    '''
    Done this way in order to allow for injection into tables with additional text.
    '''
    return NoEscape(r'\pageref{subsec:%s}' % (util_sanitize_label(strRecipeName)))

#=============================================================================
def util_page_ref_text(labels, recipeName):
    """
    Return a localized page reference text fragment.
    """
    return r'%s \pageref{subsec:%s}' % (labels['page_abbrev'], util_sanitize_label(recipeName))

#=============================================================================
def util_sanitize_label(strLabel):
    sanitized = re.sub(r'[^\w]', '', strLabel, flags=re.UNICODE)
    if not sanitized:
        sanitized = 'Recipe'
    return sanitized

#=============================================================================
def util_tex_image_path(imgPath, outLaTexAbsPath):
    try:
        relPath = os.path.relpath(
            Path(imgPath).resolve(),
            Path(outLaTexAbsPath).resolve()
        )
        return relPath.replace(os.sep, '/')
    except Exception:
        return Path(imgPath).resolve().as_posix()

#=============================================================================
def util_primary_image_orientation(recipeData):
    """Return landscape, portrait, square, or none for the primary image."""
    picture = recipeData.getPicturePrimary()
    if not picture:
        return 'none', 0.0

    try:
        with Image.open(picture['path']) as image:
            width, height = image.size
        ratio = float(width) / float(height)
    except (OSError, KeyError, TypeError, ZeroDivisionError):
        return 'square', 1.0

    if ratio >= 1.18:
        return 'landscape', ratio
    if ratio <= 0.85:
        return 'portrait', ratio
    return 'square', ratio

#=============================================================================
def util_estimated_text_lines(text, chars_per_line):
    """Conservatively estimate wrapped LaTeX lines for a text value."""
    if not text:
        return 0
    text = str(text).strip()
    if not text:
        return 0
    return max(1, int(math.ceil(len(text) / float(chars_per_line))))

#=============================================================================
def util_step_metrics(step, chars_per_line=58, depth=0):
    """Return estimated lines and characters for a step and its children."""
    text = translate_text(step.info.get('inText', ''))
    lines = util_estimated_text_lines(text, max(34, chars_per_line - (depth * 6)))
    lines += 1
    chars = len(text)
    for child in step.info.get('childStep', []):
        child_lines, child_chars = util_step_metrics(
            child, chars_per_line=chars_per_line, depth=depth + 1
        )
        lines += child_lines
        chars += child_chars
    if step.info.get('inPic'):
        lines += 8 * len(step.info['inPic'])
    return lines, chars

#=============================================================================
def util_step_compact_counts(step):
    """Count list items and inline photos for compact height estimation."""
    item_count = 1
    photo_count = len(step.info.get('inPic', []))
    for child in step.info.get('childStep', []):
        child_items, child_photos = util_step_compact_counts(child)
        item_count += child_items
        photo_count += child_photos
    return item_count, photo_count

#=============================================================================
def util_recipe_layout_metrics(recipeData):
    """Measure recipe density and choose the most useful photo placement."""
    orientation, aspect_ratio = util_primary_image_orientation(recipeData)
    ingredient_rows = 0
    ingredient_chars = 0
    group_rows = 0
    for group_name in recipeData.info.get('ingredientsGrpOrder', []):
        if group_name:
            group_rows += 1
        for ingredient in recipeData.info['ingredients'].get(group_name, []):
            ingredient_rows += 1
            ingredient_chars += len(str(ingredient.get('amount', '')))
            ingredient_chars += len(translate_text(ingredient.get('units', '')))
            ingredient_chars += len(
                translate_text(ingredient['ingredients'].getName())
            )

    step_lines = 0
    step_chars = 0
    compact_step_items = 0
    compact_step_photos = 0
    for step in recipeData.info.get('steps', []):
        lines, chars = util_step_metrics(step)
        step_lines += lines
        step_chars += chars
        item_count, photo_count = util_step_compact_counts(step)
        compact_step_items += item_count
        compact_step_photos += photo_count

    description = translate_text(recipeData.GetDescription() or '')
    description_lines = util_estimated_text_lines(description, 92)
    substitutes = getattr(recipeData, 'local_substitutes', [])
    extra_lines = len(recipeData.info.get('notes', [])) * 2
    extra_lines += len(substitutes) * 2

    # Square photographs usually read best in the portrait/sidebar treatment.
    placement = orientation
    if orientation == 'square':
        placement = 'portrait'

    if placement == 'landscape':
        ingredient_lines = group_rows + ingredient_rows
        ingredient_lines += int(math.ceil(ingredient_chars / 52.0))
        direction_lines = 15 + step_lines + extra_lines
        body_lines = max(ingredient_lines + 3, direction_lines)
    elif placement == 'portrait':
        ingredient_lines = group_rows + ingredient_rows
        ingredient_lines += int(math.ceil(ingredient_chars / 62.0))
        left_lines = 19 + ingredient_lines
        body_lines = max(left_lines, step_lines + extra_lines + 3)
    else:
        ingredient_lines = group_rows + ingredient_rows
        ingredient_lines += int(math.ceil(ingredient_chars / 55.0))
        body_lines = max(ingredient_lines + 3, step_lines + extra_lines + 3)

    estimated_lines = 5 + description_lines + body_lines
    compact_ingredient_lines = group_rows + ingredient_rows
    compact_ingredient_lines += int(math.ceil(ingredient_chars / 82.0))
    compact_photo_lines = 13 if orientation != 'none' else 0
    compact_step_lines = int(math.ceil(step_chars / 100.0))
    compact_step_lines += int(math.ceil(compact_step_items * 0.55))
    compact_step_lines += compact_step_photos * 8
    compact_lines = (
        5 + description_lines
        + max(compact_photo_lines, compact_ingredient_lines + 3)
        + compact_step_lines + extra_lines + 4
    )
    return {
        'orientation': orientation,
        'placement': placement,
        'aspect_ratio': aspect_ratio,
        'ingredient_rows': ingredient_rows,
        'step_chars': step_chars,
        'estimated_lines': estimated_lines,
        'compact_lines': compact_lines,
    }

#=============================================================================
def util_append_primary_image(
        latexDoc, recipeData, outLaTexAbsPath, max_height, width=r'\linewidth'):
    """Append a centered image constrained in both dimensions."""
    picture = recipeData.getPicturePrimary()
    if not picture:
        return
    img_path = util_tex_image_path(picture['path'], outLaTexAbsPath)
    latexDoc.append(NoEscape(r'\begingroup\centering'))
    latexDoc.append(Command(
        'includegraphics',
        NoEscape(img_path),
        NoEscape(
            r'width=%s,height=%s,keepaspectratio' % (width, max_height)
        )
    ))
    latexDoc.append(NoEscape(r'\par\endgroup'))

#=============================================================================
def util_build_adaptive_ingredients(recipeData, labels):
    """Build a compact, wrapping two-column ingredients table."""
    table = Tabular(NoEscape(
        r'@{}p{0.16\linewidth}p{0.76\linewidth}@{}'
    ))
    for ingredient in recipeData.genIngredientsBlock('LaTex'):
        amount, unit, name = ingredient[:3]
        recipe_ref = ingredient[3] if len(ingredient) > 3 else None
        if amount == '' and name == '':
            if unit:
                table.add_row(('', unit))
            continue

        quantity = str(amount).strip()
        description_parts = [
            part for part in (str(unit).strip(), str(name).strip()) if part
        ]
        ingredient_description = ' '.join(description_parts)
        if recipe_ref is not None:
            ingredient_description = NoEscape(
                ingredient_description + ', '
                + util_page_ref_text(labels, recipe_ref)
            )
        table.add_row((quantity, ingredient_description))
    return table

#=============================================================================
def util_append_recipe_heading(latexDoc, label):
    latexDoc.append(NoEscape(r'\par\vspace{4pt}\noindent'))
    latexDoc.append(LargeText(bold(label)))
    latexDoc.append(NoEscape(r'\par\vspace{2pt}'))

#=============================================================================
def util_append_recipe_description(latexDoc, recipeData):
    description = recipeData.GetDescription()
    if description:
        latexDoc.append(NoEscape(r'\par\smallskip\noindent'))
        latexDoc.append(italic(description))
        latexDoc.append(NoEscape(r'\par\smallskip'))

#=============================================================================
def util_append_recipe_extras(latexDoc, recipeData, labels):
    """Append recipe notes and localized substitutions."""
    notes = recipeData.info.get('notes', [])
    if notes:
        util_append_recipe_heading(latexDoc, labels['notes'])
        for note in notes:
            note_text = translate_text(note.get('txt', ''))
            if note_text:
                latexDoc.append(italic(note_text))
                latexDoc.append(NoEscape(r'\par'))

    substitutes = getattr(recipeData, 'local_substitutes', [])
    if substitutes:
        util_append_recipe_heading(latexDoc, labels['substitutes'])
        for substitute in substitutes:
            original = substitute.get('original', '')
            replacement = substitute.get('substitute', '')
            note = substitute.get('note', '')
            line = '%s -> %s' % (original, replacement)
            if note:
                line += ' (%s)' % note
            latexDoc.append(line)
            latexDoc.append(NoEscape(r'\par'))

#=============================================================================
def util_append_recipe_directions(latexDoc, recipeData, labels):
    util_append_recipe_heading(latexDoc, labels['directions'])
    # Adaptive recipes place directions inside minipages or multicols, where
    # floating figure environments are invalid.  Step photos are therefore
    # rendered inline by the existing no-figure path.
    directions = recipeData.genStepsBlock('LaTex_noFig', latexDoc)
    if directions is not None:
        latexDoc.append(directions)

#=============================================================================
def util_finish_adaptive_recipe(latexDoc):
    latexDoc.append(NoEscape(
        r'\par\vspace{6pt}\noindent\rule{\textwidth}{0.35pt}'
        r'\par\vspace{12pt}'
    ))

#=============================================================================
def genRecipeFormatAdaptiveCompact(
        latexDoc, recipeName, recipeData, outLaTexAbsPath, labels, metrics):
    """Render a short recipe card sized so two cards can share a page."""
    # The complete card is one minipage, so TeX can use its exact height and
    # move it intact when the remaining page space is insufficient.
    latexDoc.append(NoEscape(r'\noindent\begin{minipage}{\textwidth}'))
    util_FancyBuildHeader(latexDoc, recipeName)

    with latexDoc.create(SmallText()):
        util_append_recipe_description(latexDoc, recipeData)
        if recipeData.getPicturePrimary():
            latexDoc.append(NoEscape(
                r'\noindent\begin{minipage}[t]{0.275\textwidth}\vspace{0pt}'
            ))
            util_append_primary_image(
                latexDoc, recipeData, outLaTexAbsPath,
                RECIPE_COMPACT_MAX_HEIGHT
            )
            latexDoc.append(NoEscape(r'\end{minipage}\hfill'))
            latexDoc.append(NoEscape(
                r'\begin{minipage}[t]{0.69\textwidth}\vspace{0pt}'
            ))
            util_append_recipe_heading(latexDoc, labels['ingredients'])
            latexDoc.append(util_build_adaptive_ingredients(recipeData, labels))
            latexDoc.append(NoEscape(r'\end{minipage}'))
        else:
            util_append_recipe_heading(latexDoc, labels['ingredients'])
            latexDoc.append(util_build_adaptive_ingredients(recipeData, labels))

        latexDoc.append(NoEscape(
            r'\par\setlist[enumerate,1]{itemsep=1pt,topsep=2pt}'
        ))
        util_append_recipe_directions(latexDoc, recipeData, labels)
        util_append_recipe_extras(latexDoc, recipeData, labels)

    latexDoc.append(NoEscape(r'\end{minipage}'))
    util_finish_adaptive_recipe(latexDoc)

#=============================================================================
def genRecipeFormatAdaptiveStandard(
        latexDoc, recipeName, recipeData, outLaTexAbsPath, labels, metrics):
    """Render a one-page recipe card that LaTeX keeps together."""
    # The complete card is one minipage, so TeX can use its exact height and
    # move it intact when the remaining page space is insufficient.
    latexDoc.append(NoEscape(r'\noindent\begin{minipage}{\textwidth}'))
    util_FancyBuildHeader(latexDoc, recipeName)

    with latexDoc.create(SmallText()):
        util_append_recipe_description(latexDoc, recipeData)
        placement = metrics['placement']
        if placement == 'portrait':
            left_width = r'0.405\textwidth'
            right_width = r'0.56\textwidth'
        else:
            left_width = r'0.315\textwidth'
            right_width = r'0.65\textwidth'

        latexDoc.append(NoEscape(
            r'\noindent\begin{minipage}[t]{%s}\vspace{0pt}' % left_width
        ))
        if placement == 'portrait':
            util_append_primary_image(
                latexDoc, recipeData, outLaTexAbsPath,
                RECIPE_PORTRAIT_MAX_HEIGHT
            )
        util_append_recipe_heading(latexDoc, labels['ingredients'])
        latexDoc.append(util_build_adaptive_ingredients(recipeData, labels))
        latexDoc.append(NoEscape(r'\end{minipage}\hfill'))

        latexDoc.append(NoEscape(
            r'\begin{minipage}[t]{%s}\vspace{0pt}' % right_width
        ))
        if placement == 'landscape':
            util_append_primary_image(
                latexDoc, recipeData, outLaTexAbsPath,
                RECIPE_LANDSCAPE_MAX_HEIGHT
            )
        util_append_recipe_directions(latexDoc, recipeData, labels)
        util_append_recipe_extras(latexDoc, recipeData, labels)
        latexDoc.append(NoEscape(r'\end{minipage}'))

    latexDoc.append(NoEscape(r'\end{minipage}'))
    util_finish_adaptive_recipe(latexDoc)

#=============================================================================
def genRecipeFormatAdaptiveLong(
        latexDoc, recipeName, recipeData, outLaTexAbsPath, labels, metrics):
    """Render a long recipe with a compact top band and breakable directions."""
    util_reserve_recipe_header_space(latexDoc, RECIPE_LONG_MIN_SPACE_LINES)
    util_FancyBuildHeader(latexDoc, recipeName)

    with latexDoc.create(SmallText()):
        util_append_recipe_description(latexDoc, recipeData)
        if recipeData.getPicturePrimary():
            if metrics['placement'] == 'landscape':
                image_width = r'0.43\textwidth'
                ingredient_width = r'0.535\textwidth'
                max_height = RECIPE_LANDSCAPE_MAX_HEIGHT
            else:
                image_width = r'0.31\textwidth'
                ingredient_width = r'0.665\textwidth'
                max_height = RECIPE_PORTRAIT_MAX_HEIGHT

            latexDoc.append(NoEscape(
                r'\noindent\begin{minipage}[t]{%s}\vspace{0pt}' % image_width
            ))
            util_append_primary_image(
                latexDoc, recipeData, outLaTexAbsPath, max_height
            )
            latexDoc.append(NoEscape(r'\end{minipage}\hfill'))
            latexDoc.append(NoEscape(
                r'\begin{minipage}[t]{%s}\vspace{0pt}' % ingredient_width
            ))
            util_append_recipe_heading(latexDoc, labels['ingredients'])
            latexDoc.append(util_build_adaptive_ingredients(recipeData, labels))
            latexDoc.append(NoEscape(r'\end{minipage}'))
        else:
            util_append_recipe_heading(latexDoc, labels['ingredients'])
            latexDoc.append(util_build_adaptive_ingredients(recipeData, labels))

        latexDoc.append(NoEscape(r'\par\smallskip'))
        latexDoc.append(NoEscape(
            r'\setlength{\columnsep}{18pt}\begin{multicols}{2}'
        ))
        util_append_recipe_directions(latexDoc, recipeData, labels)
        util_append_recipe_extras(latexDoc, recipeData, labels)
        latexDoc.append(NoEscape(r'\end{multicols}'))

    util_finish_adaptive_recipe(latexDoc)

#=============================================================================
def getLateByIngredientIndex( doc, cookbookData):
    """
    Generate Latex code for a index of recipes by Ingredient
    """
    lstIngred = []
    dictIngred = {}
    used_ingredients = set()
    recipe_objects = cookbookData.get('Recipes', {}).get('inputObjects', {})
    for recipe in recipe_objects.values():
        for ingredient_grp in recipe.info.get('ingredientsGrpOrder', []):
            for ingredient in recipe.info['ingredients'].get(ingredient_grp, []):
                used_ingredients.add(ingredient['ingredients'].getName())
    txtExcludeList = ['Household', 'Spices', 'Oils']
    for ingredGrp in cookbookData['ingredients']['text_tree']:
        if( ingredGrp not in txtExcludeList):
            ingredGrpBase = cookbookData['ingredients']['text_tree'][ingredGrp] 
            for ingred in ingredGrpBase:
                if used_ingredients and ingred not in used_ingredients:
                    continue
                display_name = translate_text(ingred).strip()
                lstIngred.append((display_name, ingred))
                dictIngred[ ingred ] = ingredGrpBase[ingred] 
    
    lstIngred.sort(key=lambda item: item[0].lower())
    
    doc.append( ' ' )
    doc.append( Command( 'noindent') )
    GrpLetter = ' '
    for display_name, ingItem in lstIngred:
        if (GrpLetter != display_name[0].upper() ):
            GrpLetter = display_name[0].upper()
            doc.append( NoEscape(r'\par') )
            doc.append( bold( GrpLetter ) )
            doc.append( NoEscape(r'\par') )
        doc.append( display_name )
        lstRecipe = list( dictIngred[ingItem]['ingred'].getRecipeList() )
        lstRecipe.sort()
        for itemLstRecipe in lstRecipe:
            doc.append( NoEscape(r'\par') )
            doc.append( Command(NoEscape(r'hspace*'), ['3 mm']) )
            doc.append( translate_text(itemLstRecipe) + ',')
            doc.append( util_refRecipePageNum( itemLstRecipe) )
        doc.append( NoEscape(r'\par') )
        
    #listIngred = 'ingredients'

#=============================================================================
def buildPdfImg( outAbsPath, inFilePath, roundEdges=True, scaleAmt=1.0,
                  inMaxDpi=300, inMaxSizeInch=4):
    """
    Convert a Image for use in LaTex PDF - and store to an out directory.
     
    Pass back the new path.
    """
    
    myImage = Image.open(inFilePath)
    fileNameSplit = os.path.split(inFilePath)
    fileDirSplit = os.path.split( fileNameSplit[0])
    
    outFilePath = os.path.join( outAbsPath, fileDirSplit[1] )
    Path(outFilePath).mkdir(parents=True, exist_ok=True)
    outFilePath = os.path.join( outFilePath, fileNameSplit[1])
    
    # Figure out what DPI to set this do
    dpiInW = 300
    dpiInH = 300 
    if ('dpi' in  myImage.info.keys() ):
        dpiInW, dpiInH = myImage.info['dpi']
        
    maxDpi = max( [dpiInW, dpiInH])    
    dpiRatioAdjust = inMaxDpi / maxDpi
    newDpioutW = (dpiRatioAdjust * dpiInW)
    newDpioutH = (dpiRatioAdjust * dpiInH) 
    
    ## See if we need a re-size
    sizeInIncW, sizeInIncH = myImage.size
    sizeInIncW /= newDpioutW
    sizeInIncH /= newDpioutH
    maxSizeInInc = max( [sizeInIncW, sizeInIncH])
    sizeInIncRatio = 1
    if(maxSizeInInc > inMaxSizeInch):
        sizeInIncRatio = inMaxSizeInch / maxSizeInInc
    
    # Adjust for Scale 
    sizeInIncRatio *= scaleAmt

    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = getattr(Image, "LANCZOS", Image.ANTIALIAS)

    myImage = myImage.resize(
        (int(sizeInIncW * sizeInIncRatio * newDpioutW),
         int(sizeInIncH * sizeInIncRatio * newDpioutH)),
        resample)
    
    if (roundEdges):
        myImage = myImage.convert('RGBA')
        # Use an Alpha Channel to round the corners
        myImage = util_pdfImg_add_corners(myImage, int( max([newDpioutW, newDpioutH])/2 ) )
        # Convert the Alpha Channel to a white background to allow saving
        # see - https://stackoverflow.com/a/33507138/2628864
        # Done because the PDF size with JPEG is about 1/10 the size of the one using PNG
        background = Image.new('RGBA', myImage.size, (255,255,255))
        myImage = Image.alpha_composite(background, myImage)
    
    myImage = myImage.convert('RGB')
    myImage.save(
        outFilePath, 
        dpi=(newDpioutW, newDpioutH)
        )
    
    if( False ):
        print(
            "Coverting image %s to lower res at %s" % 
            (inFilePath, outFilePath) )
        
    return outFilePath

#=============================================================================
def util_pdfImg_add_corners(im, rad):
    """
    Add rounded corner to an image
    taken from https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi
    """
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

#=============================================================================
def main(argv=None):
    """
    Description of program.
    """
    pass

#*  Main Code Path ***********************************************************
if __name__ == "__main__":
    # Exit code is main() return value
    # (see http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
    sys.exit(main())


#*****************************************************************************
#*****************************************************************************
