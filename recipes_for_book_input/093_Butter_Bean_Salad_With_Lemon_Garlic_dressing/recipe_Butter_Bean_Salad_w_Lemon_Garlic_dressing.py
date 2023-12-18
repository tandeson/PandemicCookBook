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
        r = MyRecipe('Butter Bean Salad with Lemon Garlic Dressing', 'Salads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('ButterBeans_1', 'ButterBeans_1.JPEG')
        r.addPicture('ButterBeans_2', 'ButterBeans_2.JPEG')
        r.addPicture('ButterBeans_3', 'ButterBeans_3.JPEG')
        r.setPrimaryPicture('ButterBeans_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        
        r.addIngredient('Butter Beans', 1, '15 oz can')
        
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoons')
        r.addIngredient('Lemon Juice', 2, 'tablespoons')
        r.addIngredient('Garlic', 3, 'cloves, minced')
        r.addIngredient('Parsley', 2, 'tablespoons, chopped')
        r.addIngredient('Mustard', 1, 'teaspoon, Dijon')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        
        # Add Steps and Notes
        steps= [
            'Drain and Rinse beans, put into a bowl.',
            'In a separate bowl, mix together the rest of the ingredients. Adjust seasoning then add the beans.',
            'Marinate - ideally for at least a few hours.'
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
