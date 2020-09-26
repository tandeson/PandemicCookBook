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
        r.addPicture('picklesDone', '2020_09_09_Pickles_post.jpg')
        r.setPrimaryPicture( 'picklesDone')
        #  -- Add Ingredients --
        
        ## Pickling liquid
        ingGrpName = "Pickling Liquid"
        r.addIngredient('Distilled Vinegar White', 1, 'quart', ingGrpName)
        r.addIngredient('Tap Water', 3, 'quart', ingGrpName)
        r.addIngredient('Non-Iodized Salt', 1, 'cup', ingGrpName)
        
        
        ## Flavoring
        ingGrpName = "For inside the jars"
        r.addIngredient('Garlic', 1, 'clove', ingGrpName)
        r.addIngredient('Grape Leaves', 1, 'leaf', ingGrpName)
        r.addIngredient('Celery seed', 0.25, 'teaspoon', ingGrpName)
        r.addIngredient('Dill', 0.25, 'teaspoon', ingGrpName)
        
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
