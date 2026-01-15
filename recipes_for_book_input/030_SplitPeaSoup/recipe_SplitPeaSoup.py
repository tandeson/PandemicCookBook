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
        r = MyRecipe('Split Pea Soup', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('splitpea_1', 'Splitpea_Cup_1.JPEG')
        r.addPicture('splitpea_2', 'Splitpea_Cup_2.JPEG')
        r.setPrimaryPicture('splitpea_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Extra Virgin Olive Oil', 4, 'tablespoons')
        r.addIngredient('Garlic', 4, 'cloves, chopped')
        r.addIngredient('Yellow Onion', 1, 'medium, chopped')
        r.addIngredient('Celery', 4, 'sticks, chopped')
        r.addIngredient('Vegetable Broth', 8, 'cups')
        r.addIngredient('Split Peas', 1, 'bag, 1 pound, dry')
        
        # Add Steps and Notes
        steps= [
            'Heat a large pot with a lid over medium-high heat.',
            'Add the oil, garlic, celery and Onion. Stir until the Onion becomes translucent, about 2-3 minutes.',
            'Add in Vegetable Broth, raise the heat to high, and bring to just boiling.',
            'Add the Split Peas, and move the heat to low.',
            'Simmer for about 1 hour with the lid on.',
            'Check the Peas, if they are not soft, simmer for another 20-30 minutes.',
            'Mash the soft mixture with a Potato masher until smooth.',
            'Serve!'
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
