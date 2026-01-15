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
        r = MyRecipe('Sticky Tofu', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Textured Tofu', 1, 'block, extra-firm')
        r.addIngredient('Soy Sauce', 2, 'tablespoons')
        r.addIngredient('Hoisin Sauce', 1, 'tablespoon')
        r.addIngredient('Sriracha', 1, 'teaspoon')
        r.addIngredient('Sesame Oil',1, 'teaspoon')
        r.addIngredient('Corn Starch', 3, 'tablespoon')
        r.addIngredient('Water', 1.3, 'cups')
        r.addIngredient('Sesame seeds', 1, 'tablespoon')
        
        ## Steps
        steps = [
            'Slice tofu into pieces resembling checkers - long rectangles.',
            'Coat Tofu pieces in 2 tablespoons of Corn Starch.',
            'Bake at 350 deg F for 15 minutes.'
            'Mix all remaining ingredients together in a pan and heat on medium until it thickens. Toss the tofu in it.',
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
