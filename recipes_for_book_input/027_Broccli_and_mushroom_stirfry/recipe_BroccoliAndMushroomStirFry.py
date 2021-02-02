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
        r = MyRecipe('Broccoli and Mushroom Stir Fry', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('PlateOne', 'MushroomsAndBroccliPlate_1.jpg')
        r.addPicture('PlateTwo', 'MushroomsAndBroccliPlate_2.jpg')
        r.setPrimaryPicture('PlateOne')
        
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Garlic', 6, 'cloves, or more')
        r.addIngredient('Ginger', 2 , 'tablespoons, chopped')
        r.addIngredient('Red Pepper Flakes', 1, 'shake, or to taste')
        r.addIngredient('Soy Sauce', 3, 'tablespoons (aprox)')
        r.addIngredient('Rice Vinegar', 3 , 'tablespoons (aprox)')
        r.addIngredient('Broccoli', 3, 'heads, about 1 pound, chopped')
        r.addIngredient('Mushrooms', 8, 'oz (or more) chopped')
        r.addIngredient('Sesame seeds', 2, 'tablespoons (aprox)')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons (aprox)')
        # Add Steps and Notes
        steps= [
            'Heat olive oil in pan on medium-high heat.',
            'Add ginger, garlic and red pepper flakes',
            'Saute for 1 - 2 minutes until fragrant',
            'Add broccoli and a little water - roughly 2 tablespoons to steam them.',
            'Stir for about 5 min, until broccoli becomes a brighter green',
            'Add mushrooms, continue to stir over head for 10 - 15 minutes until everything is cooked.',
            'Combine soy sauce and vinegar, then stir in for 5 -10 seconds.',
            'Remove from heat, sprinkle with sesame seeds',
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
