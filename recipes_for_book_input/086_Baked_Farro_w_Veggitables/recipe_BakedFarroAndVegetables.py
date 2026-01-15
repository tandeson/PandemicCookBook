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
        r = MyRecipe('Baked Farro with Vegetables', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BakeInBowl', 'BakeInBowl.jpeg')
        r.addPicture('BakeInPot', 'BakeInPot.jpeg')
        r.addPicture('BakeOnPlate', 'BakeOnPlate.jpeg')
        r.setPrimaryPicture('BakeOnPlate')
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')

        #  -- Add Ingredients --

        ##
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablesppons')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Black Pepper', 1, 'pinch, to taste')
        r.addIngredient('Corn', 3, 'ears')
        r.addIngredient('Zucchini', 1.5, 'pounds or similar')
        r.addIngredient('Yellow Onion', 1, 'medium, diced.')
        r.addIngredient('Garlic', 5, 'cloves, thinly sliced')
        r.addIngredient('Roma Tomato', 4, 'large, diced')
        r.addIngredient('Oregano', 1, 'teaspoon')
        r.addIngredient('Red Pepper Flakes', 0.5, 'teaspoon')
        r.addIngredient('Tomato Paste', 1, 'tablespoon')
        r.addIngredient('Wine', 0.25, 'cup, white or rose')
        r.addIngredient('Basil', 0.5, 'cup, fresh, sliced')
        r.addIngredient('Farro', 1, 'cup, uncooked')
        r.addIngredient('Water', 1.5, 'cups')
        r.addIngredient('Parmesan Cheese', 1, 'cup, grated')
        r.addIngredient('Mozzarella', 6, 'oz, diced')
        
        
        # Add Steps and Notes
        steps = [
            "pre-heat oven to 375 deg F.",
            
            "If you have an ovenproof 11-inch or 4-quart pan with a "
            "lid, use it here. If not, use a large (11- to 12-inch) "
            "saute pan for the stove portion and transfer it to a 3- "
            "to 4-quart baking dish for the oven part.",
            
            "On the stove, heat pan to medium-high. Once hot, add "
            "2 tablespoons olive oil. Let the oil warm and add corn and Zucchini. "
            "Season with 1/2 teaspoon salt and many grinds of black pepper"
            " and cook, stirring occasionally, until the corn is lightly golden,"
            " and zucchini is cooked - about 5 minutes. Tip into a large bowl.",
            
            "Reduce heat to medium and add another drizzle of olive oil. Add onion, "
            "1 teaspoon salt, red pepper flakes, and cook until the onion is translucent,"
            " about 2 minutes. Stir in the tomatoes, garlic, and oregano and cook, stirring"
            " occasionally, until the tomatoes soften and begin to form a sauce, about 5 "
            "minutes. Stir in the tomato paste and cook for 1 minute. Add the wine and cook"
            " until the wine has reduced and the sauce is fairly thick, about 3 minutes more."
            " Return the corn and zucchini to pan the and cook with the sauce for 2 minutes. "
            "Add basil and stir to combine.",
            
            "Add farro, water, and 1 more teaspoon of salt and stir to combine. If you need to transfer"
            " this to an ovenproof dish, do it now. Stir in diced mozzarella and half of parmesan. "
            "Sprinkle remaining parmesan on top, and cover with a lid or tightly with foil and bake "
            "for 30 to 40 minutes, until farro is cooked. Cooked farro should be tender but a little "
            "chewy. If the pan is dry and your farro still seems undercooked, add another 1/4 to 1/2 "
            "cup water and return it to the oven until it reaches the right texture.",
            
            "Transfer dish to your broiler, or to the hottest part of your oven (and crank the heat) and "
            "cook until browned and crisp on top, about 3 to 5 minutes under a broiler or 5 to 7 in the "
            "oven. Serve warm"
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
