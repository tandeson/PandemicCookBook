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
        r = MyRecipe('Sweet Potato Pancakes', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Pancakes','2021_Feb_SweetPotatoPancakes.jpg')
        r.setPrimaryPicture('Pancakes')
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')    
        #  -- Add Ingredients --
        
        r.addIngredient('Sweet Potatoes', 3, 'cups, grated')
        r.addIngredient('Carrot', 1, 'cup, grated')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Green Onion', 3, 'tablespoons, chopped')
        r.addIngredient('Black Pepper', 0.25, 'teaspoon')
        r.addIngredient('Fish Sauce', 2, 'teaspoons')
        r.addIngredient('Corn Starch', 1, 'tablespoon')
        r.addIngredient('All Purpose Flour', 3, 'tablespoons')
        r.addIngredient('Eggs', 1, 'large')
        r.addIngredient('Vegetable Oil', 0.3, 'cups')
        
                
        # Add Steps and Notes
        steps = [
            'In a large bowl, combine the grated sweet potato, carrot, and salt. Massage with both hands until wet and squishy, about 1 minute.',
            'Transfer the grated veggies to a piece of muslin or a non-terry dish '
            'towel, and wrap the veggies in the towel. Standing over the sink, firmly squeeze and twist to expel moisture. '
            'Dump the veggies into a dry bowl. Add the green onion, mixing with a fork to distribute well. Mix in the pepper, fish sauce, cornstarch, and all purpose flour. Add the egg, break it up with a fork, and mix well.',
            'Warm a large nonstick skillet over medium heat, then add about 2 tablespoons of oil to film the bottom. Fry in '
            'two batches, 4 pancakes at a time.',
            'For each one, use a fork and your fingers to scoop up the 1/4 cup portions of the potato-and-carrot mixture. '
            'Deposit into the skillet, spreading and flattening the mixture with the measuring cup bottom and fork to make a 3 1/2-inch-wide pancake.',
            'Fry for about 3 minutes, until bits of the fringe-like edges are richly brown and crisp. Flip and fry for about 3 minutes longer, until crisp and brown underneath. Repeat with the rest of the mix.'
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
