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
        r = MyRecipe('Guacamole','Spreads and Dips', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('GuacOnSweetPotatoNachos', '2020_09_14_NachosWithGuac.JPG')
        r.setPrimaryPicture('GuacOnSweetPotatoNachos')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Avocados', 3 , 'Haas, halved, seeded and peeled')
        r.addIngredient('Lime', 1, 'medium, juiced')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Cumin', 0.5, 'teaspoon')
        r.addIngredient('Cayenne Pepper', 0.5, 'teaspoon')
        r.addIngredient('Chili powder', 0.5, 'teaspoon')
        r.addIngredient('Red Onion', 1, 'medium, diced')
        r.addIngredient('Jalapeno Pepper', 0.5, 'seeded and minced')
        r.addIngredient('Roma Tomato', 2, 'seeded and diced')
        r.addIngredient('Cilantro', 0.25, 'bunch, chopped')
        r.addIngredient('Garlic', 3, 'cloves, minced')
        
        # Add Steps and Notes
        steps = [
            'Place the Avocadoes in a bowl, mix with the Lime and mash into a chunky paste.',
            'Add in the Salt, Cumin, Cayenne, Chili Powder and mix.',
            'Add in the Red Onion, Jalapeno, Tomatos, Cilantro and Garlic, again - mix well.'
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
