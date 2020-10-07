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

from pathlib import Path

## For rendering options
from pylatex import Document, Section, SmallText, Command, Tabular, Tabularx, \
                    simple_page_number, Foot, PageStyle, NewPage, NewLine, \
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
        geometry_options = {
            #'head': '40pt',
            'margin': '0.5in',
            'bottom': '0.6in',
            'includeheadfoot': True
            }
         )
    
    ## Setup Syle for Recipe pages
    styleBookContents = PageStyle("styleBookContents")
    #with styleBookContents.create( Head("C")) as docHeader:
    #    docHeader.append("The Pandemic Cookbook")
    with styleBookContents.create( Foot("C") ) as docFooter:
        docFooter.append( simple_page_number() )
    doc.preamble.append(styleBookContents)
    doc.change_document_style("styleBookContents")
    
    ## --------------------
    ## Build Up the Recipe Book Structure
    genTitlePage(doc)
    
    # Add in the Table of Contents
    doc.append( Command('tableofcontents') )
    
    # Add in the Recipes
    with doc.create( Chapter('Recipes') ):
        doc.append( 
            italic(
                "The following are the things we've been cooking together as we find ways to "
                "keep busy inside and away from people. We've been enjoying them, and we hope you do too.")
            )
        doc.append( NewPage())
        
        for iRecipe in cookbookData['Recipes']['inputObjects'].keys() :
            if (args.verbose):
                print( "Building LaTex Code for Recipe:%s" % ( iRecipe ) )
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
    latexDoc.preamble.append(Command('author', 'Bilyana Yakova and Thomas Anderson'))
    latexDoc.preamble.append(Command('date', NoEscape(r'\today')))
    latexDoc.append(NoEscape(r'\maketitle'))

#=============================================================================
def genRecipe( latexDoc, recipeName, recipeData ):
    """
    Format a Recipe into LaTex
    """
    with latexDoc.create ( Section( "%s" % ( recipeName )) ):
        ## Create Recipe Header
        picForRecipe = ''
        if( recipeData.getPicturePrimary()['path'] ):
            picForRecipe = Figure(position='h!')
            picForRecipe.add_image(
                str( Path(os.path.join( recipeData.getPathLoc(), recipeData.getPicturePrimary()['path'])).absolute() ),
                width=NoEscape(r"0.3\textwidth") )
                                 
        with latexDoc.create( Tabularx( 'XXX', width_argument=NoEscape(r"\textwidth")) ) as recipeHeadTable:
            recipeHeadTable.add_row( (
                '',
                '', #bold( recipeName ),
                '.'
                ))
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
        dirPage = recipeData.genStepsBlock('LaTex', latexDoc)
        
        with latexDoc.create( SmallText() ):
            latexDoc.append( Command('begin',['paracol', 2], packages=[ Package('paracol')]) )
            latexDoc.append( ingredPage )
            latexDoc.append( picForRecipe )
            latexDoc.append(  Command('switchcolumn',packages=[ Package('paracol')]) )
            latexDoc.append( dirPage )
            latexDoc.append(  Command('end','paracol',packages=[ Package('paracol')]) )
        
        #with latexDoc.create( Tabularx( 'XX', width_argument=NoEscape(r"\textwidth")) ) as recipeBodyTable:
        #    recipeBodyTable.add_row( ingredPage, dirPage )
        
        latexDoc.append( NewPage() )
            

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
