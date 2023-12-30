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
        r = MyRecipe('Banana Bites', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('banana_bites', '2021_12_Banana_Bites_1.jpg')
        r.setPrimaryPicture( 'banana_bites' )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Banana', 1, 'ripe ')
        r.addIngredient('Oatmeal', 0.5, 'cup, rolled')
        r.addIngredient('Walnuts', 0.25, 'cup, pieces')
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 350 deg F',
            'In a bowl mix all ingredients.',
            'Fill a baking sheet with 1 tablespoon sized scopes of batter.',
            'Bake for 15 minutes.',
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
