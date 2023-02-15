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
        r = MyRecipe('Creme Brulee', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        
        #  -- Add Ingredients --
        
        ## 
        #--
        r.addIngredient('Eggs Yolks', 5, '')
        r.addIngredient('Granulated White Sugar', 0.6, 'cups, plus extra for topping')
        r.addIngredient('Heavy Cream', 2.5, 'cups')
        r.addIngredient('Vanilla', 2, 'teaspoons')
        r.addIngredient('Salt', 0.25, 'teaspoons')

        # Add Steps and Notes
        steps = [
            'Preheat the oven to 325 deg F.',
            'Put the Egg Yokes and Sugar in a bowl, and wisk until it lightens in color.',
            'Add in the Heavy Cream, Vanilla and salt. For a differet flavor - you can replace 0.5 cups of Heavy Cream '
            'with Irish Cream.',
            'Gently wisk until the mixture is uniform.',
            'Place 5 small ramekins in a larger glass dish. Fill each to about 80% full with the mixture.',
            'Pour hot water from the sink into the dish up to the half way point on the ramekins.',
            'Bake for 45 minutes, until the custard is just set. Leave the ramekins in the water for another 15 minutes, then '
            'let them set in the fridge for at least 4 hours.',
            'When ready to top - sprinkle sugar over the top and then use a kitchen torch to melt. Let sit for 15 minutes befor serving.'
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
