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
        r = MyRecipe('West African Peanut Soup', 'Soups', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('SoupPot', '2020_09_30_Peanut_soup.jpg')
        r.addPicture('SoupBowl', 'IMG_2370.jpeg')
        r.setPrimaryPicture('SoupBowl')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Vegetable Broth', 4, 'cups')
        r.addIngredient('Water', 2, 'cups')
        r.addIngredient('Red Onion', 1, 'medium, chopped')
        r.addIngredient('Ginger', 2 , 'tablespoons, minced')
        r.addIngredient('Garlic', 4, 'cloves, chopped')
        r.addIngredient('Salt', 1, 'teaspoon')
        r.addIngredient('Collard Greens', 1, 'bunch (or Kale)')
        r.addIngredient('Peanut Butter', 0.75, 'cups unsalted')
        r.addIngredient('Tomato Paste', 0.5 , 'cups')
        r.addIngredient('Sriracha', 1, 'squrit, to taste, ')
        r.addIngredient('Peanuts', 0.25, 'cups, chopped')
        r.addIngredient('Sweet Potatoes', 1, 'chopped')
           
        # Add Steps and Notes
        steps= [
            'Combine the broth and water in a medium pot.',
            'Bring to boil, then add the Red Onion, Ginger, Garlic, Salt and Sweet Potato.',
            'Cook on medium-low heat for 20 minutes.',
            'In a medium-sized heat-safe mixing bowl, combine the Peanut Butter and Tomato Paste.',
            'Transfer 1 - 2 cups of the hot stock to the bowl. Whisk until smooth, then pour back '
            'into the soup and mix well.',
            'Stir in Collard Greens and season the soup with Hot Sauce to taste.',
            'Simmer for 15 minutes on medium-low heat, stirring often.',
            'Season with additional salt or Hot Sauce if desired.',
            'Serve with a sprinkle of chopped Peanuts. Goes well over Quinoa or Brown Rice.'
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
