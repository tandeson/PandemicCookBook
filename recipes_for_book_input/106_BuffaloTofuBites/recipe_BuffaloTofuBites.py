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
        r = MyRecipe('Buffalo Tofu Bites', 'Appetizers', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Bites_1', 'IMG_2915.jpeg')
        r.addPicture('Bites_2', 'IMG_2916.jpeg')
        r.setPrimaryPicture( 'Bites_2')
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Textured Tofu', 1, 'block, extra-firm')
        
        r.addIngredient('Almond Milk', 1.5, 'cups, aprox')
        r.addIngredient('Corn Starch', 0.75, 'cup, apox')
        r.addIngredient('Breadcrumbs', 0.75, 'cup, aprox')
        r.addIngredient('Hot Sauce', 3, 'tablespoons, to taste')
        
        
        ## Steps
        steps = [
            'Drain Tofu and chop into large cubes.',
            'Preheat the over to 400 deg F.',
            'Get a bowl and two plates. Put Almond Milk into the bowl, Corn Starch on one plate and Breadcrums on the other. '
            'Put out baking sheet with a wire rack on top( so all sides get crispy)',
            'Take each piece and dunk in: Almond Milk - Corn Starch - Almond Milk - Breadcrumbs. Then place on the wire rack.',
            'Bake for 25 minutes.',
            'Cool for 5 minutes, and the toss with the Hot Sauce in a bowl. We like to use Frank\'s Hot Sauce.'
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
