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
        r = MyRecipe('Avocado Tahini Sauce', 'Spreads and Dips', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Sauce','Avocado_Tahini_2021.jpeg')
        r.setPrimaryPicture('Sauce')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --
        
        r.AddDescription(
            "We added this to a grain bowl with farro and roasted vegitabled and enjoyed"
            " it- but it can go on a number of different dishes ~ Bilyana")
        
        ##
        r.addIngredient('Avocados', 1, 'chopped')
        r.addIngredient('Lime', 1, 'juiced')
        r.addIngredient('Tahini', 2 ,'tablespoons')
        r.addIngredient('Garlic', 6, 'cloves, finely diced')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Cilantro', 0.5, 'bunch')
        r.addIngredient('Basil', 1, 'cup, chopped to taste')
        r.addIngredient('Water', 0.5, 'cup, to taste')
        
        # Add Steps and Notes
        steps = [
            'Put all ingredients in a blender and blend until smooth. Adjust seasoning to taste.'
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
