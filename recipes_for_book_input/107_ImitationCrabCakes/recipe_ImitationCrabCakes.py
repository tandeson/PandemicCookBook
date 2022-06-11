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
        r = MyRecipe('Imitation Crab Cakes', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('ImitationCakes_1', 'ImitationCrabCakes_1.jpeg')
        r.addPicture('ImitationCakes_2', 'ImitationCrabCakes_2.jpeg')
        r.setPrimaryPicture('ImitationCakes_1')
        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        r.addIngredient('Chickpeas', 1, 'can drained and rinsed')
        r.addIngredient('Artichoke Hearts', 1, 'can drained and chopped')
        r.addIngredient('Breadcrumbs', 0.75, 'cups')
        r.addIngredient('Nori', 2, 'sheet, chopped into flakes')
        r.addIngredient('Mayonnaise', 0.25, 'cups')
        r.addIngredient('Lemon Juice', 2, 'tablespoon')
        r.addIngredient('Mustard', 1, 'tablespoon dijon')
        r.addIngredient('Non-Iodized Salt', 0.5, 'teaspoon')
        r.addIngredient('Black Pepper', 0.5, 'teaspoon')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        
        ## Steps
        steps = [
            'In a large bowl add the chickpeas. Use a potato masher to mash into a rough paste.',
            'Add in the artichokes, bread-crumbs, chopped nori, mayonnaise, lemon juice, dijon '
            'mustard, salt, and pepper. Mix gently.',
            'Divide the mixture into 6 and use your hands to form 6 patties.',
            'Heat the oil in a large skillet over medium high heat. When hot add the patties and fry 3-5 minutes per side until golden brown.',
            'Serve hot.'
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
