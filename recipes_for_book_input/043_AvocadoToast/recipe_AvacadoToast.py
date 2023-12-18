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
        r = MyRecipe('Avocado Toast', 'Appetizers', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('ToastOnAPlate', '2020_10_25_ToastAndAvocado.jpg')
        r.setPrimaryPicture('ToastOnAPlate')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        r.AddDescription(
            'While not a complex recipe, this is almost a daily breakfast for Bilyana.'
        )
        #  -- Add Ingredients --

        ##
        r.addIngredient('Avocados', 0.5, 'Haas, skin removed,')
        r.addIngredient('Bread', 1, 'slice')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        
        # Add Steps and Notes
        steps= [
            'If the Bread if fresh, use as is. If not, lightly toast.',
            'Cut the 1/2 an Avocado into 4 roughly equal pieces. Place on a plate next to the Bread.',
            'Lightly salt the Avocado to taste.'
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
