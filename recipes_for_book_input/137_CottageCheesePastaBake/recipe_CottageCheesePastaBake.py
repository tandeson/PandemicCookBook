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
        r = MyRecipe('Cottage Cheese Pasta Bake', 'Main dishes', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        #  -- Add Ingredients --

        r.addIngredient('Pasta', 3, 'cups, dry (penne or other short shape)')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Garlic', 4, 'cloves, minced')
        r.addIngredient('Broccoli', 2, 'cups, florets (about 142 grams)')
        r.addIngredient('Spinach', 3, 'cups, baby spinach (tightly packed)')
        r.addIngredient('Cottage Cheese', 2, 'cups, 500g / 17 oz container')
        r.addIngredient('Marinara Sauce', 2, 'cups')
        r.addIngredient('Mozzarella', 1, 'cup, shredded')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Basil', 5, 'large fresh leaves, chopped (garnish)')

        # Add Steps and Notes
        steps = [
            "Preheat oven to 400 deg F. Bring a large pot of salted water to a boil."
            " While you wait, chop the broccoli into florets and mince the garlic.",

            "Cook the pasta al dente according to package instructions. Drain and set aside.",

            "Meanwhile, heat the olive oil in a large pan over medium-high heat."
            " Add the minced garlic and broccoli florets and saute for about 7 minutes."
            " Add the spinach and cook until wilted. Remove from heat.",

            "To a large baking dish, add the cooked pasta, sauteed vegetables, cottage cheese,"
            " and marinara sauce. Season generously with salt and pepper, then stir everything"
            " together until well combined.",

            "Sprinkle the shredded mozzarella evenly over the top.",

            "Bake for 20 minutes, or until the cheese is melted and nicely browned."
            " Garnish with fresh basil and serve hot.",
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
