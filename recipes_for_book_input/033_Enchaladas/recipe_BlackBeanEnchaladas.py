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
        r = MyRecipe('Black Bean Enchiladas', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('RedSauceEnchalads', 'blackBeanEnchaladas_2020.jpg')
        r.setPrimaryPicture('RedSauceEnchalads')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Enchilada Sauce', 1, 'can, 28 oz')
        r.addIngredient('Black Beans', 1, 'can, 15 oz')
        r.addIngredient('Shredded Mexican Cheese', 2, 'cups')
        r.addIngredient('Black Olives', 2, 'oz')
        r.addIngredient('Jalapeno Pepper', 2, 'seeded and chopped')
        r.addIngredient('Cilantro', 0.5, 'cup, chopped')
        
        r.addIngredient('Extra Virgin Olive Oil', 4, 'tablespoons, aprox')
        r.addIngredient('Garlic', 4, 'cloves (or more), minced')
        r.addIngredient('Onion', 1, 'large, chopped')
        
        r.addIngredient('Corn Tortillas', 16, 'count')

        # Add Steps and Notes
        steps= [
            'preheat oven to 400 deg F with a rack in the middle.',
            'Drain and rinse the Black Beans. Put into a large bowl.',
            'Add to the Bowl 1/2 of the Enchilada Sauce, 1/2 of the Shredded Cheese, Jalapeno, Cilantro and Olives.',
            'Over medium-high heat, fry the Onion and Garlic until translucent in 1 tablespoon of oil. When done, add to the bowl.',
            'Mix all the fillings in the bowl well, and set aside.',
            'Heat a frying pan to medium heat, and place a small amount of oil in it.',
            'Lightly grease two 11x15 baking pans with some of the Oil and set aside.',
            'One or two at a time, fry the Corn Tortillas until just soft. When they are ready, spoon the filling into them, roll and place in the pan.',
            'Repeat until all the filling is used up, and the pans are full ( about 8 Enchiladas per pan).',
            'Pour the remaining Enchilada sauce over the tops of the Enchiladas.',
            'Cover the Enchiladas with the remaining cheese.',
            'Bake in the oven, uncovered, for 20 minutes.',
            'remove and serve!'
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
