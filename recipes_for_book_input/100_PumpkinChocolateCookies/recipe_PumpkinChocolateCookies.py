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
        r = MyRecipe('Pumpkin Chocolate Cookies', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('PumpkinCookies', 'IMG_2899.jpeg')
        r.setPrimaryPicture('PumpkinCookies')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS') 
        #  -- Add Ingredients --
        
        ## 
        #--
        r.addIngredient('Pumpkin Puree', 1, 'cups')
        r.addIngredient('Oatmeal', 2, 'cups')
        r.addIngredient('Maple Syrup', 0.25, 'cups')
        r.addIngredient('Peanut Butter', 0.5, 'cups')
        r.addIngredient('Pumpkin Pie Spice', 1, 'teaspoon')
        r.addIngredient('Dark Chocolate chips', 0.3, 'cups')
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 350 deg F.',
            'Prepare 2 baking sheets with nonstick spray.',
            'Add Pumpkin, oats, syrup, peanut butter and pumpkin pie spice in a large bowl and with hand mixer mix for about 30 seconds.',
            'Form the dough into tablespoon sized balls. The dough should be sticky. To make balls easier to roll with sticky dough, lightly wetten your fingers. Place on cookie sheets.',
            'Gently press down each cookie with your fingers or spoon. You don\'t want to squash them you just want to flatten them into a cookie shape.',
            'Add chocolate chips ( about 5-8) on top of each cookie.',
            'Bake for 15-17 minuts.'
            ]
        
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        # Notes
        
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
