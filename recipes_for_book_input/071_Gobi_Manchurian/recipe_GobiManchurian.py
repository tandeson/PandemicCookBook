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
        r = MyRecipe('Gobi Manchurian', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('GobiManDish', '2021_02_15_GobiManchurian.jpg')
        r.setPrimaryPicture( 'GobiManDish' )
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')
        
        r.AddDescription('Thomas made this for my 38th birthday. It is a ton of work '
                         'but absoletuly delisious. ~Bilyana')
        ## ---
        
        grpCauliflower ="Fried Cauliflower"
        r.addIngredient('Cauliflower', 500, 'grams, ~1 head', grpCauliflower)
        r.addIngredient('All Purpose Flour', 0.5, 'cup', grpCauliflower)
        r.addIngredient('Corn Starch', 0.5, 'cup', grpCauliflower)
        r.addIngredient('Chili powder', 1.5, 'teaspoon', grpCauliflower)
        r.addIngredient('Black Pepper', 0.5, 'teaspoon, to taste', grpCauliflower)
        r.addIngredient('Salt', 0.5, 'teaspoon, to taste', grpCauliflower)
        r.addIngredient('Water', 1, 'cup', grpCauliflower)
        r.addIngredient('Vegetable Oil', 1, 'cup, at least', grpCauliflower)
        
        grpManchurianSauce = "Manchurian Sauce"
        r.addIngredient('Vegetable Oil', 3, 'tablespoons', grpManchurianSauce)
        r.addIngredient('Garlic', 4, 'cloves, minced', grpManchurianSauce)
        r.addIngredient('Ginger', 1, 'teaspoons, chopped', grpManchurianSauce)
        r.addIngredient('Green Chillies', 2, 'chopped', grpManchurianSauce)
        r.addIngredient('Onion', 1, 'cups, chopped', grpManchurianSauce)
        r.addIngredient('Red Bell Pepper', 0.5, 'cups, chopped', grpManchurianSauce)
        r.addIngredient('Soy Sauce', 2, 'tablespoon', grpManchurianSauce)
        r.addIngredient('Tomato Ketchup', 4, 'tablespoons', grpManchurianSauce)
        r.addIngredient('Red Chilli sauce', 1, 'teaspoon', grpManchurianSauce)
        r.addIngredient('Rice Vinegar', 1, 'tablespoon', grpManchurianSauce)
        r.addIngredient('Sugar', 2, 'teaspoons', grpManchurianSauce)
        r.addIngredient('Salt', 1, 'pinch, to taste', grpManchurianSauce)
        r.addIngredient('Black Pepper', 1, 'pinch, to taste', grpManchurianSauce)
        r.addIngredient('Water', 0.3, 'cup', grpManchurianSauce)

        # Add Steps and Notes
        r.addStep( 
            RecipeStep( "Prepare the Cauliflower",[
                RecipeStep('Cut the califlower head into medium sized florets.'),
                RecipeStep('Heat 4 cups of water in large pot, add florets when the water is getting close to boiling.'),
                RecipeStep('Turn off heat, let the florets sit in the hot water for 5 minutes.'),
                RecipeStep('Remove the florets and spread on a cloth or paper towel to dry. Let dry, if they are not dry, they will not be crispy when fried.')
                ] 
            )
        )
        r.addStep( RecipeStep( "Place the oil in deep pan, and heat to medium heat for deep frying." ))
        r.addStep( 
            RecipeStep( "Prepare the batter",[
                RecipeStep('Add corn Starch, flour, chilli powder, black pepper and salt in a mixing bowl.'),
                RecipeStep('Mix, and add water little by little as needed. Make a free flowing lump free batter.'),
                RecipeStep('NOTE: the mix should be between a paste and crepe batter.'),
                ]
            )
        )
        r.addStep(
            RecipeStep(
                'Using a spoon, Dip florets in batter to coat and place in the oil. Do this until there is a single layer'
                ' in the pan. If not covered in oil, flip half way though frying. Fry until crispy, then remove and place '
                'on paper towel. Repeat until all the cauliflower is cooked.' ))
        
        r.addStep(
            RecipeStep("Make the Manchurian Sauce", [ 
                RecipeStep('Heat oil on medium in wide pan large enough to hold all the fried caulifower and a sauce.'),
                RecipeStep('Add in the garlic, ginger and green chilies. Saute for 1 - 2 minutes.'),
                RecipeStep('Raise the heat to high, add onions and bell pepper. Saute for 2 minutes.'),
                RecipeStep('Reduce heat to medium. Add in Soy sauce, red chili sauce, ketchup, chili paste, sugar, vinegar and water. Mix and cook stiring until sauce thickens.'),
                RecipeStep('Remove from heat and let cool for 1 - 2 minutes.'),
            ]
            )
        )
        
        r.addStep(
            RecipeStep('Add in the Fried cauliflower to the sauce, and stir gently to coat.')
            )
        
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
