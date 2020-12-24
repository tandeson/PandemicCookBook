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
        r = MyRecipe('Fried Rice', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        
        #  -- Add Ingredients --
        r.AddDescription(
            'This is typically a way for me to use up vegitable before '
            'they go bad, so the kind of vegitable listed here is more of a suggestion. ~Thomas')
        
        ## Makes about 2 dozen?
        #--
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        
        r.addIngredient('Mushrooms', 0.5, 'cups, about 1/2 a box, chopped')
        r.addIngredient('Broccoli', 1, 'cup, about 1 head chopped')
        r.addIngredient('Onion', 1 , 'cup, chopped')
        r.addIngredient('Carrot', 1, 'cup, chopped')
        r.addIngredient('Garlic', 3, 'cloves, diced')
        r.addIngredient('Ginger', 1, 'tablespoon, diced, fresh')
        
        r.addIngredient('Eggs', 2, 'large, beaten')
        
        r.addIngredient('Rice', 2 ,'cups, cooked (preferably leftover)')
        r.addIngredient('Soy Sauce', 0.25, 'cup, to taste')
        r.addIngredient('Sesame Oil', 1, 'tablespoon')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        
        
        # Add Steps and Notes
        steps = [
            'Heat a large frying pan or caste iron pan on medium-high heat.',
            'Stir fry the veggies (in this case Mushrooms, Broccoli, Onion and Carrots) as well as the garlic and ginger.'
            ' You can substitute whatever veggies you have on hand. Fry until just tender, about 4 minutes.',
            'Move the veggies to the side of the pan, and quickly fry the egg in the middle of the pan. Break it up like scrambled egg and mix it in when it\'s done.',
            'Lower the heat to medium.',
            'Add in the Rice and the seasoning - cook for several more minutes stirring often.',
            'Remove from heat and serve.'
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
