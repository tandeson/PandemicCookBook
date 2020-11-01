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
        r = MyRecipe('Potato Salad', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        #  -- Add Ingredients --

        ##
        r.addIngredient('Potato', 2, 'pounds, whole, waxy')
        r.addIngredient('Eggs', 3, 'medium')
        
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Pickles', 4, 'large, whole')
        r.addIngredient('Celery', 4, 'ribs, chopped')
        r.addIngredient('Red Onion', 0.5, 'medium, chopped')
        
        r.addIngredient('Mayonnaise', 1.5, 'cups')
        r.addIngredient('Apple Cider Vinegar', 3, 'tablespoons')
        r.addIngredient('Mustard', 1, 'tablespoon')
        r.addIngredient('Dill', 0.5, 'tablespoon')
        r.addIngredient('Salt', 2, 'teaspoons')
        r.addIngredient('Black Pepper', 1, 'teaspoons')
                        
        r.addIngredient('Black Olives', 1, 'can, 2.25 oz')
        r.addIngredient('Capers', 1, 'can, 3.5 oz')
        
       
         
        # Add Steps and Notes
        steps= [
            'Fill a large pot about 1/3 of the way with water, add Salt and bring to a Boil.',
            'Add the Potatoes to the pot, reduce heat to just below a boil. Let cook for 8 minutes.',
            'Add in the Eggs to the pot with the Potatoes, let cook for 12 more minutes.',
            'Heat a frying pan on medium heat.',
            'Chop the Pickles, Celery and Onion. Fry in the pan with oil until just softened 3 - 5 minutes.',
            'Put the cooked Pickles, Celery and Onion into a large bowl.',
            'in a separate container mix the Mayonnaise, Vinegar, Mustard, Dill, Salt and Pepper.',
            'When the potatos are done - Turn the stove off.',
            'Working with groups of 2 - 4, remote the Potatos from the pot, slice into large chunks '
            'and place in the bowl. Pour part of the dressing mixture on them, and stir to coat. '
            'Repeat until all the potates are in the bowl.',
            'Shell the hard boiled Eggs, chop, and place in the bowl.',
            'Mix in the Olive, Capers and any remaining dressing. Mix well.'
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
