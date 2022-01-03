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
        r = MyRecipe('Black Eyed Peas', "Main dishes", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('PeasWithOnionBowl', '2020_09_09_QuickPickleBlackEyedPeasGreekYougert.jpg')
        r.setPrimaryPicture( 'PeasWithOnionBowl')
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Black-Eyed Peas', 16, 'oz (1 can)')
        r.addIngredient('Vegetable Oil', 1, 'teaspoon' )
        r.addIngredient('Asafetida', 1, 'pinch (optional)')
        r.addIngredient('Cumin Seeds', 0.25, 'teaspoon')
        r.addIngredient('Turmeric', 0.25, 'teaspoon')
        r.addIngredient('Cayenne Pepper', 0.25, 'teaspoon (optional)')
        r.addIngredient('Coriander Powder', 1, 'teaspoon')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Water', 0.5, 'cup')
        r.addIngredient('Garam Masala', 0.25, 'teaspoon')
        r.addIngredient('Lemon Juice', 1, 'teaspoon')
        
        # Add Steps and Notes
        steps = [
            'In a strainer, drain and rinse the Black-Eyed Peas. Set aside.',
            'In a heavy non-stick skillet, heat the oil over medium heat.',
            'Add the Asafetida and Cumin Seeds.',
            'Cook until the Cumin Seeds are golden brown - a few seconds.',
            'Add the Black-Eyed Peas and stir.',
            'Add the Turmeric, Cayenne Pepper (if using), Coriander Powder, Salt and Water. Stir to mix.',
            'Bring to a boil.',
            'Cover with a lid and reduce the heat.',
            'Simmer until most of the water is absorbed - 10 to 12 minutes.'
            'Add the Garam Masala and Lemon Juice and stir to combine.',
            'Transfer to a serving Platter and enjoy.'
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
