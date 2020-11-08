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
        r = MyRecipe('Moroccan Lentil Stew', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        ## Source: https://www.simplyquinoa.com/detox-moroccan-lentil-soup/
        #  -- Add Ingredients --

        ##
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoons')
        r.addIngredient('Onion', 1, 'cup, chopped')
        r.addIngredient('Celery', 1, 'cup, chopped')
        r.addIngredient('Carrot', 1, 'cup, chopped')
        r.addIngredient('Potato', 1, 'cup, chopped (Russet)')
        r.addIngredient('Garlic', 4, 'Cloves, minced')
        r.addIngredient('Salt', 1, 'teaspoon')
        r.addIngredient('Black Pepper', 1, 'teaspoon')
        r.addIngredient('Turmeric', 2, 'teaspoons')
        r.addIngredient('Cumin', 2, 'teaspoons')
        r.addIngredient('Ginger', 2, 'teaspoons (ground)')
        r.addIngredient('Smoked Paprika', 2, 'teaspoons')
        r.addIngredient('Cinnamon', 1, 'teaspoon')
        r.addIngredient('Brown Lentils', 1, 'cup')
        r.addIngredient('Vegetable Broth', 4, 'cups')
        r.addIngredient('Water', 2, 'cups')
        r.addIngredient('Tomato Paste', 0.25, 'cup')
        r.addIngredient('Coconut Milk', 1, 'cup')
        r.addIngredient('Lemon Juice', 1, 'tablespoon')
        r.addIngredient('Spinach', 2, 'cups')
        
        # Add Steps and Notes
        steps= [
            'Heat the oil in a large Pot.',
            'Add Onions, Celery, Carrot, Potato and Garlic. Saute for about 5 minutes until everything softens slightly.',
            'Season with salt, pepper and the spices and cook about 2 minutes.',
            'Add lentils and saute 1 - 2 minutes',
            'Add the broth, water and tomato paste. Stir to combine and until the tomato paste has dissolved.',
            'Bring the soup to a boil, cover and reduce to simmer for 30 minutes.',
            'Remove from heat and stir in Coconut milk, lemon juice, and spinach, and stir until the spinach has wilted.',
            'Serve immediately and top with your desired toppings.'
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
