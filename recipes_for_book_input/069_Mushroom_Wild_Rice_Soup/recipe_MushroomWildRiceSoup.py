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
        r = MyRecipe('Mushroom and Wild Rice Soup', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('MushroomSoup', '2021_MushroomSoup.jpg')
        r.setPrimaryPicture( 'MushroomSoup' )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        r.addIngredient('Wild Rice Blend', 0.75, 'cup')
        r.addIngredient('Mushrooms', 4 ,'cups, diced')
        r.addIngredient('White Onion', 1, 'cup, diced')
        r.addIngredient('Garlic', 2, 'cloves, diced')              
        r.addIngredient('Unsalted Butter', 2, 'tablespoons')
        r.addIngredient('Parsley', 1, 'teaspoon')
        r.addIngredient('Vegetable Broth', 4, 'cups')
        r.addIngredient('Coconut Milk', 1, 'can 14 oz')
        r.addIngredient('Salt', 1, 'Pinch to taste')
        r.addIngredient('Quinoa', 0.5, 'cups')
        r.addIngredient('Black Pepper', 1, 'Pinch to taste')                

        # Add Steps and Notes
        steps = [
            'First, rinse the wild rice and add it to a small or bowl to soak in cold water for 15-30 minutes.',
            'While the rice is soaking, chop & prep the vegetables. Slice the mushrooms thinly (removing the bottom'
            ' of the stems if desired) and  finely dice the onions.',
            'Next, add the butter to a large soup pot and turn on the heat. Once the butter has melted, add in '
            'the onion, garlic, and mushrooms. Then, saute for 15 minutes until the onions & mushrooms are beginning to'
            ' crisp up and brown. Make sure to stir consistently to evenly cook the vegetables.',
            'Once the vegetables are cooked, season with a mix of parsley, salt, and pepper. Then, add the vegetable broth, '
            'soaked & strained wild rice, and coconut milk to the pot with the vegetables. Stir to mix together.',
            'Bring the pot of soup to a boil. Then, reduce the heat to a simmer and cook covered for 35-40  minutes.',
            'Add Quinoa, stir, then turn off heat and let sit for 15 minutes to cook with the lid on.',
            'Remove the soup from the heat and let it sit for 5 minutes to thicken. Finally, serve and enjoy!'
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
