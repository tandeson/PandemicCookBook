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
        r = MyRecipe('Tzatziki Sauce', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('TzatzikiSauce', 'TzatzikiSauce.jpg')
        r.setPrimaryPicture('TzatzikiSauce')
        
        #  -- Add Ingredients --

        ##
        r.addIngredient('Greek Yogurt', 2, 'cups') 
        r.addIngredient('Cucumber', 0.5, 'finely diced')
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoons')
        r.addIngredient('Lemon Juice', 1, 'teaspoon')
        r.addIngredient('Dill', 3, 'tablespoons')
        r.addIngredient('Garlic', 6, 'cloves, finely diced')
        r.addIngredient('Salt', 1, 'teaspoon')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        
        # Add Steps and Notes
        steps = [
            'OPTIONAL: Press the Cucumber in cheese cloth or paper towels to remove moisture prior to mixing below.',
            'Mix the Greek Yogurt, Cucumber, Oil and Lemon Juice.',
            'When fully combined, add in the spices, mix well.'
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
