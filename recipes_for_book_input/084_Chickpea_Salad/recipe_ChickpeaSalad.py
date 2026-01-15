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
        r = MyRecipe('Chickpea Salad', 'Salads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('chickpea_salad_1', 'IMG_2337.JPEG')
        r.addPicture('chickpea_salad_2', 'IMG_2338.JPEG')
        r.setPrimaryPicture('chickpea_salad_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')

        #  -- Add Ingredients --

        ##
        r.addIngredient('Chickpeas', 15, 'oz, 1 can')
        r.addIngredient('Green Onion', 3, 'stalks')
        r.addIngredient('Celery', 2, 'stalks')
        r.addIngredient('Carrot', 0.25 , 'cups, chopped')
        r.addIngredient('Red Bell Pepper', 0.25, 'cups, chopped')
        r.addIngredient('Pickles', 0.25, 'cups, dill, chopped')
        r.addIngredient('Mayonnaise', 0.25, 'cups')
        r.addIngredient('Mustard', 2, 'teaspoons, dijon')
        r.addIngredient('Mustard', 2, 'teaspoons, yellow')
        r.addIngredient('Dill', 0.25, 'teaspoons')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Sunflower Seeds', 3, 'tablespoons, roasted')
        r.addIngredient('Basil', 2, 'tablespoons, chopped')
        
        # Add Steps and Notes
        steps = [
            'Drain and rinse your chickpeas and add them to a large bowl. Mash '
            'with a potato masher until texture appears flaked, almost like '
            'tuna salad. You can use both a potato masher and follow up with a fork '
            'to make sure every chickpea is smashed.',
            'Chop your green onion, celery, shredded carrots, pepper, and pickles.',
            'Add to the bowl with your chickpeas, then add mayo, dijon, yellow '
            'mustard, dill, salt, and pepper. Stir well to coat.',
            "Fold in sunflower seeds and basil (as much or as "
            "little as you'd like) and adjust any ingredients to taste.",
            'Serve on a wrap or in a sandwich.'
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
