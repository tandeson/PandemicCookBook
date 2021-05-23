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
        r = MyRecipe('Greek Salad', 'Salads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('SaladInBowl','IMG_2312.JPEG')
        r.addPicture('SaladClose','IMG_2313.JPEG')
        r.setPrimaryPicture( 'SaladInBowl' )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Falafel Mix', 1, 'box')
        r.addIngredient('Romaine Lettuce', 2, 'heads, chopped')
        r.addIngredient('Feta Cheese', 0.5, 'cups')
        r.addIngredient('Red Onion', 1, 'medium, chopped')
        r.addIngredient('Cucumber', 0.25, 'cubed')
        r.addIngredient('Tomatoes', 2, 'seeded and cubed')
        r.addIngredient('Black Olives', 0.25, 'cup')
        r.addIngredient('Pepperoncini', 0.25, 'cups, to taste')
        r.addIngredient('Tzatziki Sauce', 0.5, 'cups')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
                         
        # Add Steps and Notes
        steps= [
            'Make the Falafel by mixing in water as directed on the package.'
            ' Wait 10 minutes. Form, then bake at 400 deg F for 20 minutes on '
            'parchment paper.',
            'Place all the ingrediants in a large bowl and mix.'
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
