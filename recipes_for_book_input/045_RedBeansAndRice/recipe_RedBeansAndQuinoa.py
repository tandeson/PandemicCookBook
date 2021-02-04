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
        r = MyRecipe('Red Beans and Quinoa', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BowlRedBeans', '2020_11_07_BowlBase.jpg')
        r.setPrimaryPicture( 'BowlRedBeans' )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Celery', 1, 'bunch, chopped')
        r.addIngredient('Yellow Onion', 1 ,'large, chopped')
        r.addIngredient('Garlic', 2, 'Cloves, minced')
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoons')
        r.addIngredient('Kidney Beans', 1, 'can, 16 oz')
        r.addIngredient('Vegetable Broth', 1.5, 'cups')
        r.addIngredient('Veggie Grillers Crumbles', 6, 'oz')
        r.addIngredient('Paprika', 1, 'tablespoon')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Quinoa', 2, 'cups, cooked')

        
        # Add Steps and Notes
        steps= [
            'Heat a cast Iron Frying pan on medium-high heat.',
            'When the pan is hot, add the Oil, Celery, Onion and Garlic. Cook until soft, stirring often.',
            'Pour the Vegetable broth into the pan.',
            'Drain and Rinse the Kidney Beans, then add to the pan. Add in the spices.',
            'Bring the mixture to a boil, and then simmer for 20 - 30 minutes, until reduced.',
            'Add in the Crumbles, cook until heated.',
            'Serve over Quinoa.'
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
