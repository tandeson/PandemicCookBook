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

import sys

from CookbookConst import C_BOOK_SECTIONS

from pathlib import Path

from PIL import Image

## For rendering options
from pylatex import Document, Section, Subsection, LargeText, SmallText, \
                    Command, Tabular, Tabularx,  Center, \
                    Foot, Head, PageStyle, NewPage, NewLine, \
                    Package, Figure
from pylatex.utils import NoEscape, italic, bold
from pylatex.section import Chapter
from pylatex.basic import NewLine

#*  Constants ****************************************************************

#=============================================================================
def genLaTexOut(args, outAbsPath, cookbookData, gitRepo):
    
    outLaTexAbsPath = Path( os.path.join( outAbsPath, 'LaTex') )
    outLaTexAbsPath.mkdir(parents=True, exist_ok=True)
    
    outLaTexAbsFilePath =  Path( os.path.join( outLaTexAbsPath, 'Pandemic_Cookbook') )
    
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
    genTitlePage(doc)
    
    # Add in the Table of Contents
    doc.append( Command('tableofcontents') )
    
    # Add in the Recipes
    doc.change_document_style("styleBookContents")
    with doc.create( Chapter('Recipes') ):
        doc.append( Command('thispagestyle', [ strNameBookStyle]) )
        doc.append( 
            italic(
                "The following are the things we've been cooking together as we find ways to "
                "keep busy inside and away from people. We've been enjoying them, and we hope you do too.")
            )
        doc.append( NewPage())
        
        recipeList = list( cookbookData['Recipes']['inputObjects'].keys() )
        recipeList.sort()
        
        for grpSectionName in C_BOOK_SECTIONS:
            if (args.verbose):
                    print( "Building LaTex Code for Section:%s" % ( grpSectionName ) )
            
            with doc.create(Center()):
                doc.append( Command('rule',['4in', '0.4pt'] ) )
                doc.append( Section(  grpSectionName  ) )
                doc.append( Command('rule',['4in', '0.4pt'] ) )
                
            ## TODO - any info on this sections..
            doc.append( NewPage())
            
            for iRecipe in recipeList:
                if (args.verbose):
                    print( "-Building LaTex Code for Recipe:%s" % ( iRecipe ) )
                if (cookbookData['Recipes']['inputObjects'][iRecipe].getSection() == grpSectionName):
                    genRecipe(doc, iRecipe, cookbookData['Recipes']['inputObjects'][iRecipe] )
    
        with doc.create( Chapter('Index') ):
            doc.append( Command('thispagestyle', [ strNameBookStyle]) )
            
            doc.append( Command('twocolumn ',[],[NoEscape(r'\section{By Ingredient} \label{sec:ByIngredient}')]) )
            getLateByIngredientIndex( doc, cookbookData)
            
            
            doc.append( Command('onecolumn ') )
            
    ## --------------------
    ## Do the generation
    if(args.verbose):
        print("Building LaTex file: %s" % (outLaTexAbsFilePath) )
    
    doc.generate_pdf(
        outLaTexAbsFilePath, 
        clean_tex=False)
    
    if(args.verbose):
        print("Finished Building LaTex file: %s" % (outLaTexAbsFilePath) )


#=============================================================================
def genTitlePage( latexDoc ):
    """
    Build the Title Page
    """
    latexDoc.preamble.append(Command('title', 'The Pandemic Cookbook'))
    latexDoc.preamble.append(Command('author', NoEscape(r'Bilyana Yakova \and Thomas Anderson')))
    latexDoc.preamble.append(Command('date', NoEscape(r'\today')))
    latexDoc.append(NoEscape(r'\maketitle'))

#=============================================================================
def genRecipe( latexDoc, recipeName, recipeData ):
    """
    Format a Recipe into LaTex
    """
    if( recipeData.getRecipeFormat() == 'TWO_COLUMN_OPTIONAL_PICTURES'): 
        genRecipeFormatDefault( latexDoc, recipeName, recipeData )
    elif( recipeData.getRecipeFormat() == 'FANCY_WIDE_PIC_OVER_DIRECTIONS'):
        genRecipeFormatFancyWidePic( latexDoc, recipeName, recipeData )
    elif( recipeData.getRecipeFormat() == 'FANCY_TALL_PIC_OVER_INSTRUCTIONS'):
        genRecipeFormatFancyTallPic( latexDoc, recipeName, recipeData )
    elif( recipeData.getRecipeFormat() == 'FANCY_LONG_RECIPE'):
        genRecipeFormatFancyLong( latexDoc, recipeName, recipeData )
    else:
        raise Exception("Unknown Latex Recipe Format! - %s" % (recipeData.getRecipeFormat()))

#=============================================================================
# Helpers
#=============================================================================

#=============================================================================
def util_FancyBuildHeader( latexDoc, recipeName  ):
    '''
    Fancy Head build
    '''
    #latexDoc.append( Command('hrule' ))
    #latexDoc.append( Command('vspace', ['5pt']))
    with latexDoc.create(Center()) as centered:
        centered.append( Subsection( "%s" % ( recipeName )))
    latexDoc.append( Command('hrule' ))

#=============================================================================
def util_injectNotes( latexDoc, recipeData  ):
    latexDoc.append( Command('vspace', ['10pt'] ) )
    latexDoc.append( LargeText( bold('Notes')) )
    latexDoc.append( NewLine()  )
    latexDoc.append( 
            SmallText( italic( recipeData.GetDescription() ))
        )
#=============================================================================
def util_addPicNotInFig(latexDoc, strPicPath, widthNum):
    '''
    Helper to put picture in that isn't in a figure.
    '''
    latexDoc.append( Command(
        'includegraphics',
        NoEscape( strPicPath ),
        NoEscape(r'width=' + widthNum + r'\columnwidth'))
    )
    latexDoc.append( NewLine() )

#=============================================================================
def util_refRecipePageNum( strRecipeName):
    '''
    Done this way in order to allow for injection into tables with additional text.
    '''
    return NoEscape(r'\pageref{subsec:%s}' % (strRecipeName.replace(" ", "") ))

#=============================================================================
# Builders
#=============================================================================

#=============================================================================
def genRecipeFormatFancyLong( latexDoc, recipeName, recipeData  ):
    
    ingredLaTex = recipeData.genIngredientsBlock('LaTex')   

    util_FancyBuildHeader(latexDoc, recipeName)
    
    ## Create Recipe Header
    picForRecipe = ''
    if( recipeData.getPicturePrimary() ):
        picForRecipe = Figure(position='h')
        picForRecipe.add_image(
            str( Path( recipeData.getPicturePrimary()['path']).absolute() ),
            width=NoEscape(r"0.3\textwidth") )
    
    latexDoc.append( Command('vspace', ['10pt'] ) )
    
    if recipeData.GetDescription():
        latexDoc.append( 
            italic( recipeData.GetDescription() )
        )
        latexDoc.append( NewLine() )
                                 
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
                latexDoc.append( Command('vspace', ['10pt'] ) )
                latexDoc.append( NoEscape('\n') )
                latexDoc.append( ingredDat[1] )
                latexDoc.append( NewLine() )
        else:
            if( ingredDat[3] != None):
                latexDoc.append( 
                    NoEscape(
                        str(ingredDat[0]) + ' ' + 
                        ingredDat[1] + ' ' + 
                        ingredDat[2] + ', pg ' + util_refRecipePageNum(ingredDat[3]) 
                        )
                    )
                latexDoc.append( NewLine() )
            else:
                latexDoc.append( str(ingredDat[0]) + ' ' + ingredDat[1] + ' ' + ingredDat[2] )
                latexDoc.append( NewLine() )
    
  
    if( recipeData.getPicturePrimary() ):
        latexDoc.append( Command('begin', ['center']) )
        util_addPicNotInFig(
            latexDoc, 
            Path( recipeData.getPicturePrimary()['path']).absolute().as_posix(), 
            '0.3')
        latexDoc.append( Command('end', ['center']) )
        
    latexDoc.append( Command('end',['wrapfigure']) )

    recipeData.genStepsBlock('LaTex_indented_InjectHere', latexDoc)
    
    ##----
    # Add in Ingredients
         
    latexDoc.append( NewPage() )
    
#=============================================================================
def genRecipeFormatFancyTallPic( latexDoc, recipeName, recipeData  ):
    '''
    Fancy formating with inspiration from https://www.etsy.com/listing/827640730/printable-recipe-book-kit-editable
    '''

    ## Setup header
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
                        ', pg ' + util_refRecipePageNum( ingredDat[3]) )
                    )
                )
            else:
                ingredPage.add_row( (ingredDat[0], ingredDat[1] + ' ' + ingredDat[2])  )
    
    
    ###################
    latexDoc.append( Command('begin',['tabularx',NoEscape(r"\textwidth"),  NoEscape(r' p{.5\textwidth}p{.01\textwidth}X')]))
    
    ## Column 1
    if( recipeData.getPicturePrimary() ):
        latexDoc.append( Command('hline') )
        latexDoc.append( Command('vspace', ['5pt'] ) )
        util_addPicNotInFig(
            latexDoc, 
            Path( recipeData.getPicturePrimary()['path']).absolute().as_posix(), 
            '0.45')
    
    latexDoc.append( Command('vspace', ['10pt'] ) )
    latexDoc.append( LargeText( bold('Ingredients')) )
    latexDoc.append( NewLine() )
    latexDoc.append(ingredPage )
    
    
    latexDoc.append( NoEscape(r'&'))
       
    ## Column 2
    latexDoc.append( Command('vrule depth  7in' ) )
    latexDoc.append( NoEscape(r'&'))
    
    ## Column 3
    latexDoc.append( Command('vspace', ['10pt'] ) )
    
    latexDoc.append( LargeText( bold('Directions')) )
    latexDoc.append( NewLine() )
    latexDoc.append(recipeData.genStepsBlock('LaTex', latexDoc) )
    
    
    if recipeData.GetDescription():
        util_injectNotes( latexDoc, recipeData  )
         
    latexDoc.append( NoEscape(r'\\'))
    
    latexDoc.append( Command('end',['tabularx']))
    
    ## Setup for next page
    latexDoc.append( NewPage() )

#=============================================================================
def genRecipeFormatFancyWidePic( latexDoc, recipeName, recipeData  ):
    '''
    Fancy formating with inspiration from https://www.etsy.com/listing/827640730/printable-recipe-book-kit-editable
    '''

    ## Setup header
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
                        ', pg ' + util_refRecipePageNum(ingredDat[3]))
                    )
                )
            else:
                ingredPage.add_row( (ingredDat[0], ingredDat[1] + ' ' + ingredDat[2])  )
    
    
    ###################
    latexDoc.append( Command('begin',['tabularx',NoEscape(r"\textwidth"),  NoEscape(r' p{.3\textwidth}p{.01\textwidth}X')]))
    
    ## Column 1
    latexDoc.append( Command('vspace', ['10pt'] ) )
    latexDoc.append( LargeText( bold('Ingredients')) )
    latexDoc.append( NewLine() )
    latexDoc.append(ingredPage )
    
    if recipeData.GetDescription():
        latexDoc.append( Command('vspace', ['10pt'] ) )
        latexDoc.append( NewLine() )
        util_injectNotes( latexDoc, recipeData  ) 
    
    latexDoc.append( NoEscape(r'&'))
       
    ## Column 2
    latexDoc.append( Command('vrule depth  7in' ) )
    latexDoc.append( NoEscape(r'&'))
    
    ## Column 3
    latexDoc.append( Command('vspace', ['10pt'] ) )
    if( recipeData.getPicturePrimary() ):
        util_addPicNotInFig(
            latexDoc, 
            Path( recipeData.getPicturePrimary()['path']).absolute().as_posix(), 
            '0.55')
        latexDoc.append( Command('vspace', ['5pt'] ) )
        latexDoc.append( NewLine() )

    latexDoc.append( LargeText( bold('Directions')) )
    latexDoc.append( NewLine() )
    latexDoc.append(recipeData.genStepsBlock('LaTex', latexDoc) )
    latexDoc.append( NoEscape(r'\\'))
    
    latexDoc.append( Command('end',['tabularx']))
    
    ## Setup for next page
    latexDoc.append( NewPage() )

#=============================================================================
def genRecipeFormatDefault( latexDoc, recipeName, recipeData  ):
    '''
    Generic Recipe processing function
    '''
    util_FancyBuildHeader(latexDoc, recipeName)

    ## Create Recipe Header
    picForRecipe = ''
    if( recipeData.getPicturePrimary() ):
        picForRecipe = Figure(position='h!')
        picForRecipe.add_image(
            str( Path( recipeData.getPicturePrimary()['path']).absolute() ),
            width=NoEscape(r"0.3\textwidth") )
    
    if recipeData.GetDescription():
        latexDoc.append( Command('vspace', ['10pt'] ) )
        latexDoc.append( 
            italic( recipeData.GetDescription() )
        )
        latexDoc.append( NewLine() )
                                 
    with latexDoc.create( Tabularx( 'XXX', width_argument=NoEscape(r"\textwidth")) ) as recipeHeadTable:
        recipeHeadTable.add_empty_row()
    latexDoc.append( NewLine() )
    
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
                        ', pg ' + util_refRecipePageNum(ingredDat[3]))
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
    
    latexDoc.append( NewPage() )

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
                lstIngred.append( ingred )
                dictIngred[ ingred ] = ingredGrpBase[ingred] 
    
    lstIngred.sort()
    
    doc.append( ' ' )
    doc.append( Command( 'noindent') )
    GrpLetter = ' '
    for ingItem in lstIngred:
        if (GrpLetter != ingItem[0].upper() ):
            GrpLetter = ingItem[0].upper()
            doc.append( NewLine() )
            doc.append( bold( GrpLetter ) )
            doc.append( NewLine() )
        doc.append( ingItem )
        lstRecipe = list( dictIngred[ingItem]['ingred'].getRecipeList() )
        lstRecipe.sort()
        for itemLstRecipe in lstRecipe:
            doc.append( NewLine() )
            doc.append( Command(NoEscape(r'hspace*'), ['3 mm']) )
            doc.append( itemLstRecipe + ',')
            doc.append( util_refRecipePageNum( itemLstRecipe) )
        doc.append( NewLine() )
        
    #listIngred = 'ingredients'

#=============================================================================
def buildPdfImg( outAbsPath, inFilePath, inMaxDpi=300, inMaxSizeInch=4):
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
    myImage = myImage.resize( 
        ( int( sizeInIncW * sizeInIncRatio * newDpioutW) , int(sizeInIncH * sizeInIncRatio * newDpioutH) ), 
        Image.ANTIALIAS)
    
    myImage.convert('RGB').save(
        outFilePath, 
        dpi=(newDpioutW, newDpioutH)
        )
    
    if( False ):
        print(
            "Coverting image %s to lower res at %s" % 
            (inFilePath, outFilePath) )
        
    return outFilePath

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
