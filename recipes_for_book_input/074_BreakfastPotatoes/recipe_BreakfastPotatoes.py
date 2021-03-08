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
        r = MyRecipe('Breakfast Potatoes', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('potatoes_1', 'PotatoesPlate_1.JPEG')
        r.addPicture('potatoes_2', 'PotatoesPlate_2.JPEG')
        r.setPrimaryPicture( 'potatoes_1')
        r.AddDescription(
            'This is the process')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Potato', 3, 'medium, russet')
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoons')
        r.addIngredient('Corn Starch', 3, 'tablespoons')
        r.addIngredient('Salt', 2, 'teaspoon, to taste')
        r.addIngredient('Black Pepper', 1, 'teaspoon, to taste')
        r.addIngredient('Red Onion', 1, 'medium, sliced')
        r.addIngredient('Garlic', 5, 'cloves, diced')
        
        r.addStep( RecipeStep('Wash and scrub the Potatoes') )
        r.addStep( 
            RecipeStep( 'Cook Potatoes (Microwave)', [
                RecipeStep('Poke holes in the Potatoes with a fork'),
                RecipeStep('Place in a microwave on a paper towel. Set to "baked potatoes" (usually about 10 min).'),
            ]))
        
        r.addStep(
            RecipeStep( 'Cook Potatoes (boiled)', [
                RecipeStep('Place in a pot and cover with cold salt water, and then bring to a boil'),
                RecipeStep('Reduce to a low boil, and cook for 25 - 30 minutes.'),
                RecipeStep('Drain, and let sit for 5 minute to dry the Potatoes.'),
            ]))
        
        # Add Steps and Notes
        steps = [
            'Heat oil on medium high heat in a large frying pan.',
            'Cut the potatoes into roughly 1/2" cubes.',
            'Place the potatoes in the pan, cover with Corn Starch, Salt and Pepper. Stir with a wooden spoon to mix well.',
            'Stir occasionally while the potatoes cook to get even browning. As soon as some side appear brown, add in the garlic and onion.',
            'Continue to cook until Potatoes are mostly brown, about 5 minutes. Remove from heat and serve.'
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
