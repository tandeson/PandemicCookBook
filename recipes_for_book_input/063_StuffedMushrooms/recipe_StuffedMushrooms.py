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
        
        r = MyRecipe('Blue cheese and Walnut Stuffed Mushrooms', 'Appetizers', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Mushrooms', 'StuffedMushrooms_Nov2020.jpg')
        r.setPrimaryPicture('Mushrooms')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --

        ##
        r.addIngredient('Mushrooms', 16, 'individual, about 1 pound')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Blue Cheese', 3, 'oz')
        r.addIngredient('Walnuts', 0.3, 'cups, chopped')
        r.addIngredient('Breadcrumbs', 0.25, 'cups')
        r.addIngredient('Thyme', 1, 'teaspoon, chopped')
        r.addIngredient('Black Pepper', 0.25, 'teaspoon, to taste')
                              
        # Add Steps and Notes
        steps= [
            'Heat oven to 375 deg F.',
            'Coat baking sheet with parchment paper.',
            'Brush mushrooms with oil, arrange, stem sides down, on baking sheet.',
            'Bake until almost tender, 10 minues.',
            'In a bowl, combine remaining ingredients.',
            'Flip mushrooms over. Fill evenly with cheese mixture.',
            'Heat broiler, broil until cheese melts, 1-2 minutes.'
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
