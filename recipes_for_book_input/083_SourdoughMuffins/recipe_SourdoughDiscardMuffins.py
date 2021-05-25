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
        r = MyRecipe('Sourdough Muffins','Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('MuffinsStack','MuffinsPile.jpeg')
        r.setPrimaryPicture('MuffinsStack')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        
        ## 
        r.addIngredient('All Purpose Flour', 158, 'grams (1 1/3 cup)')
        r.addIngredient('Cornmeal', 100, 'grams (2/3 cup)')
        r.addIngredient('Salt', 0.75, 'teaspoon')
        r.addIngredient('Baking Soda', 1, 'teaspoon')
        r.addIngredient('Cinnamon', 1.5, 'teaspoons')
        
        r.addIngredient('Sourdough Starter', 227, 'grams (1 cup)')
        r.addIngredient('Whole Milk', 57, 'grams (1/4 cup)')
        r.addIngredient('Eggs', 1, 'large')
        r.addIngredient('Unsalted Butter', 57, 'grams, 4 tablespoons, melted')
        r.addIngredient('Maple Syrup', 156, 'grams, 1/2 cup')
        r.addIngredient('Blueberries', 340, 'grams, 2 cups')

        # Add Steps and Notes
        steps = [
            'Preheat oven to 425 deg F. Grease a 12-cup muffin pan.',
            'Combine the dry ingredients in a mixing bowl.',
            'In a second bowl, beat together the starter, milk, egg, melted butter,'
            ' and sweetener. Blend the wet ingredients with the dry, taking about 20 '
            'seconds. Gently stir in the blueberries just until blended',
            'Fill the pan cups evenly with the batter.',
            'Bake the muffins for 25 minutes, until a toothpick inserted in the center'
            ' comes out clean. Remove the pan from the oven and allow the muffins to'
            ' cool for 5 minutes before removing them from the pan.'
            
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
