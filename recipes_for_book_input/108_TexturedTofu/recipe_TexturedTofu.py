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
        r = MyRecipe('Textured Tofu', 'Appetizers', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('TofuTextured', 'PostFrozenTofu.jpg')
        r.setPrimaryPicture( 'TofuTextured')
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Tofu', 1, 'block, extra-firm')
        
        r.AddDescription('Andrew shared with us this trick to get tofu to have a spongy texture, which soask up sauce and improves a number of recipes!')
        
        ## Steps
        steps = [
            'Open and drain tofu.',
            'Place the tofu in ziplock plastic bag.',
            'Place the Tofu in the freezer for at least 24 hours.',
            'Thaw out the tofu - in the refigerator if you don\'t need it for a day - or on the counter if you want to use it in a few hours.',
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
