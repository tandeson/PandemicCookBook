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
        r = MyRecipe('Fried Brussel Sprouts and Onions', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        #  -- Add Ingredients --

        ##
        r.addIngredient('Brussel Sprouts', 1, 'pound')
        r.addIngredient('Yellow Onion', 1 ,'medium, chopped')
        r.addIngredient('Garlic', 4, 'Cloves, minced')
        r.addIngredient('Extra Virgin Olive Oil', 4, 'tablespoons')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')

        
        # Add Steps and Notes
        steps= [
            'Cut the Brussel Sprout into 1/2 or 1/4 pieces, so they are all about the same size. Discard any exterior leaves that look bad.',
            'Heat a cast Iron Frying pan on medium-high heat.',
            'When the pan is hot, add the Oil, Onion and Brussel Sprouts. Cook undisturbed until the Brussel Sprouts turn a lighter green, with one side browned, 5-7 minutes.',
            'Add in the Garlic, Salt and Pepper. Cook until the Garlic is lightly browned.',
            'Remote from heat, serve hot.'
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
