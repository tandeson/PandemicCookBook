#!/usr/bin/env python
#*****************************************************************************
"""
    Make A recipe
"""
#*****************************************************************************

#*  Imports ******************************************************************
import sys

from scripts.myRecipe import MyRecipe
from scripts.myRecipe import RecipeStep

#*  Constants ****************************************************************
# PY-2.10
# DELIMITER = ","

#*  Class and Function Definitions *******************************************

#=============================================================================
def makeRecipe( dirPathRecipe, sharedIngredentList ):
        """
        Make this specific Recipe
        """
        r = MyRecipe('Sourdough Bread', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BreadLoafs', '2020_04_13_Loafs.JPG')
        r.addPicture('SlicedRounds', '2020_05_13_Roudloaf_Sliced.JPG')
        r.addPicture('Rounds', '2020_05_13_RoundLoafs.JPG')
        r.setPrimaryPicture( 'BreadLoafs')
        
        #  -- Add Ingredients --

        ## Garlic
        r.addToDoNote('Add rest of ingredients.')
        r.addIngredient('Bread Flour', 602, 'grams ( 5 cups)')
           
        # Add Steps and Notes
        steps = [
            '..',
             ]
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        
        # Return this back.
        return r

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
