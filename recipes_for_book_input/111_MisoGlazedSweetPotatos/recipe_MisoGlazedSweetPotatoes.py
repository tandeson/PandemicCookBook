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
        r = MyRecipe('Miso Glazed Sweet Potatoes', 'Appetizers', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('GlazedSweetPotatoes', 'IMG_3764.jpeg')
        r.addPicture('GlazedSweetPotatoes_1', 'IMG_3765.jpeg')
        r.setPrimaryPicture('GlazedSweetPotatoes')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Sweet Potatoes', 6, 'cups, cubed 3/4 inch')
        
        r.addIngredient('Miso Paste', 0.25, 'cups, 80 grams')
        r.addIngredient('Agave Nectar', 3, 'tablespoons, 60 grams')
        r.addIngredient('Soy Sauce', 2, 'teaspoons, 10 grams')
        r.addIngredient('Lemon Juice', 2, 'teaspoons, 12 grams')
        r.addIngredient('Red Pepper Flakes', 1.5, 'teaspoon, 10 grams')
        r.addIngredient('Sesame seeds', 1, 'teaspoon, 4 grams' )
        r.addIngredient('Ginger', 0.5, 'teaspoon, ground')
        r.addIngredient('Water', 3, 'tablespoons, 45 grams')
        
        ## Steps
        steps = [
            'Line a sheet pan with parchment paper and preheat the oven to 415 deg F, '
            'spread the potatoes out evenly.',
            
            'Bake for 15 minutes, give them a toss so they cook evenly and roast for 15-20 '
            'more minutes or until golden brown and cooked through, but not mushy. Check and '
            'taste one with a fork before removing.',
            
            'Meanwhile, make the glaze. Add all of the ingredients to a bowl and whisk until completely smooth.',
            
            'Let the potatoes cool for about 5 minutes and then add to a large pan with the glaze over low heat. '
            'Cook for just a couple of minutes so that the glaze thickens up a bit, but doesn\'t cook away.',
            
            'Serve immediately.'
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
