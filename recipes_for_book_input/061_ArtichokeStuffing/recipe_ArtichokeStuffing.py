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
        r = MyRecipe('Artichoke Stuffing', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('FullTable', '2020Thanksgiving.jpg')
        r.setPrimaryPicture('FullTable')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Bread', 1, 'loaf (1 pound),sourdough')
        r.addIngredient('Mushrooms', 0.5, 'pounds, sliced')
        r.addIngredient('Celery', 2, 'ribs, chopped')
        r.addIngredient('Yellow Onion', 1, 'medium, chopped')
        r.addIngredient('Garlic', 6, 'cloves, minced')
        r.addIngredient('Salted Butter', 2, 'tablespoons')
        r.addIngredient('Artichoke Hearts', 13, 'oz, marinated, chopped')
        r.addIngredient('Parmesan Cheese', 0.5, 'cup, grated')
        r.addIngredient('Poultry Seasoning', 1, 'teaspoon')
        r.addIngredient('Eggs', 1, 'large')
        r.addIngredient('Vegetable Broth', 14.5, 'oz')
                              
        # Add Steps and Notes
        steps= [
            'Preheat the oven to 350 deg F.',
            'Cube the bread into 1 inch cubes.',
            'Place the bread in a large ungreased baking pan. Bake for 15 minutes until lightly browned.',
            'In a large skillet, saute the Mushrooms, Celery, Onion and Garlic in butter until tender.',
            'Stir in the Artichokes, Parmesan Cheese and Poultry Seasoning.',
            'Transfer to a large bowl. Stir in bread cubes.',
            'In a small bowl, wisk egg and brother until blended.',
            'Pour over bread mixture and mix well.',
            'Transfer to a greased 3 quart baking dish ( the dish will be full).',
            'Cover and ake for 30 minutes.',
            'Uncover - bake 5 - 15 minutes longer until a thermometer reads 160 deg F.',
            'Remove and serve.'
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
