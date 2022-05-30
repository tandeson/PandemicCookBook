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
        r = MyRecipe('Cashew Cheese', "Appetizers", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Cheese_1', '2021_Cheese.jpg')
        r.setPrimaryPicture('Cheese_1')
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')
        
         
        ## --
        r.addIngredient('Cashews', 1, 'cup, raw')
        
        r.addIngredient('Lemon', 1, 'juiced')
        r.addIngredient('Garlic Powder', 1, 'teaspoon')
        r.addIngredient('Onion Powder', 0.5, 'teaspoons')
        r.addIngredient('Smoked Paprika', 1, 'teaspoon')
        r.addIngredient('Nutritional Yeast', 0.5, 'cups')
        r.addIngredient('Turmeric', 0.5, 'teaspoons')
        r.addIngredient('Salt', 0.5, 'teaspoons, to taste')
        r.addIngredient('Water', 1.25, 'cups')
        
        r.addIngredient('Agar Agar Powder', 1, 'tablespoon')
        
        
        
        # Add Steps and Notes
        steps= [
            'Soak the cashews overnight in water, drain before using the nex day.',
            'Blend the cashews, Lemon, spices and 0.5 cups water until uniform, set aside.',
            
            'Put Agar Agar powder and remaining 0.75 cups of water into a pot and bring to boil then simmer for 5 minutes while stiring constantly.',
            'Add the blended mixture and stir.'
            
            'Pour the mixture into a container lined with parchment paper.',
            'Let sit in the refigerator for at least two hours - then Enjoy!'
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
