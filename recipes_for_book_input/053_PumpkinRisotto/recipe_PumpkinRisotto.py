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
        r = MyRecipe('Pumpkin Risotto', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BowlOfRisotto', 'PumpkinRisottoOnPlate.jpg')
        r.setPrimaryPicture( 'BowlOfRisotto')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')    
        #  -- Add Ingredients --
        
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoon')
        r.addIngredient('Unsalted Butter', 1, 'tablespoon')
        r.addIngredient('Yellow Onion', 1, 'medium, chopped')
        r.addIngredient('Garlic', 5, 'cloves')
        r.addIngredient('Arborio Rice', 1, 'cup, dry')
        r.addIngredient('Wine', 0.5, 'cup, White ')
        r.addIngredient('Vegetable Broth', 3.5, 'cups')
        r.addIngredient('Pumpkin Puree', 0.75, 'can, 15 oz')
        r.addIngredient('Peas', 0.75, 'cup, frozen')
        r.addIngredient('Ancho Chili powder', 0.5, 'teaspoon')
        r.addIngredient('Rosemary', 0.5, 'teaspoon')
        r.addIngredient('Nutmeg', 0.75, 'teaspoon')
        r.addIngredient('Parmesan Cheese', 0.75, 'cup, shredded')
                
        # Add Steps and Notes
        steps = [
            'Heat Oil and Butter in a pot over medium heat.',
            'Add Onion and Garlic, cook until softened.',
            'Add in Rice, stir for 30 seconds until combined.',
            'Add in Wine, stir until absorbed.'
            ]
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        r.addStep( RecipeStep(
            'Start stirring in the broth, 0.5 cups at a time. Broth should be warm. At each addition, stir until absorbed before adding the next 0.5 cup.',
            [    
                RecipeStep('After the first 0.5 cups, Add in spices'),
                RecipeStep('With the last 0.5 cup of broth, add peas, pumpkin and Parm.')
            ]))
        
        r.addStep( RecipeStep( 'Stir until fully absorbed, take off heat.'))
        r.addStep( RecipeStep( 'Serve with additional Parm. Ta Da.' ))
        
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
