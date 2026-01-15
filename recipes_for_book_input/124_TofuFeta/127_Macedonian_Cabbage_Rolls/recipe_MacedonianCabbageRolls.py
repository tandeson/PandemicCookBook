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
        
        ## From First for women magaizin, 2020-11-30
        
        r = MyRecipe('Cabbage Rolls', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')
        #  -- Add Ingredients --

        ##
        strGrpCabbage = 'For the Cabbage'
        r.addIngredient('Pickled Cabbage Leaves', 30, 'leaves', strGrpCabbage)
        
        strGrpFilling = 'For the Filling'
        r.addIngredient('Extra Virgin Olive Oil',3, 'tablespoons', strGrpFilling)
        r.addIngredient('Onion', 2, 'large, finely diced', strGrpFilling)
        r.addIngredient('Garlic', 4, 'cloves, minced', strGrpFilling)
        r.addIngredient('Parsley', 0.25, 'cup, minced', strGrpFilling)
        r.addIngredient('Tomatoes', 2, 'fresh, finely chopped', strGrpFilling)
        r.addIngredient('Tomato Paste', 3, 'tablespoons', strGrpFilling)
        r.addIngredient('Smoked Paprika', 2, 'teaspoons', strGrpFilling)
        r.addIngredient('Salt', 2, 'tablespoons, to taste', strGrpFilling)
        r.addIngredient('Black Pepper', 1, 'teaspoon', strGrpFilling)
        r.addIngredient('Oregano', 1, 'teaspoon, dried', strGrpFilling)
        r.addIngredient('Thyme', 1, 'teaspoon, dried', strGrpFilling)
        r.addIngredient('Rice', 2, 'cups, long grain white', strGrpFilling)
        r.addIngredient('Walnuts', 1, 'cup, chopped', strGrpFilling)
        
        
        strGrpSauce = 'For the Sauce'
        r.addIngredient('Extra Virgin Olive Oil',3, 'tablespoons', strGrpSauce)
        r.addIngredient('Garlic', 4, 'cloves, minced', strGrpSauce)
        r.addIngredient('Smoked Paprika', 1, 'tablespoon', strGrpSauce)
        r.addIngredient('Vegetable Broth', 2, 'cups', strGrpSauce)
                
        # Add Steps and Notes
        steps= [
            'Preheat oven to 350 deg F.',
            'Grease a 9x13 baking dish with cooking spray and set aside.',
            
            'Heat 3 tablespoons olive oil in a large skillet set over medium-high heat.',
            'Add the onions to the heated oil and cook for 3 minutes, stirring occasionally.',
            'Stir in the garlic and parsley; cook for 30 seconds.',
            'Add in the tomatoes and stir in the tomato paste; season with paprika, salt, pepper, oregano, thyme, and lemon pepper seasoning, and continue to cook for 4 minutes, stirring frequently, until tomatoes are tender.',
            'Add the rice and saute for 1 minute. Remove from heat.',
            'Using a paring knife, cut off the raised part of the vein on each cabbage leaf. This will make it easier to roll.',
            "Lay the leaf flat on your hands and place a heaping spoonful of the filling on one side of the leaf; add a piece of walnut in the middle of the filling. Don't add too much filling because it will be too stuffed to roll it up.",
            "Roll it up tightly, tucking in the sides of the leaf, kind of like you would roll up a burrito.",
            "Place the stuffed cabbage rolls in previously prepared baking dish, seam sides down. Season tops with salt and black pepper. Set aside.",
            "Heat 3 tablespoons olive oil in a saucepan.",
            "Add garlic to the heated oil and cook for 15 seconds.",
            "Mix in the sweet paprika. Stir in the broth and bring to a boil.",
            "Pour the hot liquid over the cabbage rolls.",
            "Cover the dish with a lid or aluminum foil. Bake for 45 minutes.",
            "Remove the cover and continue to bake for 15 minutes.",
            "Remove from oven and check to make sure that the rice is cooked through; if not, put it back in the oven for 10 to 12 minutes longer.",
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
