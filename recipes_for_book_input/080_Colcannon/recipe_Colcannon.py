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
        r = MyRecipe('Colcannon', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('both', 'Colcannon_and_Gravy.jpeg')
        r.addPicture('Colcannon', 'colcannon_only.jpeg')
        r.setPrimaryPicture('Colcannon')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Potato', 2, 'pounds, russet')
        r.addIngredient('Leek', 2, 'large, whole')
        r.addIngredient('Savoy Cabbage', 0.5, 'head, finely shredded')
        r.addIngredient('Garlic', 3, 'cloves, minced')
        r.addIngredient('Unsalted Butter', 6, 'tablespoons')
        r.addIngredient('Half and Half', 1, 'cup')
        r.addIngredient('Salt', 2, 'teaspoons')
        r.addIngredient('Black Pepper', 1, 'teaspoon')

        
       
         
        # Add Steps and Notes
        steps= [
            'Boil potatoes in a large pot of water with a pinch of salt until '
            'tender, about 15 minutes. When cooked, a paring knife can be inserted '
            'into the centers and removed without resistance. Drain potatoes well and '
            'return to the hot pot. Let stand a few minutes to allow any remaining '
            'moisture to evaporate.',
            
            'While potatoes are boiling, melt 4 tablespoons butter in a large skillet '
            'until foaming subsides. Add cabbage and 1 teaspoon each kosher salt and black'
            ' pepper. Cook over medium-high heat, stirring frequently, until cabbage is just'
            ' starting to brown, 5 to 8 minutes.',
            
            'Add leeks and an additional 1/2 teaspoon of salt. Continue cooking, stirring often, '
            'until vegetables are tender, 5 to 8 minutes more. Add garlic, and cook for an additional '
            'minute. Stir in half and half, bring to a simmer, and remove from heat.',
            
            'Stir vegetables and half and half into the cooked potatoes. Use a potato masher to fully'
            ' combine and mash to desired consistency. Potatoes will thicken a bit as they stand. '
            'Season to taste with salt and pepper.',
            
            'To serve, mound potatoes into a serving bowl, and use a spoon to create a shallow well in '
            'the center. Melt the remaining 2 tablespoons of butter and drizzle it over the potatoes, '
            'allowing it to pool into the well. Scoop potatoes, catching some of the melted butter with '
            'each serving.'
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
