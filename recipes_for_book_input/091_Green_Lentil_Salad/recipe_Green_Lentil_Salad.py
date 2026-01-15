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
        r = MyRecipe('Green Lentil Salad', 'Salads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('GreenLentilSalad', 'IMG_3179.jpeg')
        r.setPrimaryPicture('GreenLentilSalad')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        
        r.addIngredient('Brown Lentils', 1, 'cup, dry')
        r.addIngredient('Red Onion', 0.3, 'cup, chopped, to taste')
        r.addIngredient('Tomatoes', 0.5, 'cup, chopped, to taste')
        r.addIngredient('Parsley', 0.5, 'bunch, chopped, to taste')
        r.addIngredient('Black Olives', 0.3, 'cup, sliced')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Smoked Paprika', 1, 'pinch, to taste')
        r.addIngredient('Cumin', 1, 'pinch, to taste')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons, to taste')
        r.addIngredient('Apple Cider Vinegar', 2, 'tablespoons, to taste')
        
        # Add Steps and Notes
        steps= [
            'Boil the lentils in water until soft, but not mushy - about 20 minutes. Drain, and let cool.',
            'Mix the remaining ingredients into the lentils and stir well. Adjust seasoning to taste.'
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
