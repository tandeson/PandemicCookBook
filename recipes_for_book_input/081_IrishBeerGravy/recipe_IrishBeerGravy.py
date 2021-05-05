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
        r = MyRecipe('Irish Beer Gravy','Spreads and Dips', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Gravy_and_Colcannon', 'Colcannon_and_Gravy.jpeg')
        r.addPicture('BeerGravy','IrishBeerGravy.jpeg')
        r.setPrimaryPicture('Gravy_and_Colcannon')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Mushrooms', 8, 'oz, quartered')
        r.addIngredient('Red Onion', 0.5, 'medium, chopped fine')
        
        r.addIngredient('Mustard', 0.5, 'tablespoon, grainy')
        r.addIngredient('Unsalted Butter', 3, 'tablespoons')
        r.addIngredient('All Purpose Flour', 3, 'tablespoons')
        
        r.addIngredient('Beer', 8, 'oz, Guinness, Stout, Brown Ale, etc')
        r.addIngredient('Half and Half', 2, 'tablespoons')
        
        r.addIngredient('Rosemary', 0.5, 'tablespoons')
        r.addIngredient('Worcestershire Sauce', 1, 'tablespoon')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
                
        # Add Steps and Notes
        steps = [
            'In a dry preheated cast iron (or other heavy bottomed) pan over medium '
            'heat add the mushrooms and onions and cook until the mushroom begin '
            'to sweat and the onions begin to brown.',
            
            'Add the mustard, butter and flour. Cook over medium heat stirring constantly '
            'until the flour is completely saturated with the oils.',
            
            'Reduce the heat to medium low and slowly add  about four ounces of the beer, '
            'whisking to combine into a smooth paste (except, of course, for the onions and mushrooms). '
            'Once that is incorporated, continue to add the beer and half and half. Once this is done '
            'add the Rosemary, Worcestershire sauce, Salt and pepper. Heat, stirring frequently, until the '
            'gravy is just bubbly and thickened to your taste.'
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
