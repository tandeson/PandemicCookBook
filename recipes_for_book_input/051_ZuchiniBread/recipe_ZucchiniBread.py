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
        r = MyRecipe('Zucchini Bread', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('full_loaf', '2020ThanksgivingBread.jpg')
        r.setPrimaryPicture('full_loaf')
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Eggs', 3, 'large')
        r.addIngredient('Granulated White Sugar', 2, 'cups')
        r.addIngredient('Vegetable Oil', 1, 'cup')
        r.addIngredient('Zucchini', 2, 'cups, grated, raw')
        r.addIngredient('All Purpose Flour', 2, 'cups')
        r.addIngredient('Cinnamon', 3, 'teaspoons')
        r.addIngredient('Baking Soda', 2, 'teaspoons')
        r.addIngredient('Baking Powder', 0.25, 'teaspoon')
        r.addIngredient('Salt', 0.75, 'teaspoons')
        r.addIngredient('Walnuts', 1, 'cup, chopped')
        r.addIngredient('Vanilla', 2, 'teaspoons')
        
        # Add Steps and Notes
        steps= [
            'Preheat oven to 350 deg F.',
            'In a large bowl, beat eggs until light.',
            'Add sugar and oil and beat until well mixed.',
            'Sift flour with cinnamon, baking soda, baking powder, and salt. Add to bowl and mix.',
            'Add zucchini to bowl and mix.',
            'Add nuts and vanilla, mix well.',
            'In two greased and floured 8-inch by 4-inch baking pans, pour in the batter.',
            'Bake for 1 hour.'
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
