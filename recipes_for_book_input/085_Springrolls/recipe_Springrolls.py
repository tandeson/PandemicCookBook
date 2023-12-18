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
        r = MyRecipe('Spring Rolls', 'Appetizers', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('SpringRolls', '2021_SpringRolls_1.jpeg')
        r.setPrimaryPicture('SpringRolls')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')

        #  -- Add Ingredients --

        ##
        r.addIngredient('Rice Vermicelli Noodles', 2, 'oz')
        r.addIngredient('Sesame Oil', 1, 'teaspoon')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        
        r.addIngredient('Spring roll wrappers', 8, 'sheets')
        r.addIngredient('Fried Tofu', 14, 'oz')
        r.addIngredient('Romaine Lettuce', 1, 'head, chopped')
        r.addIngredient('Green Onion', 3, 'stalks, optional')
        r.addIngredient('Carrot', 0.5 , 'cups, chopped, optional')
        r.addIngredient('Red Bell Pepper', 1, 'sliced, optional')
        r.addIngredient('Basil', 1, 'bunch, optional')
        
        r.addIngredient('Soy Sauce', 1, 'bottle, optional')
        r.addIngredient('Sriracha', 1, 'bottle, optional')
        
        # Add Steps and Notes
        steps = [
            "Bring a pot of water to a boil, and cook the noodles just until al dente - according "
            "to the package. Drain and rinse under cold water, then toss with sesame oil and salt.",
            
            "Prepare the vegetables and place on a plate for easy access. The exact list is up to"
            " you, vegetables listed here are to give you ideas.",
            
            "Put a layer of water on another plate - This will be used to soften the wraps.",
            
            "Finally - have a place to store the completed wraps.",
            
            "To assemble, take a wrap and dip it in the water on the plate - about 5 to 10 seconds on each side."
            "Move it out of the water, and put down the Tofu, Lettuce, Noodles - and vegetables of your choice.",
            
            "To wrap - fold the lower edge up over the fillings, rolling upward just until the filling is "
            "compactly enclosed. Fold over the short sides like you would a burrito. Roll it up, and you're done!",
            
            "Flavor with Soy Sauce and Sriracha - and Enjoy."
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
