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
        r = MyRecipe('Zucchini Curry',  'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('ZucchiniCurryInBowl', '2020_ZuchiniCurry.jpg')
        r.setPrimaryPicture('ZucchiniCurryInBowl')
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')
        
        ## Source: https://www.simplyquinoa.com/detox-moroccan-lentil-soup/
        #  -- Add Ingredients --

        ##
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Red Onion', 1, 'large, diced')
        r.addIngredient('Garlic', 5, 'cloves, diced')
        r.addIngredient('Ginger', 2, 'teaspoons (freshly grated)')
        r.addIngredient('Coriander Powder', 2, 'teaspoons')
        r.addIngredient('Smoked Paprika', 2, 'teaspoons')
        r.addIngredient('Turmeric', 2, 'teaspoons')
        r.addIngredient('Cumin', 1, 'teaspoon')
        r.addIngredient('Zucchini', 3, 'medium' )
        r.addIngredient('Tomato Paste', 1, 'can, 6 oz')
        r.addIngredient('Vegetable Broth', 1, 'cup')
        r.addIngredient('Coconut Milk', 1, 'can, 14 oz full fat')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Cilantro', 0.25, 'cup, for optional garnish')

        
        # Add Steps and Notes
        steps= [
            'Add oil to a pan over medium heat and, when warm, add the diced onions and saute about 7 to 10 minutes,'
            ' stirring to keep the onions from burning.',
            'While the onions are sauteing, dice the zucchini into bite-sized pieces.',
            'Add the ginger, garlic and zucchini to the pan with the sauteed onions and saute about 5 minutes, stirring often.',
            'Add the coriander, cumin, smoked paprika and turmeric and stir so the spices are well incorporated.',
            'Add the tomato paste, vegetable stock and coconut milk and stir until combined. Simmer about 15 minutes.',
            'Season with salt and pepper. If you\'d like it a bit spicy, add a teaspoon of chili powder and mix. Garnish with chopped '
            'cilantro and enjoy with quinoa, naan or rice.'
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
