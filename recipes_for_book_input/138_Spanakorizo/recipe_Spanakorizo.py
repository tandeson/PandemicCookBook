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

#*  Class and Function Definitions *******************************************

#=============================================================================
def makeRecipe( dirPathRecipe, sharedIngredentList ):
        """
        Make this specific Recipe
        """
        r = MyRecipe('Spanakorizo (Greek Spinach Rice)', 'Main dishes', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        #  -- Add Ingredients --

        r.addIngredient('Extra Virgin Olive Oil', 0.25, 'cup, plus more for serving')
        r.addIngredient('Onion', 1, 'medium, peeled and diced')
        r.addIngredient('Green Onion', 4, 'stalks, sliced')
        r.addIngredient('Garlic', 2, 'cloves, minced')
        r.addIngredient('Arborio Rice', 1, 'cup')
        r.addIngredient('Spinach', 1, 'lb, fresh baby spinach, roughly chopped')
        r.addIngredient('Dill', 0.25, 'cup, fresh, chopped')
        r.addIngredient('Parsley', 2, 'tablespoons, fresh, chopped (optional)')
        r.addIngredient('Vegetable Broth', 4, 'cups, warmed (chicken broth also works)')
        r.addIngredient('Salt', 0.5, 'tsp')
        r.addIngredient('Black Pepper', 0.25, 'tsp')
        r.addIngredient('Lemon', 1, 'small, zested and juiced')

        # Add Steps and Notes
        steps = [
            "Heat olive oil in a wide saucepan over medium heat."
            " Saute onion, green onions, and garlic for 3-4 minutes until softened.",

            "Add rice and saute for 2-3 minutes, stirring with a wooden spoon, until translucent.",

            "Gradually add spinach a handful at a time, stirring for 4-5 minutes until wilted.",

            "Stir in dill, parsley (if using), salt, and pepper.",

            "Add broth, stir well, lower heat, cover, and simmer for 15 minutes until the rice"
            " absorbs the liquid.",

            "Remove from heat and stir in lemon zest and juice. Season to taste.",

            "Serve in bowls with lemon wedges and a drizzle of olive oil.",
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
