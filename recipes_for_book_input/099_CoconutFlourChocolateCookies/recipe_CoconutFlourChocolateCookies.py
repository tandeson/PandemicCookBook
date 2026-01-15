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
        r = MyRecipe('Coconut Four Chocolate Chip Cookies', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('CoconutCookies', 'IMG_2889.jpeg')
        r.setPrimaryPicture('CoconutCookies')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS') 
        #  -- Add Ingredients --
        
        ## 
        #--
        r.addIngredient('Coconut Flour', 0.3, 'cups')
        r.addIngredient('Coconut Oil', 0.25, 'cups, melted and cooled')
        r.addIngredient('Maple Syrup', 0.25, 'cups')
        r.addIngredient('Vanilla', 1, 'teaspoon')
        r.addIngredient('Salt', 0.25, 'teaspoon')
        r.addIngredient('Eggs', 2, 'large')
        r.addIngredient('Dark Chocolate chips', 0.3, 'cups')
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 350 deg F.',
            'Line a baking sheet with parchment paper or parchment paper sheets.',
            'In a medium size bowl, combine coconut flour, melted and cooled coconut oil, syrup, eggs vanilla and salt.',
            'Whisk mixture together.',
            'Allow dough to sit five minutes so the dough thickens.',
            'Add the chocolate chips.',
            'Using a tablespoon or cookie scoop, drop 12 cookies onto baking sheet.',
            'Bake 13-14 minutes and remove from oven when the edges begin to turn golden brown.'
            'Cool.'
            ]
        
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        # Notes
        
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
