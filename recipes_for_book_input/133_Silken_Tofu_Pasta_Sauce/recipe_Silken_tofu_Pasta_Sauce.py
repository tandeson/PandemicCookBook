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
        r = MyRecipe('Silken Tofu Pasta Sauce','Spreads and Dips', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --
        
        ## 
        r.addIngredient('Tofu', 1, 'block, silken')
        r.addIngredient('Onion', 1, 'medium, thin sliced')
        r.addIngredient('Garlic', 6, 'cloves, diced')
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoons')
        r.addIngredient('Nutritional Yeast', 1, 'tablespoon')
        r.addIngredient('Lemon Juice', 1, 'tablespoon')
        r.addIngredient('Water', 1.5, 'from pasta')
        r.addIngredient('Salt', 1, 'teaspoon, to taste')
        r.addIngredient('Black Pepper', 0.5, 'teaspoon, to taste')
        
        
        
        # Add Steps and Notes
        steps = [
            'Peel and dice an onion and mince the cloves of garlic. Then saute them over low heat in olive oil '
            'with a sprinkle of salt until they turn translucent.',
            
            'Open the package of silken tofu and drain off any excess water then add the tofu to the blender. Then '
            'add the sauteed onion and garlic, nutritional yeast, lemon juice, salt, and pepper.',
            
            'Add 1 cup of the starchy pasta water to the blender and blend until smooth. Add an additional 1/2 cup '
            'of the pasta water and blend again until very smooth.',
            
            'Pour the tofu cream sauce back into the frying pan used to saute the onions and warm it over low heat. '
            'Add salt and pepper to taste.'
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
