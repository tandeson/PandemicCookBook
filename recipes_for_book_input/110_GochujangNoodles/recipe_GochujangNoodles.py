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
        r = MyRecipe('Gochujang Noodles', 'Main dishes', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('2022_gochujang_noodles', '2022_gochujang_noodles.JPG')
        r.setPrimaryPicture('2022_gochujang_noodles')
        r.setRecipeFormat('FANCY_LONG_RECIPE')
        
        #  -- Add Ingredients --
        
        ## Makes about 2 dozen?
        #--
        
        grpNoodles = "Noodles"
        r.addIngredient('Dry Wide Rice Noodles', 8, 'oz', grpNoodles)
        
        grpSauce = 'Sauce'
        r.addIngredient('Gochujang Paste', 3 ,'tablespoons', grpSauce)
        r.addIngredient('Hoisin Sauce', 3 ,'tablespoons', grpSauce)
        r.addIngredient('Soy Sauce', 2 ,'tablespoons, dark', grpSauce)
        r.addIngredient('Lime', 2, 'tablespoons, juice', grpSauce)
        r.addIngredient('Sesame Oil', 2, 'tablespoon', grpSauce)
        r.addIngredient('Garlic', 5, 'cloves, diced', grpSauce)
        
        grpVegitables = "Vegitables"
        r.addIngredient('Vegetable Oil', 1, 'tablespoon',grpVegitables)
        r.addIngredient('Red Bell Pepper', 0.5, 'seeded and sliced', grpVegitables)
        r.addIngredient('Savoy Cabbage', 0.5, 'head, shredded', grpVegitables)
        r.addIngredient('Carrot', 0.5, 'cup, shredded',grpVegitables)
        
        # Add Steps and Notes
        steps = [
            'Cook the noodles as per the package directions. Drain and set aside.',
            
            'Make the sauce by Stiring together the gochujang paste, hoisin sauce, soy sauce, '
            'lime juice, sesame oil, and garlic in a small bowl.',
            
            'Heat vegetable oil in a large skillet over high heat.',
            'Once the oil is hot, add mixed bell peppers, cabbage, and carrots and saute for a minute on high heat.',
            'Add the cooked noodles and the sauce mixture and toss everything well using two large spoons or a pair of tongs',
            'Serve hot.'
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
