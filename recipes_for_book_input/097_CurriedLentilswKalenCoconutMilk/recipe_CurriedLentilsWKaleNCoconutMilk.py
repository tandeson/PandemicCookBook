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
        r = MyRecipe('Curried Lentils with Kale (Masoor Dal)', 'Soups', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('CurriedLentis_1', 'CurriedLentils_1.JPEG')
        r.addPicture('CurriedLentis_2', 'CurriedLentils_2.JPEG')
        r.setPrimaryPicture('CurriedLentis_2')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --
        
        ## Makes about 2 dozen?
        #--
        
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
        r.addIngredient('Onion', 1, 'medium, chopped')
        r.addIngredient('Garlic', 4, 'cloves, diced')
        r.addIngredient('Salt', 1, 'pinch, to taste')
        r.addIngredient('Ginger', 1, 'tablespoon, finely grated')
        r.addIngredient('Black Mustard Seeds', 2, 'teaspoons')
        r.addIngredient('Turmeric', 2, 'teaspoon')
        r.addIngredient('Coriander Powder', 1, 'teaspoon')
        r.addIngredient('Cumin', 1, 'teaspoon')
        r.addIngredient('Red Pepper Flakes', 0.5, 'teaspoon')
        r.addIngredient('Water', 3.5, 'cups')
        r.addIngredient('Coconut Milk', 1, 'Can, about 14 oz')
        r.addIngredient('Red Lentils', 0.5, 'cup, dry')
        r.addIngredient('Green Lentils', 0.5, 'cup, dry')
        r.addIngredient('Kale', 6, 'oz, 1 bunch chopped no stem')

        #- 2 green chillies, chopped ( or red chilli powder - to taste )
        
        # Add Steps and Notes
        steps = [
            'In a large pot over medium-high, combine the oil, onion, garlic and '
            '1 teaspoon salt. When you hear a sizzle, cover the pot, turn heat to '
            'low, and cook, stirring every so often, until the onion has softened and '
            'is just beginning to color, 7 to 9 minutes.',
            
            'Stir in the ginger, the mustard '
            'seeds, turmeric, coriander, fennel and red pepper flakes. Cook, stirring '
            'often, until fragrant, about 1 minute.',
            
            'Add the water, coconut milk, lentils, '
            'and remaining 1/2 teaspoon salt, then bring to a boil. Reduce to low, cover and '
            'simmer, stirring once or twice, until the lentils have broken down, 40 to 50 minutes.',
            
            'Stir in the kale and return to a simmer. Taste and season with salt if desired. Serve '
            'immediately or cool and refrigerate for a future day - it\'s good cold straight from the fridge.',
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
