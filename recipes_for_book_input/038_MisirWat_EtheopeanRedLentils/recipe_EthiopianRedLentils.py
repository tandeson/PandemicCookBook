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
        r = MyRecipe('Ethiopian Red Lentils', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('MixedPlate', 'redLentisMixedPlate.jpg')
        r.setPrimaryPicture('MixedPlate')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Unsalted Butter', 4, 'tablespoons')
        r.addIngredient('Yellow Onion', 1, 'large, diced')
        r.addIngredient('Garlic', 3, 'cloves, minced')
        r.addIngredient('Roma Tomato', 1, 'finely chopped')
        r.addIngredient('Tomato Paste', 3, 'tablespoons')
        r.addIngredient('Berbere', 1, 'tablespoon')
        r.addIngredient('Red Lentils', 1, 'cup')
        r.addIngredient('Vegetable Broth', 2.5, 'cups')
        r.addIngredient('Salt', 1, 'teaspoon')
        
        # Add Steps and Notes
        steps= [
            'Melt 3 tablespoons of the Butter in a medium pot on medium high heat.',
            'Add the Onions and cook for 8-10 minutes until golden brown.',
            'Add the Garlic, Tomatoes, Tomato Paste and 1 tablespoon of Berbere and cook for 5-7 minutes.'
            ' Reduce heat if needed to prevent burning.',
            'Add the Broth and Salt.',
            'Bring to a boil, add the Lentils, reduce the heat to low and cover. Simmer the lentils, stirring occasionally for 20 minutes until soft.',
            'Add Salt to taste.'
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
