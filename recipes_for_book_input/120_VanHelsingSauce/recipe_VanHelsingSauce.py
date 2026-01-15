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
        r = MyRecipe('Van Helsing Sauce','Spreads and Dips', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('SauceOnSpoon', 'sauce_on_spoon.jpeg.jpeg')
        r.setPrimaryPicture('SauceOnSpoon')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --
        
        r.AddDescription('Andrew shared this during his visit in 2022. '
                  'It\'s named after a Character in Dracula - due to being able to double as '
                  'a vampire deterrent. ~Thomas')
        ## 
        r.addIngredient('Goat Cheese', 8, 'Oz')
        r.addIngredient('Garlic', 0.5, 'cups raw')
        r.addIngredient('Extra Virgin Olive Oil', 1, 'cup')
        r.addIngredient('Onion', 2, 'medium, thin sliced')
        r.addIngredient('Thyme', 1.5, 'Teaspoons')
        r.addIngredient('Garlic Powder', 1.5, 'Teaspoons')
        r.addIngredient('Salt', 0.5, 'teaspoon, to taste')
        r.addIngredient('White Pepper', 0.5, 'teaspoon, to taste')
        
        
        
        # Add Steps and Notes
        steps = [
            'Cook about 1/4 cup of garlic in the olive oil on medium heat until caramelized. '
            'Put the garlic in a food processor.',
            
            'In a large frying pan, caramelize the onions. Cook on Medium heat with a small amount of salt and oil. '
            'Put in food processor with the garlic.',
            
            'Chop the remaining raw garlic.',
            'Place all the remaining ingredients in a food processor, and blend until smooth. '
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
