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
        r = MyRecipe('Fried Tofu',  'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Tofu_1', '20201_Tofu_1.JPEG')
        r.addPicture('Tofu_2','2021_Tofu_2.JPEG')
        r.setPrimaryPicture('Tofu_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Textured Tofu', 14, 'oz, drained, extra firm')
        r.addIngredient('Soy Sauce', 2, 'tablespoons')
        r.addIngredient('Corn Starch', 3, 'tablespoons')
        r.addIngredient('Garlic Powder', 1, 'teaspoon')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoons')
        
        # Add Steps and Notes
        steps= [
            'Cut the Tofu into roughly 1" cubes.',
            'Marinate in the Soy Sauce for at least 5 minutes. Most of it should be absorbed by the Tofu.',
            'Heat a large frying pan on medium-high heat.',
            'Mix the Corn Starch, Garlic Powder, Salt and Pepper together in a bowl or plastic bag.',
            'Coat the Tofu with the mixture.',
            'When the frying pan is hot, add the Oil and fry the Tofu one layer at a time. Turn as the sides brown.',
            'Once they are browned, remove them from the pan.',
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
