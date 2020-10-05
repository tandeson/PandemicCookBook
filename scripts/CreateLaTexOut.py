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
from pylatex import Document, Section, Subsection, Command, Tabular
from pylatex.utils import NoEscape

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
        documentclass='book')
    
    ## --------------------
    ## Build Up the Recipe Book Structure
    genTitlePage(doc)
    
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
    doc.generate_tex()
    
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
    with latexDoc.create (Section( "%s" % ( recipeName ), numbering=False) ):
        
        with latexDoc.create (Subsection( "Ingredients", numbering=False ) ):
            
            # Add in Ingredients
            ingredLaTex = recipeData.genIngredientsBlock('LaTex')
            with latexDoc.create(Tabular('rcl')) as table:
                for ingredDat in ingredLaTex:
                    table.add_row( ingredDat )
        
        with latexDoc.create (Subsection( "Directions", numbering=False ) ):
            recipeData.genStepsBlock('LaTex', latexDoc)
            

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
