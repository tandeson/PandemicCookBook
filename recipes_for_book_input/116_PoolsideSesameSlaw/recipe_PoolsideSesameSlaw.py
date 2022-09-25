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
        r = MyRecipe('Poolside Sesame Slaw', 'Salads', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --
        
        ## Makes about 2 dozen?
        #--
        
        grpDressing = "Miso-Sesame Dressing"
        r.addIngredient('Ginger', 1, 'tablespoon, minced', grpDressing)
        r.addIngredient('Garlic', 3, 'cloves, minced', grpDressing)
        r.addIngredient('Tahini', 2, 'tablespoons, well-stirred', grpDressing)
        r.addIngredient('Miso Paste', 2, 'tablespoons', grpDressing)
        r.addIngredient('Honey', 1, 'tablespoon', grpDressing)
        r.addIngredient('Rice Vinegar', 0.25, 'cups', grpDressing)
        r.addIngredient('Sesame Oil', 2, 'tablespoon', grpDressing)
        r.addIngredient('Vegetable Oil', 2, 'tablespoons (or other neutral oil)', grpDressing)
        
        grpSlaw = 'Slaw'
        r.addIngredient('Carrot', 1, 'cup, shredded',grpSlaw)
        r.addIngredient('Cucumber', 0.75, 'cups, thin sliced', grpSlaw)
        r.addIngredient('Celery', 0.75, 'cups, thin sliced', grpSlaw)
        r.addIngredient('Red Bell Pepper', 0.75, 'seeded and thin sliced', grpSlaw)
        r.addIngredient('Sugar Snaps', 0.75, 'cups', grpSlaw)
        r.addIngredient('Savoy Cabbage', 2, 'cups, thin slicked', grpSlaw)
        r.addIngredient('Peanuts', 1, 'cup, salted', grpSlaw)
        r.addIngredient('Green Onion', 1, 'cup, thin sliced', grpSlaw)
        r.addIngredient('Cilantro', 1, 'handful, chopped', grpSlaw)
        r.addIngredient('Fried Tofu', 1, 'package', grpSlaw)
        
        # Add Steps and Notes
        r.addStep( RecipeStep( 'Make the dressing', [
            RecipeStep('Combine all dressing ingredients in a blender and run until smooth, scraping down sides once.'),
            RecipeStep('Taste and adjust ingredients to your preference.'),
            ]))
        
        r.addStep( RecipeStep( 'Assemble the salad', [
            RecipeStep('Holding back a little of the peanuts, green onions, and herbs for garnish, add all ingredients to a large bowl and toss with half of the dressing.'),
            RecipeStep('Add in some or all of the remaining dressing, to taste.'),
            RecipeStep('Season with salt and pepper, if needed.'),
            RecipeStep('Sprinkle with reserved peanuts, green onions, and herbs for extra prettiness.'),
            ]))
        
        r.addStep( RecipeStep( 'Eat right away or bring it somewhere wonderful in a cooler and eat it in a few hours.' ))
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
