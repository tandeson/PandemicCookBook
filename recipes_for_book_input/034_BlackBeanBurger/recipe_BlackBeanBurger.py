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
        r = MyRecipe('Black Bean Burger', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BurgerOnAPlate', 'IMG_1336.JPG')
        r.setPrimaryPicture('BurgerOnAPlate')
        
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Black Beans', 1, 'can, 15 oz')
        r.addIngredient('Quinoa', 0.75, 'cup, cooked')
        r.addIngredient('Tomato Paste', 3, 'oz')
        r.addIngredient('Paprika', 1, 'teaspoon')
        r.addIngredient('Onion Powder', 1, 'teaspoon')
        r.addIngredient('Garlic Powder', 0.5, 'teaspoon')
        r.addIngredient('Oregano', 0.5, 'teaspoon')
        r.addIngredient('Salt', 1, 'pinch')
        r.addIngredient('Black Pepper', 1, 'pinch')
        r.addIngredient('Breadcrumbs', 0.3, 'cup')
        
        # Add Steps and Notes
        steps= [
            'Drain and rinse the Black Beans and place in a bowl. Mash.',
            'Add in the Quinona, Tomato Paste, spices and Breadcrumbs.',
            'Mix well.',
            'Form into hamburger shaped patties.',
            'Fry for 4 minutes on each side.'
            
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
