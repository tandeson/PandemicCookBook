#!/usr/bin/env python
#*****************************************************************************
"""
    Make A recipe
"""
#*****************************************************************************

#*  Imports ******************************************************************
import sys

from scripts.myRecipe import MyRecipe

#*  Constants ****************************************************************
# PY-2.10
# DELIMITER = ","

#*  Class and Function Definitions *******************************************

#=============================================================================
def makeRecipe( sharedIngredentList ):
        """
        Make this specific Recipe
        """
        r = MyRecipe('Dill Pickles or Veggies', sharedIngredentList)
        
        # Add Ingredients
        r.addIngredient('Distilled Vinegar White')
        r.addIngredient('Tap Water')
        r.addIngredient('Non-Iodized Salt')
        
        # Add Steps and Notes
        
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
