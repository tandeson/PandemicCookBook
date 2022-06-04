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
        r = MyRecipe('Farro with Roasted Carrots and Ginger Dill Dressing', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('FarroWithCarrots_1', 'IMG_3208.jpeg')
        r.addPicture('FarroWithCarrots_2', 'IMG_3209.jpeg')
        r.setPrimaryPicture('FarroWithCarrots_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')

        #  -- Add Ingredients --

        ##
        grpFarror = "Farro and Carrots"
        r.addIngredient('Farro', 1, 'cup, uncooked', grpFarror)
        r.addIngredient('Vegetable Broth', 2.5, 'cups', grpFarror)
        r.addIngredient('Carrot', 1, 'pound (about 4 large cut into pieces)', grpFarror)
        r.addIngredient('Yellow Onion', 1, 'chopped', grpFarror)
        r.addIngredient('Extra Virgin Olive Oil', 2, 'teaspoons', grpFarror)
        
        
        grpDressing = "Ginger Dill Dressing"
        r.addIngredient('Extra Virgin Olive Oil', 1.3, 'cups', grpDressing)
        r.addIngredient('Ginger', 1, 'teaspoon, diced', grpDressing)
        r.addIngredient('Lemon', 1, 'juiced', grpDressing)
        r.addIngredient('Maple Syrup', 1, 'teaspoon', grpDressing)
        r.addIngredient('Dill', 1, 'bunch, fresh, chopped', grpDressing)
        r.addIngredient('Salt', 1, 'pinch, to taste', grpDressing)
        r.addIngredient('Black Pepper', 1, 'pinch, to taste', grpDressing)
        
        
        
        # Add Steps and Notes
        steps = [
            "Pre-heat Oven to 400 Deg F.",
            "Line a pan with Parchment paper and place the carrots in a single layer on it. Coat  with olive oil.",
            "Bake for 25 - 30 minutes and then remove from oven.",
            
            "Put a pan on medium heat and add olive oil. Add onions and Satue for a few minutes.",
            "Add Farro and toast, stiring constantly for 2 minutes.",
            "Add Broth and bring to a boil. Lower heat and simmer for about 30 minutes covered, until cooked.",
            "Drain off excess liquid ( if any ) and set aside.",
            
            "For the Dressing - Add all ingredient except for dill to a blender, and mix well. Add Dill, and "
            "pulse a few times. Adjust seasoning to taste and set aside.",
            
            "In a large bowl - mix the roasted carrots, farro and dressing. Enjoy!"
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
