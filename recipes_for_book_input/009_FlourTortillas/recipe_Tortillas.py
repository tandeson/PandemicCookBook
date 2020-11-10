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
        r = MyRecipe('Flour Tortillas', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        
        r.AddDescription(
            'Rick Rodriguez shared this with me after a conversation at the coffee stand. '
            'He likes to make these in the morning for his wife, and fill them with eggs and '
            'potatoes. They can also come out like a Pita bread by adding a pinch of baking soda. '
            'As Pita they work well, for things like the base of a Gyro. ~Thomas'    
        )
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('All Purpose Flour', 3, 'cups')
        r.addIngredient('Vegetable Oil', 0.3, 'cups')  # 1/3
        r.addIngredient('Salt', 1/2, 'teaspoon')
        r.addIngredient('Water', 1, 'cup, hot (at or near boiling)')
        
        # Add Steps and Notes
        steps = [
            'In a medium-large bowl, mix-in the Flour, Salt and Oil',
            'With a large spoon, stir in the hot Water.',
            'After the water is mixed in and the flour and oil start to cool-off '
            ', mix the ingredients with your hand until you have a big lump of flour dough.',
            'Knead the dough and, if it\'s too "pie crush" like, add a little more hot water; or, '
            'if it\'s too mushy, add a little flour.',
            'Break off little clump of dough and round them between the palms of your hands.'
            ' when you have a nice little ball, flatten it a little between your hands into a '
            '"plump" disk-like shape.',
            'Spread a little flour on a cutting board and over-and-around a rolling pin.',
            'Gently roll out the flour disk into a oblong (elliptical) shape. Pickup up the dough, '
            'fip-it-over and place it 90 degress to your original rolling motion. Repeate this step '
            'over and over until you get a nice, flat, thin raw tortilla.',
            'Place the tortilla on a hot griddle for a few seconds, and then turn it over. You may '
            'want to rotate the tortilla with you hand while it\'s on the griddle so that it '
            'cooks evenly. Flit it over again and cook until done.',
            'If you\'re doing it right, and are lucky, the tortilla will sometimes fill with '
            'hot air and "puff up" on the griddle. If it gets too puffy, you can flatten it.',
            'When done, you should have about a dozen tortillas.'
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
