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
        r = MyRecipe('Rice and Saurkraut Bake', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture( 'PlateRiceSourkraut', 'RiceAndSourkraut.jpg')
        r.setPrimaryPicture( 'PlateRiceSourkraut')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Sauerkraut', 1, '2 pound jar')
        r.addIngredient('Rice', 0.75, 'cup, rice') 
        r.addIngredient('Water', 2.5, 'cups')
        r.addIngredient('Extra Virgin Olive Oil', 0.3, 'cup')
        r.addIngredient('Smoked Paprika', 1.5, 'tablespoon')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        
        # Add Steps and Notes
        steps= [
            'Heat the oven to 375 deg F.',
            'Combine all ingredients in a baking pan, and mix.',
            'Bake until cooked - about 90 minutes.'
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
