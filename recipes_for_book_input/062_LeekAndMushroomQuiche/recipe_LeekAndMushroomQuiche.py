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
        r = MyRecipe('Leek and Mushroom Quiche', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        #  -- Add Ingredients --

        ##
        r.addIngredient('Premade Pastry Shell', 1, 'shell')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'teaspoons')
        r.addIngredient('Leek', 3, 'thinly sliced')
        r.addIngredient('Mushrooms', 4, 'oz, sliced')
        r.addIngredient('Thyme', 0.25, 'teaspoon')
        r.addIngredient('Cheddar Cheese', 1, 'cup, shredded')
        r.addIngredient('Eggs', 4, 'medium')
        r.addIngredient('Evaporated Milk', 1, 'can, 12 oz')                
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Nutmeg', 0.25, 'teaspoon, to taste')
        
                                      
        # Add Steps and Notes
        steps= [
            'Shape the pastry shell in a pie dish.',
            'Preheat oven to 425 deg F.',
            'In a skillet heat the oil on medium high heat. Saute the leeks and mushrooms until tender.',
            'Stir in the thyme, and pour the mixture into the pastry shell.',
            'Sprinkle with cheese.',
            'In a bowl, wisk the eggs, milk, salt, pepper and nutmeg. Pour into the pastry shell.',
            'Bake for 15 minutes. Then reduce heat to 375 deg F, and bake for another 20 - 25 minutes.',
            'Let stand for at least 10 minutes before cutting.'
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
