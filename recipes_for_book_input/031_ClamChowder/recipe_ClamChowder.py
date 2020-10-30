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
        r = MyRecipe('Clam Chowder', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        #  -- Add Ingredients --

        ##
        r.addIngredient('Unsalted Butter', 1 , 'tablespoon')
        r.addIngredient('Extra Virgin Olive Oil', 4, 'tablespoons')
        r.addIngredient('Garlic', 4, 'cloves, chopped')
        r.addIngredient('Yellow Onion', 1, 'large, chopped')
        r.addIngredient('Celery', 4, 'ribs, chopped')
        
        r.addIngredient('Potato', 4, 'medium, skinned and cubed')
        r.addIngredient('Vegetable Broth', 1, 'cup' )
        r.addIngredient('Thyme', 1, 'teaspoon')
        r.addIngredient('Salt', 2, 'teaspoons')
        r.addIngredient('Black Pepper', 1, 'teaspoons')
       
        r.addIngredient('Whole Milk', 2, 'cups')
        r.addIngredient('All Purpose Flour', 0.25, 'cups')
        
        r.addIngredient('Chopped Clams', 2, 'cans, 6.5 oz each')
        
         
        # Add Steps and Notes
        steps= [
            'In a large pot over medium-high heat, melt the Butter.',
            'Add in the Oil, Onion and Celery. Saute until softened, mixing often.',
            'Add in the  Garlic and cook 1 minute longer.',
            'Add in the Potatos, Broth, Thyme, Salt and Pepper.',
            'Bring to a boil, then reduce heat and simmer uncovered until Potatos are tender, 15-20 minutes',
            'In a small bowl, combine flour and Milk. Gradually stir into soup. Bring to Boil an stir until thickened, 1 - 2 minutes.',
            'Stir in Clams with their juice and heat.'
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
