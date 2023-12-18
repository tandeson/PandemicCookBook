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
        r = MyRecipe('Kimchi Soup', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('kimchiSoup_1', 'IMG_3243.jpeg')
        r.setPrimaryPicture('kimchiSoup_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Tofu', 1, 'block, firm, drained, cubed')
        r.addIngredient('Water', 3, 'cups')
        r.addIngredient('Mushrooms', 3, 'cups, Dried Shiitaki Mushrooms')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Onion', 1, 'chopped')
        r.addIngredient('Garlic', 5, 'cloves, chopped')
        r.addIngredient('Green Onion', 1, 'bunch, chopped')
        r.addIngredient('Gochujang Paste', 1, 'tablespoon')
        r.addIngredient('Kimchi', 0.5, 'jar')
        r.addIngredient('Bonito', 1, 'tablespoon')
        r.addIngredient('Soy Sauce', 2, 'tablespoons to taste')
        r.addIngredient('Sesame Oil', 1, 'tablespoons')
                        
        # Add Steps and Notes
        steps= [
            'Drain and chop Tofu into roughly 1/2 inch cubes',
            'Bring water to a boil - about 3 cups - and cover and soak the mushrooms.'
            ' Need to soak at least 30 min - keep water when done for broth.',
            'Once rehydrated, slice the mushrooms into halves.',
            'In 1 - 2 tablespoons of olive oil, saute the white onion for a few minutes.'
            ' Then add garlic and green onion and cook for a few minutes. Then add the mushrooms - saute for a minute.',
            'Add the Gochujang and Kimchi, stir well.', 
            "Add the water from the mushrooms, Tofu, Bonito, Soy Sauce, sesame oil. Add water to cover everything if there isn't enough.",
            "Bring to a boil - cover, lower the heat to simmer, and simmer for 20 minutes."
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
