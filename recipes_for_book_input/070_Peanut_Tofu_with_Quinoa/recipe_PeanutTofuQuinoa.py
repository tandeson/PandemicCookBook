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
        r = MyRecipe('Tofu with Peanut Sauce in Quinoa', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Bowl_1', '2021_PeanutTofuBowl.JPEG')
        r.addPicture('Bowl_2', '2021_PeanutTofuBowl2.JPEG')
        r.setPrimaryPicture( 'Bowl_2' )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        
        r.addIngredient('Fried Tofu', 14, 'oz')
        
        grpQuinoa ="Coconut Quiona"
        r.addIngredient('Quinoa', 1, 'cups', grpQuinoa)
        r.addIngredient('Coconut Milk', 0.5, 'cup, full fat', grpQuinoa)
        r.addIngredient('Water', 1.25, 'cups', grpQuinoa)
        r.addIngredient('Salt', 1, 'Pinch to taste', grpQuinoa)
        
        grpPeanutSauce = "Peanut Sauce"
        r.addIngredient('Peanut Butter', 0.5, 'cups, creamy', grpPeanutSauce)
        r.addIngredient('Coconut Milk', 1.0, 'cup', grpPeanutSauce)
        r.addIngredient('Soy Sauce', 2, 'tablespoons', grpPeanutSauce)
        r.addIngredient('Maple Syrup', 2, 'tablespoons', grpPeanutSauce)
        r.addIngredient('Ginger', 2, 'teaspoons, fresh grated', grpPeanutSauce)
        r.addIngredient('Garlic', 2, 'cloves, minced', grpPeanutSauce)
        r.addIngredient('Lime', 1, 'for juice only', grpPeanutSauce)
        
        # Add Steps and Notes
        r.addStep( 
            RecipeStep( "Cook the Coconut Quinoa",[
                RecipeStep( 
                    'Put the water, Quinoa, Coconut milk and water into a medium'
                    ' pot. Bring to boil, then let simmer for 15 minutes covered.'
                    ' Turn off the heat and remove the lid.' )
                ] 
            )
        )
        r.addStep( 
            RecipeStep( "Make the Sauce",[
                RecipeStep(
                    'In a large pan add all the sauce ingredients and turn the heat'
                    ' to medium, stir constantly until smooth and creamy, about 5-10'
                    ' minutes.'),
                RecipeStep(
                    'Mix in the fried Tofu, and stir until well mixed.')
                ]
            )
        )                
    
        r.addStep( 
            RecipeStep( "Put the Quinoa into a bowl, and scoop the sauce on top to serve.")
        )
        
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
