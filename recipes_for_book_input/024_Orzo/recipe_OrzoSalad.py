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
        r = MyRecipe('Orzo Salad', 'Salads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Orzo_big_bowl', 'IMG_2358.JPEG')
        r.addPicture('Orzo_bowl', 'IMG_2359.JPEG')
        r.setPrimaryPicture('Orzo_big_bowl')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')

        #  -- Add Ingredients --

        ##
        r.addIngredient('Orzo', 3, 'cups, cooked (1.5 cup dry)') 
        r.addIngredient('Cucumber', 1, 'seeded and chopped')
        r.addIngredient('Red Onion', 1, 'medium, chopped')
        r.addIngredient('Feta Cheese', 1, 'cup, crumbled')
        r.addIngredient('Black Olives', 2, 'oz, sliced')
        r.addIngredient('Parsley', 0.25, 'cup, chopped')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        
        r.addIngredient('Extra Virgin Olive Oil', 6, 'tablespoons')
        r.addIngredient('Apple Cider Vinegar', 5, 'tablespoons')
        r.addIngredient('Lemon Juice', 2, 'tablespoons')
        
        # Add Steps and Notes
        steps = [
            'Mix all the ingredients together. NOTE: You can use Tzatziki sauce instead of Oil, Vinegar and Lemon Juice.',
            'Mix well, and let chill for 1 hour.'
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
