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
        r = MyRecipe('Clam Chowder', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Chowder', 'chowderInABowl.jpg')
        r.setPrimaryPicture('Chowder')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Unsalted Butter', 1 , 'tablespoon')
        r.addIngredient('Extra Virgin Olive Oil', 4, 'tablespoons')
        r.addIngredient('Garlic', 6, 'cloves, chopped')
        r.addIngredient('Yellow Onion', 1, 'large, chopped')
        r.addIngredient('Celery', 2, 'ribs, chopped')
        
        r.addIngredient('Potato', 3, 'large, cubed')
        r.addIngredient('Vegetable Broth', 3, 'cup' )
        r.addIngredient('Thyme', 3, 'teaspoon')
        r.addIngredient('Dill', 3, 'teaspoon')
        r.addIngredient('Salt', 2, 'teaspoons')
        r.addIngredient('Black Pepper', 1, 'teaspoon')
       
        r.addIngredient('Whole Milk', 3, 'cups')
        r.addIngredient('All Purpose Flour', 0.75, 'cups')
        
        r.addIngredient('Chopped Clams', 2, 'cans, 6.5 oz each')
        
         
        # Add Steps and Notes
        steps= [
            'In a large pot over medium-high heat, melt the Butter.',
            'Add in the Oil, Onion, Garlic and Celery. Saute until softened, mixing often.',
            'Add in the Potatoes, Broth, Thyme, Dill, Salt and Pepper.',
            'Bring to a boil, then reduce heat and simmer uncovered until potatoes are tender, 15 to 20 minutes.',
            'In a small bowl, combine flour and Milk. Gradually stir into soup. Bring to a boil and stir until thickened, 1 to 2 minutes.',
            'Stir in Clams with their juice and heat.',
            'Check seasoning - and add additional Salt, Pepper, Dill and Thyme to taste.'
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
