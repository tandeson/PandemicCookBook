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
        r = MyRecipe('Sourdough Focaccia', 'Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('decorated_focaccia', '2020_09_15_Focaccia_baked_decorated.jpeg')
        r.setPrimaryPicture( 'decorated_focaccia' )
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Bread Flour', 723, 'grams (6 cups)')
        r.addIngredient('Salt', 1, 'tablespoon')
        r.addIngredient('Active Dry Yeast', 1, 'tablespoon')
        r.addIngredient('Extra Virgin Olive Oil', 74, 'grams, 6 tablespoons')
        r.addIngredient('Sourdough Starter', 340, 'grams, fed (1.5 cups)')
        r.addIngredient('Water', 340 , 'grams (1.5 cups)')
        r.addIngredient('Honey', 43, 'grams, 2 tablespoons')
        r.addIngredient('Rosemary', 1, 'tablespoon')
        
        # Add Steps and Notes
        r.addStep( RecipeStep( 
            'Mix together the Flour, Salt and Yeast. Mix until combined.',
            ))
        
        r.addStep( RecipeStep( 
            'Add in the Water, Sourdough Starter, Olive Oil and Honey.',
            ))
        
        r.addStep( RecipeStep( 
            "Mix the dough until it's smooth and elastic.",
            ))
        
        r.addStep( RecipeStep( 
            'Place the dough in bowl lightly coated with Olive Oil and let rise for 60 minutes.',
            ))
        
        r.addStep( RecipeStep( 
            'Fold the dough 3 or 4 times and then let it rest for another 60 minutes.',
            ))
        
        r.addStep( RecipeStep( 
            'In two 9x13 baking pans, place 2 tablespoon of oil and then place 1/2 of the dough in each.',
            ))
        
        r.addStep( RecipeStep( 
            'Turn the dough over to ensure it\'s coated on both sides with the Olive Oil.',
            ))
        
        r.addStep( RecipeStep( 
            'Gently stretch the dough into the edges and corners of the pan. As soon as the dough begins to shrink'
            ' back, cover it, and let it rest for 10 to 15 minutes. Gently stretch the dough again, repeating the '
            'rest once more, if necessary, until the dough fills the pan.'
            ))
        
        r.addStep( RecipeStep(
            'Cover the pan and transfer it to the refrigerator to let the dough rise for 14 to 16 hours (overnight).'
            ))
        
        r.addStep( RecipeStep(
            'The next day, remove the pan of dough from the refrigerator and preheat the oven to 425 deg F for 30 '
            'minutes (if your kitchen is warm) to 60 minutes (in a cooler kitchen).'
            ))
        
        r.addStep( RecipeStep(
            'Just before you\'re ready to bake, gently dimple the dough at irregular intervals with your fingers, '
            'pressing down firmly but not abruptly; you don\'t want to deflate the focaccia too much. Decorate the dough '
            'with Parsley, Radishes or other vegetables.'
            ))
        
        r.addStep( RecipeStep(
            'Drizzle 2 tablespoons olive oil (or enough to collect a bit in the dimples), then sprinkle with rosemary and a'
            ' bit of flaked sea salt.'
            ))
        
        r.addStep( RecipeStep(
            'Bake the focaccia for 20 to 25 minutes, until light golden brown.'
            ))
        
        r.addStep( RecipeStep(
            'Remove the focaccia from the oven. Allow it to cool enough for you to handle it comfortably, 10 to 15 minutes, '
            'then turn it out of the pan onto a rack.'
            ))
        
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
