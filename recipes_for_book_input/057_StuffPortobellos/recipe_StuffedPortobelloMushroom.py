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
        r = MyRecipe('Stuffed Portobello Mushrooms', 'Main dishes', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --
        
        ##
        #--
        r.addIngredient('Mushrooms', 2, 'large Portobello')
        r.addIngredient('Brie', 0.25, 'cups, approximately')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        
        
        # Add Steps and Notes
        steps = [
            'Pre-heat the oven to 350 deg F.',
            'Lightly grease a baking sheet, or line it with parchment.',
            'Brush the top of the mushroom cap with oil, and place on the sheet stem side up.',
            'Evenly divide the cheese between the mushrooms, and place on top. You can also use Feta, '
            'cream cheese or other cheese as well. If the mushrooms seems dry - add additional oil.',
            'Season to taste with Salt and Pepper.',
            'Bake for 15 minutes.',
            'Remove and serve.'
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
