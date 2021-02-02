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
from pylatex import Document, Section, Subsection, SmallText, Command, Tabular, Tabularx, \
                    Foot, Head, PageStyle, NewPage, NewLine, \
                    Package, Figure
from pylatex.utils import NoEscape, italic
from pylatex.section import Chapter

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
        docFooter.append( NoEscape(r'\thepage\ ') )
    with styleBookContents.create( Foot("LE") ) as docFooter:
        docFooter.append( NoEscape(r'\thepage\ ') )
          
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
            
            with doc.create( Section( grpSectionName ) ):
                ## TODO - any info on this sections..
                doc.append( NewPage())
                
                for iRecipe in recipeList:
                    if (args.verbose):
                        print( "-Building LaTex Code for Recipe:%s" % ( iRecipe ) )
                    if (cookbookData['Recipes']['inputObjects'][iRecipe].getSection() == grpSectionName):
                        genRecipe(doc, iRecipe, cookbookData['Recipes']['inputObjects'][iRecipe] )
        
    
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
    with latexDoc.create ( Subsection( "%s" % ( recipeName )) ):
        ## Create Recipe Header
        picForRecipe = ''
        if( recipeData.getPicturePrimary() ):
            picForRecipe = Figure(position='h!')
            picForRecipe.add_image(
                str( Path( recipeData.getPicturePrimary()['path']).absolute() ),
                width=NoEscape(r"0.3\textwidth") )
        
        if recipeData.GetDescription():
            latexDoc.append( 
                SmallText( italic( recipeData.GetDescription() ))
            )
            latexDoc.append( NewLine() )
                                     
        with latexDoc.create( Tabularx( 'XXX', width_argument=NoEscape(r"\textwidth")) ) as recipeHeadTable:
            recipeHeadTable.add_empty_row()
            recipeHeadTable.add_hline()
        latexDoc.append( NewLine() )
        
        # Create Recipe body
        
                
        ##----
        # Add in Ingredients
        ingredLaTex = recipeData.genIngredientsBlock('LaTex')
        ingredPage = Tabular('rcl')
        ingredPage.add_empty_row()
        for ingredDat in ingredLaTex:
            ingredPage.add_row( ingredDat )
        
        ##---- Directions            
        dirPage =  recipeData.genStepsBlock('LaTex', latexDoc)
        
        ## Possible new Layout style
        ## \vspace{5pt}
        ## \begin{large}
        ## Ingredients
        ## \end{large}
        ## \hrule width 4in
        
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
