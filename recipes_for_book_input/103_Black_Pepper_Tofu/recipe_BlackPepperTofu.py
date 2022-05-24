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
        r = MyRecipe('Black Pepper Tofu', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BlackPepperTofu', 'BlackPepperTofu.jpg')
        r.setPrimaryPicture( 'BlackPepperTofu')
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Textured Tofu', 1, 'block, extra-firm')
        
        r.addIngredient('Corn Starch', 0.5, 'cups')
        
        r.addIngredient('Soy Sauce', 3, 'tablespoons')
        r.addIngredient('Oyster Sauce', 1, 'tablespoon')
        r.addIngredient('Water', 2, 'tablespoons')
        r.addIngredient('Garlic', 6, 'cloves, diced')
        r.addIngredient('Ginger', 2, 'tablespoons, diced')
        r.addIngredient('Green Onion', 3,'stalks, chopped')
        r.addIngredient('Black Pepper',1,'pinch, to taste')
        
        r.addIngredient('Vegetable Oil', 2, 'tablespoons')

        
        
        ## Steps
        steps = [
            'Slice tofu into pieces resembling checkers - long rectangles.',
            'Coat Tofu pieces in Corn Starch.',
            'In a bowl, mix the Soy Sauce, Oyster Sauce, Water, Garlic, Ginger, Greens Onions and Black Pepper - and mix. Set Aside',
            'Heat a frying pan with oil.',
            'Fry the tofu, turning in order to fry all sides. Add the sauce and mix. Remove from heat and serve.'
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
