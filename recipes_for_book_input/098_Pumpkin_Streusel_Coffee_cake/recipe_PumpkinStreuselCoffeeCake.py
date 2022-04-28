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
        r = MyRecipe('Pumpkin Streusel Coffee Cake', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('slice_angled', 'IMG_2876.JPEG')
        r.addPicture('slice_top', 'IMG_2877.JPEG')
        r.addPicture('slice_side', 'IMG_2878.JPEG')
        r.setPrimaryPicture('slice_side')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        ## ---
        grpTopping = "Topping"
        r.addIngredient('Sugar', 131, 'grams (2/3 cup)', grpTopping)
        r.addIngredient('Salt', 1, 'pinch, to taste', grpTopping)
        r.addIngredient('All Purpose Flour', 80, 'grams (2/3 cup)', grpTopping)
        r.addIngredient('Cinnamon', 1, 'teaspoon', grpTopping)
        r.addIngredient('Pecans', 28, 'grams, (1/4 cup)', grpTopping)
        r.addIngredient('Unsalted Butter', 57, 'grams, 4 tablespoons')
        
        grpFilling = "Filling"
        r.addIngredient('Brown Sugar', 71, 'grams (1/3 cup)', grpFilling)
        r.addIngredient('Cinnamon', 1, 'teaspoon', grpTopping)
        
        grpCake = "Cake"
        r.addIngredient('Vegetable Oil', 67, 'grams (1/3 cup)', grpCake)
        r.addIngredient('Eggs', 2, 'large', grpCake)
        r.addIngredient('Sugar', 198, 'grams (1 cup)', grpCake)
        r.addIngredient('Pumpkin Puree', 198, 'grams', grpCake)
        r.addIngredient('Cinnamon', 0.5, 'teaspoon', grpCake)
        r.addIngredient('Ginger', 0.25, 'teaspoon', grpCake)
        r.addIngredient('Nutmeg', 0.25, 'teaspoon', grpCake)
        r.addIngredient('Salt', 1, 'teaspoon', grpCake)
        r.addIngredient('Baking Soda',2, 'teaspoon', grpCake)
        r.addIngredient('All Purpose Flour', 180, 'grams (1 1/2 cup)', grpCake)
            

        # Add Steps and Notes
        steps = [
            'Preheat the oven to 350 deg F.  Lightly grease an 8" square pan for 9" round pan.',
            
            'To make the topping: Whisk together the sugar, salt, flour, spice, and nuts. Add the '
            'melted butter, stirring just until well combined. Set the topping aside.',
            
            'To make the filling: Mix together the brown sugar, and spice. Set it aside.',
            
            'To make the cake: Beat together the oil, eggs, sugar, pumpkin, spices, salt, and baking '
            'powder until smooth.',
            'Add the flour, stirring just until smooth.',
            'Pour/spread half the batter into the prepared pan, spreading it all the way to the edges. '
            'If you have a scale, half the batter is about 13 1/2 ounces.',
            'Sprinkle the filling evenly atop the batter.',
            "Spread the remaining batter atop the filling. Use a table knife to gently swirl the filling "
            "into the batter, as though you were making a marble cake. Don't combine filling and batter "
            "thoroughly; just swirl the filling through the batter.",
            'Sprinkle the topping over the batter in the pan.',
            "Bake the cake until it's light brown on top, and a toothpick or cake tester inserted into the "
            "center comes out clean, about 40 to 45 minutes.",
            'Remove the cake from the oven and allow it to cool for 20 minutes before cutting and serving. '
            'Serve the cake right from the pan'
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
