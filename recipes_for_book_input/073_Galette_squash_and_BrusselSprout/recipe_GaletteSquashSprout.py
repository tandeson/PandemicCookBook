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
        r = MyRecipe('Butternut Brussels Sprout goat cheese Galette', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('GaletteSlice', '2021_Galette_slice.JPEG')
        r.addPicture('GaletteFull','2021_Galette_Full.JPEG')
        r.setPrimaryPicture('GaletteFull')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        ## ---
        r.addIngredient('Premade Pastry Shell', 1, '9" round')
        r.addIngredient('Butternut Squash', 12, 'oz, cut in 1/4" cubes')
        r.addIngredient('Brussel Sprouts', 1, 'cup, shaved')
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoon')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Black Pepper', 0.25, 'teaspoon')
        r.addIngredient('Goat Cheese', 4, 'oz  Cream Cheese or')
        r.addIngredient('Oregano', 2, 'tablespoons')
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 400 deg F and line a baking sheet with foil.',
            'Slice peeled and seeded squash into 1/4 inch cubes and slice brussels into thin slices.',
            'In a large bowl, first toss squash with 1/2 the oil, salt and pepper.',
            'Place on the pan, and roast for 15 minutes.',
            'While squash is roasting, prepare the brussels sprouts in the same way, with the remaining oil, salt and pepper.',
            'When the time is up, add the brussels sprouts to the pan, and roast for an additional 10 minutes.',
            'Return the squash and sprouts to the bowl. Change the oven temperature to 375 deg F.',
            'Add the goat cheese and herbs to the bowl and toss. Adjust seasoning as you see fit.'
            'Put parchment paper on the baking sheet and Place the Pastry shell on it.',
            'Fill the middle of the shell with the mixture from the bowl, and fold the edges up to form a galette.'
            'Place the galette in the oven for 40-50 minutes at 375 or until the crust is golden brown. Serve warm.'
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
