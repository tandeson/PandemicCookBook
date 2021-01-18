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
        r = MyRecipe('Corn Bread', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        ## ---
        r.addIngredient('All Purpose Flour', 206, 'grams (1 3/4 cup)')
        r.addIngredient('Cornmeal', 156, 'grams (1 cup)')
        r.addIngredient('Sugar', 50, 'grams (1/4 cup)')
        r.addIngredient('Baking Powder', 2, 'teaspoons')
        r.addIngredient('Baking Soda',0.25, 'teaspoon')
        r.addIngredient('Salt', 0.5, 'teaspoon, to taste')
        r.addIngredient('Whole Milk', 283, 'grams (1 1/4 cup), warm')
        r.addIngredient('Unsalted Butter', 57, 'grams, 4 tablespoons')
        r.addIngredient('Extra Virgin Olive Oil', 50, 'grams (1/4 cup)')
        r.addIngredient('Eggs', 1, 'large')
        
        # Add Steps and Notes
        steps = [
            'Preheat the oven to 375 deg F',
            'Lightly grease a 9" square or round pan (a cast-iron skillet will work fine, too), shallow 1 1/2 quart casserole dish, or 12 muffin cups.',
            'In a medium bowl, whisk together the flour, cornmeal, sugar, baking powder, baking soda, and salt',
            'In another bowl or large measuring cup, whisk together the milk, melted butter, vegetable oil, and egg.',
            'Pour the liquid all at once into the flour mixture, stirring quickly and gently until just combined. Don\t over '
            'mix: stir the batter just enough to bring it together and evenly moisten the ingredients.',
            'Spread the batter into the prepared pan, or scoop into the muffin tin.',
            'Bake the bread for 20 to 25 minutes, until the edges just begin to pull away from the pan and a cake tester or paring knife inserted in the center comes out clean.',
            'Remove the bread from the oven and cool it on a rack for 5 minutes before cutting; serve warm.',
            
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
