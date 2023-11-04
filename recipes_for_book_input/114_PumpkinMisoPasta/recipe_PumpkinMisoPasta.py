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
        
        ## From First for women magaizin, 2020-11-30
        
        r = MyRecipe('Pumpkin Miso Pasta', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('pasta_in_pan', 'IMG_3933.jpeg')
        r.setPrimaryPicture('pasta_in_pan')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Spagetti', 16, 'oz dry, or equivalant')
        r.addIngredient('Salt', 2, 'tablespoons, to taste')
        r.addIngredient('Pumpkin Puree', 6, 'oz')
        r.addIngredient('Miso Paste', 3, 'tablespoons')
        r.addIngredient('Red Pepper Flakes', 2, 'teaspoons')
        r.addIngredient('Almond Milk', 1, 'cup, or equivalent')
                              
        # Add Steps and Notes
        steps= [
            'Prepare Spagetti or other pasta per package\'s instructions',
            
            'While the pasta is boiling, bring a skillet to medium heat. Add '
            'the pumpkin, miso paste and red pepper flakes to the pan. Immediately '
            'begin to mix the ingredients together.',
            
            'About 1/4 cup at a time, gradually add the milk to the pan, stirring '
            'constantly so that all of the ingredients meld together. During this time '
            'you are cooking the "raw" flavor out of the pumpkin, while simultaneously '
            'bringing out the umami flavor of the miso. Cook this mixture on the stove '
            'for about 4-5 minutes, stirring constantly.',
            
            'When you see the sauce start to thicken and reduce, turn off the heat '
            'source but keep the pan on the stove.',
            
            'When your pasta is done boiling, reserve 1/2 cup of starchy pasta water. Drain the rest.',
            
            'Add the pasta directly into the pan with the sauce. Mix to combine, then using '
            '1 tablespoon at a time, gradually add in the pasta water. You might not need all '
            'of the water, so just add until you think the sauce is smooth, glossy, and coating the pasta.'
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
