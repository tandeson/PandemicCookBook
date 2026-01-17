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
        r = MyRecipe('Apple Pancakes',"Baking and Breads", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Apple_Pancake', '2020_09_12_ApplePancakes.jpg')
        r.setPrimaryPicture( 'Apple_Pancake' )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --

        ##
        r.addIngredient('Eggs', 2, 'large')
        r.addIngredient('Whole Milk', 283, 'grams (1 1/4 cup)')
        r.addIngredient('Vanilla', 1 , 'teaspoon')
        r.addIngredient('Salted Butter', 43, 'grams (3 tsp)')
        
        r.addIngredient('All Purpose Flour', 184, 'grams ( 1.5 cups)')
        r.addIngredient('Salt', 0.75, 'teaspoon')
        r.addIngredient('Baking Powder', 2, 'teaspoons')
        r.addIngredient('Granulated White Sugar', 2, 'teaspoons')    
        r.addIngredient('Cinnamon', 2, 'tablespoons, ground')
         
        r.addIngredient('Apples', 4, 'large')
           
        # Add Steps and Notes
        steps = [
            'Beat the eggs, vanilla, and milk until light and foamy, about 3 minutes at high speed with a stand or hand mixer.',
            'Stir in the butter or vegetable oil.',
            'Whisk the dry ingredients together to evenly distribute the salt, baking powder, cinnamon and sweetener.',
            'Gently and quickly mix into the egg and milk mixture. Let the batter rest for at least 15 minutes, '
            'while the griddle is heating; it\'ll thicken slightly.',
            'Chop the Apples into small chunks - I prefer Honeycrisp Apples for this. Mix into the batter.',
            'Heat a heavy frying pan over medium heat, lightly grease the frying pan or griddle. The pan or griddle is '
            'ready if a drop of water will skitter across the surface, evaporating immediately.',
            'Drop 1/4 cupfuls of batter onto the lightly greased griddle. Bake on one side until bubbles begin to '
            'form and break, about 2 minutes; then turn the pancakes and cook the other side until brown, about '
            '1 1/2 to 2 minutes.',
            'Turn over only once. Serve immediately.'
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
