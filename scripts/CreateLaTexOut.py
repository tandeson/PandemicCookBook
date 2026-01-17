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

import datetime
import sys

from CookbookConst import C_BOOK_SECTIONS

from pathlib import Path

from PIL import Image, ImageDraw

## For rendering options
from pylatex import Document, Section, Subsection, LargeText, SmallText, \
                    Command, Tabular, Tabularx,  Center, \
                    Foot, Head, PageStyle, NewPage, NewLine, \
                    Package, Figure
from pylatex.utils import NoEscape, italic, bold
from pylatex.section import Chapter
from scripts.i18n import get_language_pack
from scripts.translation_runtime import translate_text

#*  Constants ****************************************************************
RECIPE_VSPACE_SMALL = '3pt'
RECIPE_VSPACE_AFTER = '4pt'
RECIPE_HEADER_NEEDSPACE_LINES = 16
RECIPE_HEADER_NEEDSPACE_LINES_LARGE = 18
RECIPE_IMG_FIXED_WIDTH = r'0.26\textwidth'
RECIPE_IMG_FIXED_HEIGHT = r'2.4in'

#=============================================================================
def genLaTexOut(args, outAbsPath, cookbookData, gitRepo):
    
    outLaTexAbsPath = Path( os.path.join( outAbsPath, 'LaTex') )
    outLaTexAbsPath.mkdir(parents=True, exist_ok=True)
    
    outLaTexAbsFilePath =  Path( os.path.join( outLaTexAbsPath, args.name) )
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
    doc.preamble.append(NoEscape(r'\setlist[itemize]{leftmargin=0pt,itemindent=0pt,label=--,labelsep=0.5em}'))
    
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
                    "%s_%s" % (args.name, util_sanitize_label(selected_recipe))
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
            doc.append( NewPage() )
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
    if compiler:
        doc.generate_pdf(
            outLaTexAbsFilePath,
            clean_tex=False,
            compiler=compiler)
    else:
        doc.generate_pdf(
            outLaTexAbsFilePath,
            clean_tex=False)
    
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
    Format a Recipe into LaTex
    """
    genRecipeFormatCompactImageLeft(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels)

#=============================================================================
# Helpers
#=============================================================================

#=============================================================================
def util_FancyBuildHeader( latexDoc, recipeName  ):
    '''
    Fancy Head build
    '''
    label = 'subsec:%s' % (util_sanitize_label(recipeName))
    latexDoc.append( NoEscape(r'\begingroup\centering') )
    latexDoc.append( Subsection( "%s" % ( translate_text(recipeName) ), label=label))
    latexDoc.append( NoEscape(r'\par\endgroup') )

#=============================================================================
def util_reserve_recipe_header_space(latexDoc, lines=RECIPE_HEADER_NEEDSPACE_LINES):
    latexDoc.append(NoEscape(r'\needspace{%s\baselineskip}' % lines))
    latexDoc.append(NoEscape(r'\nopagebreak[4]'))

#=============================================================================
def util_injectNotes(latexDoc, recipeData, labels):
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
    latexDoc.append( LargeText( bold(labels['notes'])) )
    latexDoc.append( NoEscape(r'\par')  )
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
# Builders
#=============================================================================

#=============================================================================
def genRecipeFormatTopTwoColumn(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels):
    
    ## Create Recipe Header
    util_reserve_recipe_header_space(latexDoc, RECIPE_HEADER_NEEDSPACE_LINES)
    picForRecipe = ''
    if( recipeData.getPicturePrimary() ):
        picForRecipe = Figure(position='h!')
        picForRecipe.add_image(
            util_tex_image_path(recipeData.getPicturePrimary()['path'], outLaTexAbsPath),
            width=NoEscape(r"0.4\textwidth") )
    
    if recipeData.GetDescription():
        latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
        latexDoc.append( 
            italic( recipeData.GetDescription() )
        )
        latexDoc.append( NoEscape(r'\par') )
                                 
    # Create Recipe body

    ##----
    # Add in Ingredients
    ingredLaTex = recipeData.genIngredientsBlock('LaTex')
    ingredPage = Tabular('rl')
    ingredPage.add_empty_row()
    for ingredDat in ingredLaTex:
        if ('' == ingredDat[0] and '' == ingredDat[2]):
            ingredPage.add_row( ('', ingredDat[1])  )
        else:
            if( ingredDat[3] != None):
                ingredPage.add_row( 
                    ingredDat[0], 
                    NoEscape(
                        ingredDat[1] + ' ' +
                        ingredDat[2] +
                        ', ' + util_page_ref_text(labels, ingredDat[3])
                    )
                )
            else:
                ingredPage.add_row( (ingredDat[0], ingredDat[1] + ' ' + ingredDat[2])  )
    
    ##---- Directions            
    dirPage =  recipeData.genStepsBlock('LaTex', latexDoc)
    
    util_FancyBuildHeader(latexDoc, recipeName)
    with latexDoc.create( SmallText() ):
        latexDoc.append( Command('columnratio',[0.53]) )
        latexDoc.append( Command('begin',['paracol', 2], packages=[ Package('paracol')]) )
        latexDoc.append( picForRecipe )
        latexDoc.append(  Command('switchcolumn',packages=[ Package('paracol')]) )
        latexDoc.append( ingredPage )
        latexDoc.append(  Command('end','paracol',packages=[ Package('paracol')]) )
        latexDoc.append( dirPage )
        
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_AFTER]) )
  
#=============================================================================
def genRecipeFormatFancyLong(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels):
    
    ingredLaTex = recipeData.genIngredientsBlock('LaTex')   

    util_reserve_recipe_header_space(latexDoc, RECIPE_HEADER_NEEDSPACE_LINES)
    util_FancyBuildHeader(latexDoc, recipeName)
    
    ## Create Recipe Header
    picForRecipe = ''
    if( recipeData.getPicturePrimary() ):
        picForRecipe = Figure(position='h')
        picForRecipe.add_image(
            util_tex_image_path(recipeData.getPicturePrimary()['path'], outLaTexAbsPath),
            width=NoEscape(r"0.4\textwidth") )
    
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
    
    if recipeData.GetDescription():
        latexDoc.append( 
            italic( recipeData.GetDescription() )
        )
        latexDoc.append( NoEscape(r'\par') )
                                 
    # Create Recipe body
    
    latexDoc.append( NoEscape('\r') )
    latexDoc.append(
        Command('begin',
                ['wrapfigure','r', NoEscape(r'0.5\textwidth')],
                packages=[ Package('wrapfig')])
        )
    
    for ingredDat in ingredLaTex:
        if ('' == ingredDat[0] and '' == ingredDat[2]):
            ## Special case for Grouped title in the middle column
            if( len(ingredDat[1])):
                latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
                latexDoc.append( NoEscape('\n') )
                latexDoc.append( ingredDat[1] )
                latexDoc.append( NoEscape(r'\par') )
        else:
            if( ingredDat[3] != None):
                latexDoc.append( 
                    NoEscape(
                        str(ingredDat[0]) + ' ' + 
                        ingredDat[1] + ' ' + 
                        ingredDat[2] + ', ' + util_page_ref_text(labels, ingredDat[3])
                        )
                    )
                latexDoc.append( NoEscape(r'\par') )
            else:
                latexDoc.append( str(ingredDat[0]) + ' ' + ingredDat[1] + ' ' + ingredDat[2] )
                latexDoc.append( NoEscape(r'\par') )
    
  
    if( recipeData.getPicturePrimary() ):
        latexDoc.append( Command('begin', ['center']) )
        util_addPicNotInFig(
            latexDoc, 
            recipeData.getPicturePrimary()['path'],
            '0.3',
            outLaTexAbsPath)
        latexDoc.append( Command('end', ['center']) )
        
    latexDoc.append( Command('end',['wrapfigure']) )

    recipeData.genStepsBlock('LaTex_indented_InjectHere', latexDoc)
    
    ##----
    # Add in Ingredients
         
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_AFTER]) )
    
#=============================================================================
def genRecipeFormatFancyTallPic(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels):
    '''
    Fancy formating with inspiration from https://www.etsy.com/listing/827640730/printable-recipe-book-kit-editable
    '''

    ## Setup header
    util_reserve_recipe_header_space(latexDoc, RECIPE_HEADER_NEEDSPACE_LINES_LARGE)
    util_FancyBuildHeader(latexDoc, recipeName)
    
    # Generate Ingredients List and Format
    # Add in Ingredients
    ingredLaTex = recipeData.genIngredientsBlock('LaTex')
    
    ingredPage = Tabular('p{0.20\linewidth}p{0.75\linewidth}')
    ingredPage.add_empty_row()
    for ingredDat in ingredLaTex:
        if ('' == ingredDat[0] and '' == ingredDat[2]):
            ingredPage.add_row( ('', ingredDat[1])  )
        else:
            if( ingredDat[3] != None):
                ingredPage.add_row( 
                    ingredDat[0], 
                    (NoEscape(
                        ingredDat[1] + ' ' + 
                        ingredDat[2] +
                        ', ' + util_page_ref_text(labels, ingredDat[3]) )
                    )
                )
            else:
                ingredPage.add_row( (ingredDat[0], ingredDat[1] + ' ' + ingredDat[2])  )
    
    
    ###################
    latexDoc.append( Command(
        'begin',
        ['tabularx', NoEscape(r"\textwidth"),
         NoEscape(r'p{.5\textwidth}X')]))
    
    ## Column 1
    if( recipeData.getPicturePrimary() ):
        latexDoc.append( Command('vspace', ['4pt'] ) )
        util_addPicNotInFig(
            latexDoc, 
            recipeData.getPicturePrimary()['path'],
            '0.40',
            outLaTexAbsPath)
    
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
    latexDoc.append( LargeText( bold(labels['ingredients'])) )
    latexDoc.append( NoEscape(r'\par') )

#=============================================================================
def util_addPicFixedSize(latexDoc, strPicPath, widthStr, heightStr, outLaTexAbsPath=None):
    '''
    Helper to put a fixed-size picture (width/height with aspect ratio).
    '''
    imgPath = strPicPath
    if outLaTexAbsPath is not None:
        imgPath = util_tex_image_path(strPicPath, outLaTexAbsPath)
    latexDoc.append( Command(
        'includegraphics',
        NoEscape( imgPath ),
        NoEscape(r'width=' + widthStr + r',height=' + heightStr + r',keepaspectratio'))
    )
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append(ingredPage )
    
    
    latexDoc.append( NoEscape(r'&'))
    
    ## Column 3
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
    
    latexDoc.append( LargeText( bold(labels['directions'])) )
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append(recipeData.genStepsBlock('LaTex', latexDoc) )
    
    
    if recipeData.GetDescription():
        util_injectNotes(latexDoc, recipeData, labels)
         
    latexDoc.append( NoEscape(r'\\'))
    
    latexDoc.append( Command('end',['tabularx']))
    
    ## Setup for next page
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_AFTER]) )

#=============================================================================
def genRecipeFormatFancyWidePic(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels):
    '''
    Fancy formating with inspiration from https://www.etsy.com/listing/827640730/printable-recipe-book-kit-editable
    '''

    ## Setup header
    util_reserve_recipe_header_space(latexDoc, RECIPE_HEADER_NEEDSPACE_LINES_LARGE)
    util_FancyBuildHeader(latexDoc, recipeName)
    
    # Generate Ingredients List and Format
    # Add in Ingredients
    ingredLaTex = recipeData.genIngredientsBlock('LaTex')
    
    ingredPage = Tabular('p{0.20\linewidth}p{0.75\linewidth}')
    ingredPage.add_empty_row()
    for ingredDat in ingredLaTex:
        if ('' == ingredDat[0] and '' == ingredDat[2]):
            ingredPage.add_row( ('', ingredDat[1])  )
        else:
            if( ingredDat[3] != None):
                ingredPage.add_row( 
                    ingredDat[0], 
                    (NoEscape(
                        ingredDat[1] + ' ' + 
                        ingredDat[2] +
                        ', ' + util_page_ref_text(labels, ingredDat[3]))
                    )
                )
            else:
                ingredPage.add_row( (ingredDat[0], ingredDat[1] + ' ' + ingredDat[2])  )
    
    
    ###################
    latexDoc.append( Command(
        'begin',
        ['tabularx', NoEscape(r"\textwidth"),
         NoEscape(r'p{.3\textwidth}X')]))
    
    ## Column 1
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
    latexDoc.append( LargeText( bold(labels['ingredients'])) )
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append(ingredPage )
    
    if recipeData.GetDescription():
        latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
        latexDoc.append( NoEscape(r'\par') )
        util_injectNotes(latexDoc, recipeData, labels)
    
    latexDoc.append( NoEscape(r'&'))
    
    ## Column 3
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
    if( recipeData.getPicturePrimary() ):
        util_addPicNotInFig(
            latexDoc, 
            recipeData.getPicturePrimary()['path'],
            '0.55',
            outLaTexAbsPath)
        latexDoc.append( Command('vspace', ['4pt'] ) )
        latexDoc.append( NoEscape(r'\par') )

    latexDoc.append( LargeText( bold(labels['directions'])) )
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append(recipeData.genStepsBlock('LaTex', latexDoc) )
    latexDoc.append( NoEscape(r'\\'))
    
    latexDoc.append( Command('end',['tabularx']))
    
    ## Setup for next page
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_AFTER]) )

#=============================================================================
def genRecipeFormatDefault(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels):
    '''
    Generic Recipe processing function
    '''
    util_reserve_recipe_header_space(latexDoc, RECIPE_HEADER_NEEDSPACE_LINES)
    util_FancyBuildHeader(latexDoc, recipeName)

    ## Create Recipe Header
    picForRecipe = ''
    if( recipeData.getPicturePrimary() ):
        picForRecipe = Figure(position='h!')
        picForRecipe.add_image(
            util_tex_image_path(recipeData.getPicturePrimary()['path'], outLaTexAbsPath),
            width=NoEscape(r"0.4\textwidth") )
    
    if recipeData.GetDescription():
        latexDoc.append( Command('vspace', [RECIPE_VSPACE_SMALL] ) )
        latexDoc.append( 
            italic( recipeData.GetDescription() )
        )
        latexDoc.append( NoEscape(r'\par') )
                                 
    # Create Recipe body

    ##----
    # Add in Ingredients
    ingredLaTex = recipeData.genIngredientsBlock('LaTex')
    ingredPage = Tabular('rl')
    ingredPage.add_empty_row()
    for ingredDat in ingredLaTex:
        if ('' == ingredDat[0] and '' == ingredDat[2]):
            ingredPage.add_row( ('', ingredDat[1])  )
        else:
            if( ingredDat[3] != None):
                ingredPage.add_row( 
                    ingredDat[0], 
                    (NoEscape(
                        ingredDat[1] + ' ' + 
                        ingredDat[2] +
                        ', ' + util_page_ref_text(labels, ingredDat[3]))
                    )
                )
            else:
                ingredPage.add_row( (ingredDat[0], ingredDat[1] + ' ' + ingredDat[2])  )
    
    ##---- Directions            
    dirPage =  recipeData.genStepsBlock('LaTex', latexDoc)
    
    with latexDoc.create( SmallText() ):
        latexDoc.append( Command('columnratio',[0.53]) )
        latexDoc.append( Command('begin',['paracol', 2], packages=[ Package('paracol')]) )
        latexDoc.append( ingredPage )
        latexDoc.append( picForRecipe )
        latexDoc.append(  Command('switchcolumn',packages=[ Package('paracol')]) )
        latexDoc.append( dirPage )
        latexDoc.append(  Command('end','paracol',packages=[ Package('paracol')]) )
    
    latexDoc.append( NoEscape(r'\par') )
    latexDoc.append( Command('vspace', [RECIPE_VSPACE_AFTER]) )

#=============================================================================
def genRecipeFormatCompactImageLeft(latexDoc, recipeName, recipeData, outLaTexAbsPath, labels):
    '''
    Compact layout with a fixed-size image on the left, ingredients on the right,
    instructions below, and notes at the end in italics.
    '''
    util_reserve_recipe_header_space(latexDoc, RECIPE_HEADER_NEEDSPACE_LINES)
    util_FancyBuildHeader(latexDoc, recipeName)

    ingredLaTex = recipeData.genIngredientsBlock('LaTex')
    ingredLines = [r'\textbf{%s}' % labels['ingredients']]
    for ingredDat in ingredLaTex:
        if ('' == ingredDat[0] and '' == ingredDat[2]):
            if len(ingredDat[1]):
                ingredLines.append(r'\textit{%s}' % ingredDat[1])
        else:
            qty = str(ingredDat[0]).strip()
            name = str(ingredDat[1]).strip()
            unit = str(ingredDat[2]).strip()
            parts = [p for p in (qty, name, unit) if p]
            line = ' '.join(parts)
            if ingredDat[3] != None:
                line = line + r', ' + util_page_ref_text(labels, ingredDat[3])
            ingredLines.append(line)

    ingredText = r'\par '.join(ingredLines)

    picCell = NoEscape(r'')
    if recipeData.getPicturePrimary():
        imgPath = util_tex_image_path(recipeData.getPicturePrimary()['path'], outLaTexAbsPath)
        picCell = NoEscape(r'\includegraphics[width=\linewidth]{%s}' % imgPath)

    with latexDoc.create( SmallText() ):
        latexDoc.append( NoEscape(r'{\setlength{\parindent}{0pt}') )
        if recipeData.getPicturePrimary():
            right_width = r'\dimexpr\textwidth-%s-10pt\relax' % RECIPE_IMG_FIXED_WIDTH
            latexDoc.append( NoEscape(r'\noindent\begin{minipage}[t]{%s}' % RECIPE_IMG_FIXED_WIDTH) )
            latexDoc.append( NoEscape(r'\vspace{0pt}') )
            latexDoc.append( picCell )
            latexDoc.append( NoEscape(r'\end{minipage}\hspace{10pt}\begin{minipage}[t]{%s}' % right_width) )
            latexDoc.append( NoEscape(r'\vspace{0pt}') )
            latexDoc.append( NoEscape(ingredText) )
            latexDoc.append( NoEscape(r'\end{minipage}') )
        else:
            latexDoc.append( NoEscape(r'\noindent') )
            latexDoc.append( NoEscape(ingredText) )
        latexDoc.append( NoEscape(r'}') )
        latexDoc.append( Command('vspace', ['6pt'] ) )
        latexDoc.append( NoEscape(r'\par') )
        latexDoc.append( NoEscape(r'{\setlength{\parindent}{0pt}') )
        latexDoc.append( NoEscape(r'\noindent') )
        latexDoc.append( bold(labels['instructions']) )
        latexDoc.append( NoEscape(r'\par') )
        latexDoc.append(recipeData.genStepsBlock('LaTex', latexDoc))
        latexDoc.append( NoEscape(r'}') )

        if recipeData.GetDescription():
            latexDoc.append( Command('vspace', ['2pt'] ) )
            latexDoc.append( NoEscape(r'\par') )
            latexDoc.append( italic( recipeData.GetDescription() ) )

        latexDoc.append( Command('vspace', ['4pt'] ) )
        latexDoc.append( NoEscape(r'\par\noindent\rule{\textwidth}{0.4pt}') )

    latexDoc.append( Command('vspace', [RECIPE_VSPACE_AFTER]) )

#=============================================================================
def getLateByIngredientIndex( doc, cookbookData):
    """
    Generate Latex code for a index of recipes by Ingredient
    """
    lstIngred = []
    dictIngred = {}
    txtExcludeList = ['Household', 'Spices', 'Oils']
    for ingredGrp in cookbookData['ingredients']['text_tree']:
        if( ingredGrp not in txtExcludeList):
            ingredGrpBase = cookbookData['ingredients']['text_tree'][ingredGrp] 
            for ingred in ingredGrpBase:
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
