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
        r = MyRecipe('Kimchi Tofu Scramble', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('scramble_1', 'scramble_1.JPEG')
        r.addPicture('scramble_2', 'scramble_2.JPEG')
        r.setPrimaryPicture( 'scramble_1')
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Sesame Oil', 1, 'tablespoon')
        r.addIngredient('Tofu', 1, 'block, extra-firm')
        r.addIngredient('Soy Sauce', 2, 'tablespoons')
        r.addIngredient('Garlic Powder', 0.5, 'teaspoon')
        r.addIngredient('Kale', 1, 'bunch, 4-5 leaves')
        r.addIngredient('Onion', 0.5, 'medium, sliced')
        r.addIngredient('Nutritional Yeast', 2, 'tablespoons')
        r.addIngredient('Kimchi', 1, 'cup')
        r.addIngredient('Sesame seeds', 3, 'tablespoons')
        
        ## Steps
        steps = [
            'Open and drain tofu.',
            'In a large skillet, heat oil over medium-high heat.',
            'Add tofu, crumbling between your fingers, cook, stirring occasionally for 2-3 minutes.',
            'Turn heat to medium, add soy sauce and garlic powder and stir.',
            'Add kale and onions. Cook, stirring occasionally until kale becomes soft and wilts. Cover partially to help with the process, about 5-7 minutes.',
            'Add nutritional yest and Kimchi and mix. Cover in Sesame seeds.'
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
