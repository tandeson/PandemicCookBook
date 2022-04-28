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
        r = MyRecipe('Thai Basil Tofu', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('scramble_on_bread', 'IMG_3049.jpeg')
        r.addPicture('scramble_in_pan', 'IMG_3050.jpeg')
        r.setPrimaryPicture( 'scramble_on_bread')
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Tofu', 1, 'block, extra-firm')
        r.addIngredient('Red Onion', 1, 'medium, diced')
        r.addIngredient('Garlic', 6, 'cloves, diced')
        r.addIngredient('Jalapeno Pepper',1, 'seeded and diced')
        r.addIngredient('Thai Basil', 1, 'package')
        
        grpSauce = "Sauce"
        r.addIngredient('Hoisin Sauce', 1, 'tablespoon', grpSauce)
        r.addIngredient('Soy Sauce', 1, 'tablespoon', grpSauce)
        r.addIngredient('Fish Sauce', 1, 'tablespoon', grpSauce)
        r.addIngredient('Corn Starch', 1, 'teaspoon', grpSauce)
        r.addIngredient('Water', 0.5, 'cups', grpSauce)
        
        ## Steps
        steps = [
            'Mix the sauce ingredients in a mixing bowl until well-combined and set aside.',
            'In a heated non-stick pan, add the tofu in and using a potato masher, mash tofu into crumbles.',
            'Cook the tofu crumbles until slightly dry. Then, add about 1 tablespoon of oil and continue to cook until tofu turns golden brown.',
            'Push tofu aside, and add a little more oil and sauté red onion until translucent.',
            'Continue to saute garlic and chili for another 30 – 45 seconds. Then, bring all the mixture together and give it a quick stir.',
            'Add in the sauce and cook down the mixture a little.',
            'Finally, add the Thai basil and toss everything until all incorporated.',
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
