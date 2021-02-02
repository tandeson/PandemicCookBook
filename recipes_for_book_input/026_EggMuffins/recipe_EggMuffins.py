#!/usr/bin/env python
#*****************************************************************************
"""
    Make A recipe
"""
#*****************************************************************************

#*  Imports ******************************************************************
import sys
import os 

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
        r = MyRecipe('Egg Muffins', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture(
            'muffins_on_plate', 
            os.path.join('2020_10_4_EggMuffinPic','IMG_1296.JPEG')
            )
        r.setPrimaryPicture('muffins_on_plate')
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Mushrooms', 4, 'oz')
        r.addIngredient('Green Onion', 1 , 'bunch, chopped')
        r.addIngredient('Extra Virgin Olive Oil', 0.25, 'cups' )
        r.addIngredient('All Purpose Flour', 0.25, 'cups' )
        r.addIngredient('Baking Powder', 0.5, 'teaspoon')
        r.addIngredient('Salt', 0.25, 'teaspoon')
        r.addIngredient('Shredded Mexican Cheese', 2, 'cups, anything sharp')
        r.addIngredient('Cottage Cheese', 1, 'cup')                
        
        # Add Steps and Notes
        steps= [
            'Saute mushroom and onions in 1 tablespoon olive oil until tender',
            'In a bowl, combine flour, baking powder and salt',
            'In another bowl combined eggs, cheese and 1/4 cup olive oil',
            'Combine all ingredients into one bowl, and mix',
            'Fill greased muffin cups',
            'Bake at 350 deg F for 35 minutes'
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
