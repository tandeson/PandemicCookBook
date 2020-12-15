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
        r = MyRecipe('Indian Red Lentils', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        
        #  -- Add Ingredients --
        
        ## Makes about 2 dozen?
        #--
        
        r.addIngredient('Red Lentils', 1, 'cup, dry')
        r.addIngredient('Water', 2, 'cups')
        r.addIngredient('Onion', 1, 'chopped')
        r.addIngredient('Tomatoes', 1, 'chopped')
        r.addIngredient('Coconut Milk', 1, 'Can, about 16 oz')
        r.addIngredient('Green Chillies', 2, 'chopped')
        r.addIngredient('Turmeric', 0.25, 'teaspoon')
        r.addIngredient('Cumin', 0.5, 'teaspoon')
        r.addIngredient('Coriander Powder', 0.5, 'teaspoon')
        
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Black Mustard Seeds', 0.5, 'teaspoon')
        r.addIngredient('Cumin Seeds', 1, 'teaspoon')
        r.addIngredient('Curry Leaves', 10, 'optional')
        
        r.addIngredient('Salt', 1, 'pinch, to taste')
        
        #- 2 green chillies, chopped ( or red chilli powder - to taste )
        
        # Add Steps and Notes
        steps = [
            'In a pan, put in the lentils, water, onion, Tomato, Coconut milk, chillies, turmeric, cumin and coriander. If you do not have the Chillies, you can use Chilli powder to taste.',
            'Bring to a boil, then lower to a simmer. Cook, stirring occasionally, about 25 minutes, until lentils are soft.',
            'In a separate small pan, heat oil over low heat and add in cumin seeds and mustard seeds. Cook until they pop. If using curry leaves, add and fry for about 1 minute.',
            'pour everything into the lentils, stir together. Cook for a few minutes'
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
