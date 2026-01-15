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
        r = MyRecipe('Snickerdoodle Cake', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS') 
        #  -- Add Ingredients --
        
        ## 
        #--
        grpCakeDry = 'Cake - dry'
        r.addIngredient('All Purpose Flour', 1.5 , 'cups', grpCakeDry)
        r.addIngredient('Granulated White Sugar', 0.5, 'cups', grpCakeDry)
        r.addIngredient('Brown Sugar', 0.5, 'cups', grpCakeDry )
        r.addIngredient('Cinnamon', 2.5, 'teaspoons, ground', grpCakeDry)
        r.addIngredient('Baking Soda', 1, 'teaspoon', grpCakeDry)
        r.addIngredient('Cream of Tartar', 0.5, 'teaspoon', grpCakeDry)
        r.addIngredient('Salt', 0.5, 'teaspoon', grpCakeDry)
        
        grpCakeWet = 'Cake - wet'
        r.addIngredient('Extra Virgin Olive Oil', 5, 'tablespoons', grpCakeWet)
        r.addIngredient('Vanilla', 2, 'teaspoons', grpCakeWet)
        r.addIngredient('Apple Cider Vinegar', 1, 'teaspoon', grpCakeWet)
        r.addIngredient('Water', 1, 'cup', grpCakeWet)
        
        grpTopping = 'Topping'
        r.addIngredient('Granulated White Sugar', 1, 'tablespoon', grpTopping)
        r.addIngredient('Cinnamon', 1, 'teaspoons, ground', grpTopping)
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 350 deg F.  Spray an 8"x 8" baking dish with non-stick cooking spray.',
            
            'Mix dry ingredients (flour, sugar, brown sugar, cinnamon, baking soda, cream of tartar and salt) '
            ' in prepared baking dish until well blended.',  
            
            'Next, make 3 depressions in dry ingredients – two small, one larger. Add the vinegar in one depression, '
            'vanilla in the other and the vegetable oil in the third larger depression.',
            
            'Pour water over all. Mix well until smooth.',
            'Bake on middle rack of oven for approximately 35 minutes.',
            'While the cake is baking, mix the cinnamon and sugar for the topping.',
            
            'Check center of cake with toothpick to make sure it comes out clean. While the cake is still warm fresh out '
            'of the oven, sprinkle cinnamon sugar evenly over top.',
            
            'Allow to cool,  enjoy!'
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
