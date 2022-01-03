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
        r = MyRecipe('Calzone', 'Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('CalzoneDone', '2020_02_02_CalzoneBake.jpeg')
        r.setPrimaryPicture('CalzoneDone')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')

        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Pizza Dough', 16 , 'oz')
        r.addIngredient('Pizza Sauce', 7, 'oz')
        r.addIngredient('Shredded Mexican Cheese', 1.5, 'cups')               
        r.addIngredient('Black Olives', 2, 'oz')
        r.addIngredient('Mushrooms', 2, 'oz')
        r.addIngredient('Capers', 2, 'oz') 
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Eggs', 1, 'large, optional, for wash')
        
              
        # Add Steps and Notes
        steps = [
            'Cut dough into 6 equal parts. Flatten into a square. Cover with a thin layer of sauce, then put on toppings.',
            'Fold the dough over, making a pocket. Ensure that the seams are tight.',
            'Place on a baking sheet with parchment paper, and cover with plastic wrap or a damp towel. Let rise for 45 - 60 min.',
            'Near the end of the rise preheat the oven to 450 deg F.',
            'Slash the tops (or poke with a fork). If desired, cover with an egg wash.',
            'Bake for 15 minutes at 450 deg F, then turn down to 400 deg F. Bake for another 15 minutes or until crust is golden brown.',
            'Remove and let cool on a rack for 10 - 15 minutes. Then serve.'
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
