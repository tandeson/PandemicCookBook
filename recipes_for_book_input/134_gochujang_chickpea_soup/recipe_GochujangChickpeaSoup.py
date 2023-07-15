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
        r = MyRecipe('Gochujang Chickpea Soup', 'Main dishes', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('gochujang_soup_1', 'IMG_4017.jpeg')
        r.addPicture('gochujang_soup_2', 'IMG_4018.jpeg')
        r.setPrimaryPicture('gochujang_soup_1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --
        #--
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoon')
        r.addIngredient('Yellow Onion', 1, 'medium, diced')
        r.addIngredient('Carrot', 1, 'large, chopped')
        r.addIngredient('Celery', 2, 'stalks, chopped')
        r.addIngredient('Jalapeno Pepper', 1, 'de-seeded and diced')
        r.addIngredient('Garlic', 5, 'cloves, diced')
        r.addIngredient('Ginger', 0.5, 'inch, grated')
        r.addIngredient('Gochujang Paste', 1 ,'tablespoons')
        r.addIngredient('Chickpeas', 1, 'can, 15 oz')
        r.addIngredient('Quinoa', 0.5, 'cups, dry')
        r.addIngredient('Coriander Powder', 1, 'teaspoon')
        r.addIngredient('Thyme', 1, 'teaspoon, dry powder')
        r.addIngredient('Vegetable Broth', 2.5, 'cups')
        r.addIngredient('Miso Paste', 1, 'tablespoon')
        r.addIngredient('Sesame Oil', 2, 'tablespoons')
        
        

        
        # Add Steps and Notes
        steps = [
            'Heat a small pot or saucepan over medium heat then add the oil'
            ' to warm through. Add the onions, carrots, celery and jalapeno'
            ' along with a pinch of salt and saute until the onions have softened.',
            
            'Add the garlic and ginger then saute again until fragrant then stir in'
            ' the gochujang and saute for 1 minute.',
            
            'Add in the chickpeas, quinoa, coriander and thyme, then pour in the broth.'
            ' Bring the pot to a boil, then reduce to a low simmer and cook partially covered'
            ' with a lid for 15 minutes.',
            
            'Combine the miso paste with 2 tablespoons of water and whisk until no lumps remain.'
            ' Once the soup has finished cooking, remove from heat and stir in the miso mixture'
            ' along with the sesame oil. Adjust salt to taste and serve'
            ]
        
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        # Notes
        
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
