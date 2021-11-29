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
        r = MyRecipe('Roasted Garlic Miso Soup', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Roasted Garlic', 2, 'heads')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Vegetable Broth', 6, 'cups')
        r.addIngredient('Miso Paste', 4, 'tablespoons, to taste')
        r.addIngredient('Tofu', 1, 'block, firm, drained, cubed')
        r.addIngredient('Kale', 1, 'bunch, chopped (about 4 cups)')
        r.addIngredient('Green Onion', 0.5, 'bunch, sliced, optional')
        r.addIngredient('Lemon', 1, 'juiced, optional')
                                
        # Add Steps and Notes
        steps= [
            'In a large pot squeeze garlic bulbs into the pan and mush together and add liquids.',
            'Turn heat to medium-low.',
            'Add Miso and stir to incorporate. Add Tofu',
            'Add Kale, and let wilt for about 5 - 10 minutes.',
            'Serve! (add optional Green Onion and/or Lemon at this point.)'
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
