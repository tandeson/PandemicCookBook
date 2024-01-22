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
        r = MyRecipe('Tofu Feta', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('TofuFeta', 'TofuFeta_1.jpg')
        r.setPrimaryPicture('TofuFeta')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        r.AddDescription("Keep the marinade remaining after the tofu is "
                         "consumed - it can be delicious on its own as an"
                         " addition to a salad")
        ## ---
        
        r.addIngredient('Tofu', 1, 'block, extra-firm')
        r.addIngredient('Lemon Juice', 0.25, 'cup')
        r.addIngredient('Apple Cider Vinegar', 0.25, 'cup')
        r.addIngredient('Nutritional Yeast', 2, 'tablespoons')
        r.addIngredient('Miso Paste', 1, 'tablespoon')
        r.addIngredient('Basil', 1, 'teaspoon, dried')
        r.addIngredient('Oregano', 1, 'teaspoon')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        
        ## Steps
        steps = [
            'Mix everything except the tofu in a large tupperware container.',
            'Cub the Tofu and place it in the tupperware, mix gently.',
            'Refrigerate for at least 1 hour or up to a few days - then serve.'
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
