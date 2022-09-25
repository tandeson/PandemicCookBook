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
        r = MyRecipe('Roasted Chickpeas', 'Appetizers', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Chickpeas', 1, 'pound')
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoon')
        r.addIngredient('Cumin', 2, 'teaspoons')
        r.addIngredient('Marjoram', 1, 'teaspoon')
        r.addIngredient('Allspice', 0.25, 'teaspoon')
        r.addIngredient('Salt', 0.25, 'teaspoon')
        
        ## Steps
        steps = [
            'Position rack in upper third of oven; pre-heat to 450 deg F.',
            'Blot chickpeas dry and toss in a bowl with the rest of the ingredients.',
            'Spread on a rimmed baking sheet.',
            'Bake, stirring once or twice, until browned and cruch. 25 to 30 minutes (for large batched, add another 10 minutes).',
            'Let cool on the baking sheet for 15 minutes.'
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
