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
        r = MyRecipe('Artichoke Rolls', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BakedRolls', 'Pinwheels_Pizza_r.jpg')
        r.setPrimaryPicture('BakedRolls')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Pizza Dough', 16, 'oz')
        r.addIngredient('Artichoke Hearts', 1, 'can, 14oz, in brine')
        r.addIngredient('Parmesan Cheese', 4, 'oz')
        r.addIngredient('Mayonnaise', 1, 'tablespoon')
        r.addIngredient('Cream Cheese', 1, 'tablespoon')
        
        # Add Steps and Notes
        steps= [
            'Roll the Pizza Dough out into a large rectangle.',
            'Rinse and chop the Artichoke Hearts, then place in a bowl.',
            'Add to the bowl the Cheese and Mayonnaise. Mix well.',
            'Spread the mixture thinly over the Pizza Dough, and then roll into a spiral.',
            'Preheat the oven to 400 deg F.',
            'Prepare a baking sheet with parchment paper.',
            'Use floss to cut ends off the roll - about 1/2 " - and place on a baking sheet.',
            'Bake for 25 - 30 minutes, until brown.'
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
