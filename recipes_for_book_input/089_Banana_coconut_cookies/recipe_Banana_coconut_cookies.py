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
        r = MyRecipe('Banana Coconut Cookies', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        r.AddDescription('I had my doubts about this recipe, but it turned out delicious. ~ Bilyana')  
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Coconut Flakes', 1, 'cup, to taste')
        r.addIngredient('Banana', 2, 'mashed ')
        r.addIngredient('Dark Chocolate chips', 0.25, 'cup, melted (Optional)')
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 350 deg F',
            'In a bowl mix the Bananna and Coconut Flakes.',
            'Fill a baking sheeting sheet with 1 tablespoon sized scopes of batter.',
            'Bake for 20 minutes.',
            'Once cooled, drizzle with melted chocolate if using.'
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
