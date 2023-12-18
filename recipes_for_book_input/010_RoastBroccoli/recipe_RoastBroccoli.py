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
        r = MyRecipe('Roast Broccoli',"Appetizers", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('RoatedBroc', 'IMG_2328.JPEG')
        r.setPrimaryPicture('RoatedBroc')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        r.AddDescription('One of our most favorite dishes, we eat it as a side to almost anything!')
        
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Broccoli', 1.5, 'pounds ( 1 bunch)')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Garlic', 3, 'cloves, sliced')
        r.addIngredient('Salt', 1, 'pinch')
        r.addIngredient('Black Pepper', 1, 'pinch')
        
        # Add Steps and Notes
        steps = [
            'Pre-heat the oven to 450 deg F.',
            'Slice the broccoli into 1/2 or 1/4 florets. stems peeled and sliced.',
            'Toss the Broccoli with olive oil, Garlic, Salt on a baking sheet. '
            'Spread them out and then roast, without stirring, until the edges '
            'are crispy and the stems are crips tender - about 20 minutes.',
            'Serve warm.'
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
