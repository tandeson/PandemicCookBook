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
        r = MyRecipe('Chilli', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('ChilliBowl', 'Chilli_bowl_1.jpg')
        r.setPrimaryPicture('ChilliBowl')
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Extra Virgin Olive Oil', 4, 'tablespoons')
        
        r.addIngredient('Garlic', 6, 'cloves, chopped')
        r.addIngredient('Yellow Onion', 1, 'large, chopped')
        r.addIngredient('Celery', 3, 'ribs, chopped')
        r.addIngredient('Jalapeno Pepper', 2, 'seeded and chopped')
        r.addIngredient('Red Bell Pepper', 1, 'seeded and chopped')
        
        r.addIngredient('Tomatoes', 3, 'seeded and chopped')
        r.addIngredient('Black Beans', 2, 'cans, 16 oz')
        r.addIngredient('Kidney Beans',2, 'cans, 16 oz')
        r.addIngredient('Vegetable Broth', 2, 'cup' )
        
        r.addIngredient('Molasses', 2, 'tablespoons')
        r.addIngredient('Smoked Paprika', 1, 'tablespoon')
        r.addIngredient('Cumin', 2, 'tablespoons')
        r.addIngredient('Chili powder', 1, 'tablespoon')
        r.addIngredient('Salt', 2, 'teaspoons')
        r.addIngredient('Black Pepper', 1, 'teaspoons')
        
        r.addIngredient('All Purpose Flour', 2, 'tablespoons')
          
        # Add Steps and Notes
        steps= [
            'In a large pot, heat the olive oil on medium high heat.',
            'Add in the Garlic, onion, celery, peppers. cook until softened, about 3 minutes.',
            'Add in the beans, tomatoes and broth. Bring to a boil.',
            'Reduce heat and add in molasses and spices. stir well and let heat for 10 minutes.',
            'Add in the flour to thicken, and stir well. Let cook for an additional 10 minutes.',
            'Remove from heat and serve.'
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
