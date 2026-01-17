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
        r = MyRecipe('Blue Cheese and Onion Rolls','Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BlueCheeseRolls', '2020_08_02_BlueCheeseOnionSwirlRoll.jpeg')
        r.setPrimaryPicture( 'BlueCheeseRolls')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --

        ##
        r.addIngredient('Water', 198, 'grams, (0.75 cup)')
        r.addIngredient('Sourdough Starter', 227, 'grams (1 cup)')
        r.addIngredient('Bread Flour', 361, 'grams (3 cups)')
        r.addIngredient('Bakers Special Dry Milk', 28, 'grams (0.25 cup)')
        r.addIngredient('Sugar', 14, 'grams')
        r.addIngredient('Vegetable Oil', 1, 'tablespoons')
        r.addIngredient('Salt', 1.5, 'teaspoons')
        r.addIngredient('Instant Yeast', 2, 'teaspoons')
        
        r.addIngredient('Blue Cheese', 2, 'oz' )
        r.addIngredient('French\'s Original Crispy Fried Onions', 3, 'oz')
        
        # Add Steps and Notes
        steps = [
            'Line a baking sheet with parchment paper.',
            'Mix and knead the dough ingredients to make a cohesive, fairly smooth dough.'
            'It should be slightly sticky, if it seems dry, knead in an additional '
            'tablespoon or two of water. If working with the dough by hand, slighly greasing '
            'your hands will make this process easier.',
            'Cover the dough and let it rest for 45 minutes. It will rise minimally.',
            'Toward the end of the rising time, preheat the oven to 350 deg F.',
            'Turn the dough out onto a lighly greased work surface. Fold it over a few times '
            'to gently deflate it. Divide into 12 peices, each about 70 grams.',
            'Roll each piece into a rope, and flatten.',
            'Fill the middle of the rope with Blue Cheese and Crispy Fried Onions.',
            'Pinch the rope together to make a tube holding the fillings. Pinch off both ends.',
            'Roll the ropes into a cinnamon roll shape, and place on the baking sheet.',
            'Bake for 25 - 30 minutes, until they\'re a light golden brown.',
            'Remove from the oven and allow to cool.'
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
