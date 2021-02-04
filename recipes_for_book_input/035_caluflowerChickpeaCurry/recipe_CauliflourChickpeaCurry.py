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
        r = MyRecipe('Cauliflower and Chickpea Coconut Curry','Soups',  sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Cauliflower', 1, 'large, cut into chunks')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Red Onion', 0.5, 'medium, diced')
        r.addIngredient('Chili powder', 1, 'tablespoon')
        r.addIngredient('Garlic', 4, 'cloves, minced')
        r.addIngredient('Ginger', 1, 'tablespoon, grated')
        r.addIngredient('Curry Powder', 1 , 'tablespoon')
        r.addIngredient('Diced Tomatoes', 1, 'can, 14 oz')
        r.addIngredient('Agave Nectar', 3, 'teaspoons')
        r.addIngredient('Coconut Milk', 1, 'can, 14 oz')
        r.addIngredient('Chickpeas', 1, 'can, 15 oz')
        r.addIngredient('Lime', 1, 'small, juiced')
        r.addIngredient('Cilantro', 0.3, 'cup, chopped')
        r.addIngredient('Salt', 0.75, 'teaspoon')
        r.addIngredient('Black Pepper', 1, 'pinch')
        
        # Add Steps and Notes
        steps= [
            'Preheat oven to 450 deg F.',
            'Place Cauliflower florets on a rimmed baking sheet. Drizzle with oil and sprinkle with Salt and Pepper.',
            'Combine together, and then roast for 7-10 minutes, toss, and continue roasting for 7-10 minutes longer.'
            ' The Cauliflower should be tender and lightly browned.',
            'In a large pan, heat oil over medium heat.',
            'Add Onions and Salt until translucent about 2-3 minutes.',
            'Add in Chili Powder, Garlic and Ginger. Saute until fragrant, about 30-60 seconds.',
            'Add Diced Tomatoes, Agave and Salt. Cook for 2-3 minutes to soften and meld flavors.',
            'Pour in Coconut Milk and lightly simmer for 3-4 minutes to reduce. Don\'t boil.',
            'Add in Chickpeas and Lime Juice. Gently simmer to warm and soften Chickpeas.',
            'Remove from heat.',
            'Add Roasted Cauliflower and gently toss to combine well.',
            'Adjust seasoning to taste, sprinkle with Cilantro.'
            
            
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
