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
        r = MyRecipe('Potato Leek Soup', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('potatoeSoup_1', 'IMG_3496.jpeg')
        r.addPicture('potatoeSoup_2', 'IMG_3497.jpeg')
        r.setPrimaryPicture('potatoeSoup_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Onion', 1, 'medium, chopped')
        r.addIngredient('Garlic', 5, 'cloves, chopped')
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoons')
        r.addIngredient('Leek', 4, 'large, chopped')
        r.addIngredient('Thyme', 1, 'teaspoon')
        r.addIngredient('Rosemary', 1, 'teaspoon, dried')
        r.addIngredient('Coriander Powder', 0.5, 'teaspoon')
        r.addIngredient('Potato', 6, 'medium, peeled and chopped')
        r.addIngredient('Vegetable Broth', 4, 'cups')
        r.addIngredient('Almond Milk', 14, 'oz (or other cream)')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        
        # Add Steps and Notes
        steps= [
            'Add the chopped onion and leeks to a pot with the crushed garlic and '
            'olive oil and saute until softened. Add in the thyme, rosemary and coriander '
            'powder and saute.',
            
            'Add the chopped potatoes and vegetable stock and bring to a boil. Reduce the '
            'heat, cover the pot and simmer until the potatoes are soft and cooked.',
            
            'Remove from the heat and add in the cream',
            
            'Blend the soup using an immersion blender until smooth.',
            'Add Salt and Pepper to taste - and enjoy!'
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
