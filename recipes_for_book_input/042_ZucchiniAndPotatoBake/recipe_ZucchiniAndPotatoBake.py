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
        r = MyRecipe('Zucchini and Potato Bake', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture( 'plate_1', '20201_ZucchiniPotatoBake_1.jpg' )
        r.addPicture( 'plate_2', '20201_ZucchiniPotatoBake_2.jpg' )
        
        r.setPrimaryPicture( 'plate_1' )
        ## Source: https://www.simplyquinoa.com/detox-moroccan-lentil-soup/
        #  -- Add Ingredients --

        ##
        r.addIngredient('Zucchini', 2, 'medium' )
        r.addIngredient('Potato', 4, 'medium')
        r.addIngredient('Red Bell Pepper', 1, 'medium')
        r.addIngredient('Garlic', 2, 'Cloves, sliced')
        r.addIngredient('Breadcrumbs', 0.5, 'cups')
        r.addIngredient('Extra Virgin Olive Oil', 0.25, 'cups')
        r.addIngredient('Paprika', 1, 'pinch, to taste')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        
        # Add Steps and Notes
        steps= [
            'Preheat oven to 400 deg F.',
            'Quarter the Zucchini, and then cut into large pieces.',
            'Peel the potatoes, and cut into large chunks.',
            'Seed the Red Bell Pepper, and chop.',
            'In a medium baking pan, toss together the zucchini, potatoes, red bell pepper, '
            'garlic, bread crumbs, and olive oil. Season with paprika, salt, and pepper.',
            'Bake 1 hour in the preheated oven, stirring occasionally, until potatoes are tender and lightly brown.'
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
