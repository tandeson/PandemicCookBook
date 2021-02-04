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
        
        r = MyRecipe('Zoodles', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('OurZoodles', 'Zoodles_Nov2020.jpg')
        r.setPrimaryPicture('OurZoodles')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Zucchini', 4, 'large')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Garlic', 5, 'cloves, to taste')
        r.addIngredient('Red Pepper Flakes', 1, 'teaspoon')
        r.addIngredient('Marinara Sauce', 1, 'jar')
                              
        # Add Steps and Notes
        steps= [
            'Zoodle the zucchini, removing large chunk of skin from the pile.',
            'Heat the oil in a frying pan on medium heat.',
            'Lightly cook the zoodles with the red pepper flakes and garlic, 3-5 minutes.',
            'Add in pasta sauce and cook until heated.',
            'Season to taste.'
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
