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
        
        ## From First for women magaizin, 2020-11-30
        
        r = MyRecipe('Italian Cabbage', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        r.addPicture('ItalianCabbageWithBeans', 'IMG_3736.jpeg')
        r.setPrimaryPicture('ItalianCabbageWithBeans')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Extra Virgin Olive Oil', 5, 'tablespoons, to taste')
        r.addIngredient('Onion', 1, 'large, thinly sliced')
        r.addIngredient('Sea Salt', 1, 'pinch to taste')
        r.addIngredient('Red Pepper Flakes', 1, 'pinch, to taste')
        r.addIngredient('Fennel Seeds', 1.5, 'tablespoons')
        r.addIngredient('Smoked Paprika', 2, 'teaspoons')
        r.addIngredient('Tomato Paste', 1.5, 'tablespoons')
        r.addIngredient('Shredded Cabbage', 0.5, 'head, green')
        r.addIngredient('Liquid Smoke' , 1, 'teaspoon')
        r.addIngredient('Black Pepper', 1, 'pinch to taste')
        r.addIngredient('Canellini Beans', 15, 'oz, can')
        
        
        # Add Steps and Notes
        steps= [
            'Preheat a large heavy bottom skillet over medium heat and add 2-3 tablespoons of olive oil.',
            
            'Add the sliced onions and a pinch of sea salt. As the onion starts to soften and release its water '
            'content turn up the heat so the liquid evaporates and the onion starts to get some color.',
            
            'Pan fry the onions until nicely golden with crispy edges. Stir in the chili flakes if using. Add 1 '
            'tablespoon of the fennel seeds and toast with the onion until fragrant.',
            
            'Stir in the smoked paprika and tomato paste and cook for a few minutes until the sugars begin to caramelize.',
            
            'Add the shredded cabbage, season with a pinch of salt and black pepper then mix everything well, scraping any '
            'brown bits from the bottom.',
            
            'Stir in the liquid smoke if using and cook down the cabbage until wilted and softened and the sugars start to '
            'caramelize again on the bottom. You want little golden bits only so be careful not to burn it.',
            
            'Push the mixture to the side and add remaining olive oil to toast the remaining fennel seeds and infuse '
            'a new layer of flavor into your dish.',
            
            'Stir in the cannellini beans and black pepper. Toss to coat well. Cook only until warmed through. Adjust '
            'seasonings and serve.'
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
