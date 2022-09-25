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
        r = MyRecipe('Sauerkraut Soup', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Onion', 1, 'large, diced')
        r.addIngredient('Leek', 1, 'medium, finely sliced')
        r.addIngredient('Carrot', 1, 'medium, diced')
        r.addIngredient('Parsnip', 1, 'medium, diced')
        r.addIngredient('Garlic', 4, 'cloves, chopped')
        r.addIngredient('Caraway seeds', 0.5, 'teaspoons')
        r.addIngredient('Marjoram', 1, 'teaspoon')
        r.addIngredient('Allspice', 1, 'teaspoon')
        r.addIngredient('Rosemary', 1, 'teaspoon')
        r.addIngredient('Bay Leaves', 3, '')
        r.addIngredient('Sauerkraut', 1, 'pound (400g), drained')
        r.addIngredient('Potato', 3, 'peeled and cut into cubes')
        r.addIngredient('Vegetable Broth', 6, 'cups')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')   
        
        # Add Steps and Notes
        steps= [
            'Heat the oil in a large stockpot and saute the onion for 2-3 minutes over medium heat.',
            'Add the leek, carrot and parsnip and continue to cook for 8-10 minutes until the veggies soften.',
            'Stir in the garlic, caraway seeds, marjoram, allspice, rosemary and bay leaves and continue to cook for 1-2 minutes, stirring occasionally.',
            'Add the sauerkraut and continue cooking for 1-2 minutes. Next, add a ladle of veggie stock and simmer for 10 minutes.',
            'Add the potatoes and the rest of the stock and simmer on a low heat for 25 minutes or until the potatoes are fork-tender.',
            'Season to taste and serve.',
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
