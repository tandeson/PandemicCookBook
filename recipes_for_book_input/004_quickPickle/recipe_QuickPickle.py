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
def makeRecipe( sharedIngredentList ):
        """
        Make this specific Recipe
        """
        r = MyRecipe('Red Onion Quick Pickle', sharedIngredentList)
        r.addPicture('PickleOnionPeas', '2020_09_09_QuickPickleBlackEyedPeasGreekYougert.jpg')
        r.addPicture('PickleOnionToast', '2020_09_09_QuickPickleOnToastEgg.jpg')
        r.setPrimaryPicture( 'PickleOnionToast')
        
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Apple Cider Vinegar', 0.5, 'cups')
        r.addIngredient('Distilled White Vinegar', 0.5, 'cups')
        r.addIngredient('Salt', 1, 'teaspoon')
        
        ## Can be white, brown, coconut 1/4 - 1/2 tsp
        r.addIngredient('Sugar', 0.25, 'teaspoon')
        
        r.addIngredient('Red Onion', 1, 'large, thinly sliced')
           
        # Add Steps and Notes
        steps = [
            'Place Apple Cider Vinegar, Distilled White Vinegar, Salt and Sugar into a '
            'tupperware container. Close the lid and shake until Salt and Sugar are dissolved.',
            'Place the sliced Onion into the tupperware. Be sure all the Onions are covered '
            'by the liquid.',
            'Put the lid back on, give a tupperware another shake, and place in the refrigerator.',
            'Wait at least 2 hours, and then serve!'
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
