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
        r = MyRecipe('Banana Oat Bake', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Banana_oat_1', 'IMG_3160.jpeg')
        r.addPicture('Banana_oat_2', 'IMG_3161.jpeg')
        r.setPrimaryPicture('Banana_oat_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')  
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Unsalted Butter', 0.25 , 'cup, melted')
        r.addIngredient('Brown Sugar', 0.5, 'cup')
        r.addIngredient('Granulated White Sugar', 0.25, 'cup')
        r.addIngredient('All Purpose Flour', 1.25, 'cup')
        r.addIngredient('Oatmeal', 1.5, 'cup')
        r.addIngredient('Baking Soda', 0.5, 'teaspoons')
        r.addIngredient('Cinnamon', 1, 'teaspoon')
        r.addIngredient('Salt', 0.25, 'teaspoon')
        r.addIngredient('Vanilla', 2, 'teaspoon')
        
        r.addIngredient('Eggs', 1, 'large, lightly beaten')
        
        r.addIngredient('Banana', 1, 'cup, very ripe mashed (about 2)')
        r.addIngredient('Walnuts', 0.5, 'cups, coarsely chopped')
        r.addIngredient('Dark Chocolate chips', 1.25, 'cups')
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 350F, line a 9x9 inch pan with foil (or spray with cooking spray only), set aside',
            'In a bowl, combine egg, bananas, sugars, butter, vanilla, and mix or beat on medium speed until well combined',
            "Mix together oats, flour, cinnamon, baking soda, salt",
            "Combine the wet and dry ingredients",
            "Mix in the chocolate chips and walnuts, pour into pan",
            "Bake for 25 minutes. Allow to cool for at least 30 minutes before cutting"
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
