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
        r = MyRecipe('Pastry Cream', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        
        #  -- Add Ingredients --
        r.AddDescription("This is from the Eclaire class at King Arthur.")
        ## 
        #--
        r.addIngredient('Whole Milk', 947, 'grams, 4 cups')
        r.addIngredient('Granulated White Sugar', 200, 'grams, 1 cup')
        r.addIngredient('Corn Starch', 71, 'grams, 3/4 cup')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Eggs', 1, 'large')
        r.addIngredient('Eggs Yolks', 4, '')
        r.addIngredient('Unsalted Butter', 19, 'grams, 1.3 tablespoons - room temperature')
        r.addIngredient('Vanilla', 2, 'teaspoons')
        
        # Add Steps and Notes
        steps = [
            'This recipe goes fast - be sure to read all the steps and measure out the ingredents before starting.',
            'Place the milk and half the sugar in a saucepan and bring to a boil. Do not stir while heating.',
            'In a bowl, whisk together the remaining sugar, constarch, and salt.'
            'Add the egg and yolks, wisking until very smooth.',
            'Temper the egg mixture with the milk and return to the saucepan. Bring the mixture back to a boil, whisking constantly.'
            ' Boil for 1 minute. Remove from the heat.',
            'Stir in the butter and vanilla extract. If you are using different flavor, this is the time to use that instead.',
            'Cover with plastic wrap directly on the surface and chill until cold and set. Pastry cream may be stored covered in'
            ' the refrigerator up to four days. Freezing is not recommend.',
            'Stir pastry cream before using, then transfer to a piping bag.'
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
