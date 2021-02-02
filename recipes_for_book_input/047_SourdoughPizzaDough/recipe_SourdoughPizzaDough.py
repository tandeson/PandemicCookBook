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
        r = MyRecipe('Sourdough Pizza Dough', 'Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Pizza', 'Pizza_2.jpg')
        r.setPrimaryPicture('Pizza')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Sourdough Starter', 1, 'cup, 227 grams')
        r.addIngredient('Water', 0.5 ,'cup, 113 grams, warm')
        r.addIngredient('Bread Flour', 2.5, 'cups, 298 grams')
        r.addIngredient('Salt', 1, 'teaspoon')
        r.addIngredient('Instant Yeast', 0.5 , 'teaspoon')
        r.addIngredient('Pizza Dough Flavor', 4, 'tablespoons')
        
        # Add Steps and Notes
        r.addStep( RecipeStep( 'Make the dough',
            [
                RecipeStep('Add the water, flour, salt, yeast, and Pizza Dough Flavor (if using). Mix to combine, then knead until the dough wraps '
                           'is smooth and elastic.'),
                RecipeStep('Place the dough in a greased container, cover and let rise until almost doubled in bulk. Depending on the vitality of '
                           'your starter, this will take between 2 and 4 hours. For a faster rise, place the dough in a warm spot, or double the '
                           'yeast.'),
                RecipeStep('If not using immediately, place in the refrigerator for up to 4 days.')
            ]))
            
        r.addStep( RecipeStep( 'To make into Pizza',
            [
                RecipeStep('For two thin-crust pizzas, divide the dough in half, and shape each into a flattened disk. Drizzle two 12" round pizza'
                           ' pans with olive oil, and brush to coat the bottom. Place the dough in the pans, cover, and let rest for 15 minutes. '
                           'After this rest, gently press the dough toward the edges of the pans. If it starts to shrink back, cover and let rest'
                           ' for 15 minutes before continuing.'),
                RecipeStep('For a thicker, large pizza, oil a 14" round pizza pan (an 18" x 13" half-sheet pan will also work). Place the dough in'
                           ' the selected pan and press it out to the edges, again giving it a 15-minute rest before continuing if it starts to '
                           'snap back.'),
                RecipeStep('Cover the pan(s) and let the dough rise until it\'s as thick as you like.'),
                RecipeStep('Towards the end of the rise time, preheat your oven to 450 deg F'),
                RecipeStep('Sauce and top as you like, but don\'t add cheese yet. Bake thin-crust pizzas for 5 minutes before removing from the oven'
                           ' and adding cheese. For thick-crust pizza, bake for 10 minutes before removing from the oven and adding cheese. Return to'
                           ' the oven and bake for 5 to 7 more minutes, until the cheese is melted.')
            ]))
                               
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
