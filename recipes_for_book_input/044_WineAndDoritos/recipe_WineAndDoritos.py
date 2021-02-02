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
        r = MyRecipe('Wine and Doritos', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('WineAndChips', 'WineAndDoritoes_2020.jpg')
        r.setPrimaryPicture('WineAndChips')
        
        r.AddDescription(
            'Some nights, we\'re fancy - some nights we make '
            'this for dinner. ~Thomas'
        )
        #  -- Add Ingredients --

        ##
        r.addIngredient('Wine', 0.5, 'Bottle, white or rose')
        r.addIngredient('Doritos', 1, 'bag, preferably Cool Ranch')
        
        # Add Steps and Notes
        steps= [
            'Pour Wine into cups.',
            'Open bag of Doritos.',
            'Enjoy.'
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
