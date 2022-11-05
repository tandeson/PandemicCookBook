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
        r = MyRecipe('Almond Cake', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('cakeSlice', 'IMG_3593.jpeg')
        r.addPicture('cakeFull', 'IMG_3592.jpeg')
        r.setPrimaryPicture('cakeSlice')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')  
        #  -- Add Ingredients --

        ##
        r.addIngredient('Almond Flour', 1.5, 'cups')
        r.addIngredient('Granulated White Sugar', 0.5, 'cups')
        r.addIngredient('Eggs', 4, 'medium, at room temperature')
        r.addIngredient('Lemon', 1, 'large, zest')
        r.addIngredient('Salt', 2, 'teaspoons')
          
        # Add Steps and Notes
        steps= [
            'Grease a 9" pan, prehead the oven to 350 deg F.',
            'In a large mixing bowl, combine 4 Eggs yokes with Sugar. Beat until thick.',
            'Add in Almond Flour and Lemon Zest. Mix well with a spatula.',
            'In a seperate bowl beat 4 Egg whites until stiff peaks form.',
            'Fold the whites into the flour mixture one large spoonful at a time.',
            'Mix until uniform - but try to do as little as possible. The air in the Eggs is what gives the cake its flufflyness',
            'Transfer batter into pan. Bake for 30 minutes, until top is firm.',
            'Let cake rest for 15 minutes in pan, then loosen with a knife around the edges before removing.'
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
