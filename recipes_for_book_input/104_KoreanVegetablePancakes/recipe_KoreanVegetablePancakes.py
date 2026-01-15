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
        r = MyRecipe('Korean Vegetable Pancakes', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Pancake_1', 'IMG_3151.jpeg')
        r.addPicture('Pancake_2', 'IMG_3152.jpeg')
        r.setPrimaryPicture('Pancake_1')
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')
        ## ---
        
        grpRecipeBatter = "Batter"
        r.addIngredient('All Purpose Flour', 1.5 , 'cups', grpRecipeBatter)
        r.addIngredient('Baking Powder', 2 , 'teaspoons', grpRecipeBatter)
        r.addIngredient('Corn Starch', 4 , 'tablespoons', grpRecipeBatter)
        r.addIngredient('Salt', 1.5 , 'teaspoons', grpRecipeBatter)
        r.addIngredient('Turmeric', 0.5 , 'teaspoons', grpRecipeBatter)
        r.addIngredient('Water', 1.5 , 'cups', grpRecipeBatter)
        
        grpRecipeVegies = "Vegetable Mix"
        r.addIngredient('Zucchini', 1, 'medium, sliced into matchsticks', grpRecipeVegies)
        r.addIngredient('Sweet Potatoes', 1, 'small, sliced into matchsticks', grpRecipeVegies)
        r.addIngredient('Carrot', 1, 'medium, sliced into matchsticks', grpRecipeVegies)
        r.addIngredient('Onion', 0.5, 'medium, sliced thin', grpRecipeVegies)
        r.addIngredient('Jalapeno Pepper', 1, 'medium, sliced into matchsticks', grpRecipeVegies)
        r.addIngredient('Green Onion', 1, 'bunch, chopped', grpRecipeVegies)
        r.addIngredient('Shredded Cabbage', 1, 'cup', grpRecipeVegies)
        
        r.addIngredient('Vegetable Oil', 2, 'tablespoons','For Frying')
        ## Steps
        steps = [
            'In bowl, mix all the Batter ingredients except water. Once it is mixed well - add the water and mix.',
            'In another large bowl, place all the vegetables.',
            'Add the batter to the vegetables, and mix so they are well coated.',
            'Heat a large frying pan on medium heat, add in the oil.',
            'When the pan is hot - and the oil is translucent - put enough of the mixture into the pan to cover. '
            'Fry for 1-2 minutes, then flip and repeat. When the pancake is cooked - remove and cut into 1/4ths.'
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
