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
        r = MyRecipe('Ethiopian Style Kale', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('KaleOnAPlate', 'IMG_1303.JPEG')
        r.setPrimaryPicture('KaleOnAPlate')
        
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Kale', 10, 'oz, or Collard Greens')
        r.addIngredient('Extra Virgin Olive Oil', 3 , 'tablespoons, or Butter')
        r.addIngredient('Ginger', 1.5 , 'teaspoons, minced')
        r.addIngredient('White Onion', 1, 'large, chopped')
        r.addIngredient('Smoked Paprika', 1, 'teaspoon')
        r.addIngredient('Cardamom', 0.5, 'teaspoon')
        r.addIngredient('Chili powder', 0.5, 'teaspoon')
        r.addIngredient('Cayenne Pepper', 0.5, 'teaspoon')
        r.addIngredient('Lemon', 1, 'medium')
        
        # Add Steps and Notes
        steps= [
            'In a large skillet, add oil, garlic, ginger, chili pepper, cumin, cardamom, '
            'paprika, saute for about 30 seconds or more, be careful not to let the '
            'ingredients burn.',
            'Add onions, mix with the spices. Saute for about 3-5 minutes.',
            'Throw in chopped Kale, cayenne pepper, lemon juice.',
            'Continue cooking for another 7-10 minutes until flavors have blend and greens are cooked, according to preference.',
            'Adjust seasoning - Salt and pepper.',
            'Remove from heat and let cool.'
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
