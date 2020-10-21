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
        r = MyRecipe('Thai Quinona Salad', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('ThaiSalad', '2020_10_02_ThaiQuinoaSalad.jpg')
        r.setPrimaryPicture('ThaiSalad')
        
        #  -- Add Ingredients --

        ##
        grpSaladIngred = "For the salad"
        r.addIngredient('Quinoa', 2, 'cup, cooked', grpSaladIngred)
        r.addIngredient('Red Cabbage', 2, 'cups, shredded', grpSaladIngred)
        r.addIngredient('Red Bell Pepper', 1, 'diced', grpSaladIngred)
        r.addIngredient('Red Onion', 0.25, 'cup, diced', grpSaladIngred)
        r.addIngredient('Carrot', 1, 'cup, shredded', grpSaladIngred)
        r.addIngredient('Cilantro', 0.5, 'cup, chopped', grpSaladIngred)
        r.addIngredient('Green Onion', 0.25, 'cup, diced', grpSaladIngred)
        r.addIngredient('Cashews', 0.5, 'cup, halves (or Peanuts)', grpSaladIngred)
        r.addIngredient('Chickpeas', 1, 'cup (or Edamame)', grpSaladIngred)
        r.addIngredient('Lime', 1, 'squeeze', grpSaladIngred)
        
        grpDressing = 'For the dressing'
        r.addIngredient('Peanut Butter', 0.25, 'cup', grpDressing)
        r.addIngredient('Ginger', 2, 'teaspoons, grated', grpDressing)
        r.addIngredient('Soy Sauce', 3, 'tablespoons', grpDressing)
        r.addIngredient('Honey', 1, 'tablespoon', grpDressing)
        r.addIngredient('Rice Vinegar', 1, 'tablespoon or Red Wine Vinegar', grpDressing)
        r.addIngredient('Sesame Oil', 1, 'teaspoon', grpDressing)
        r.addIngredient('Extra Virgin Olive Oil', 1, 'teaspoon', grpDressing)
        
        # Add Steps and Notes
        r.addStep( RecipeStep( 'Make the dressing.', [ 
                RecipeStep( 'Add peanut butter and honey to a medium microwave safe bowl; heat in microwave for 20 seconds.' ),
                RecipeStep( 'Add in ginger, soy sauce, vinegar, and both sesame and olive oil and stir until mixture is smooth and creamy.'),
                RecipeStep('If you want a thinner dressing, simply stir in a teaspoon or two of water or olive oil.'),
            ]))
        
        r.addStep(RecipeStep('Add as much or as little dressing as you\'d like to the quinoa.'))
        r.addStep(RecipeStep('Fold in red pepper, onion, cabbage, carrots, and cilantro into the quinoa.'))
        r.addStep(RecipeStep('Garnish with cashews and green onions. Serve chilled or at room temperature with lime wedges, if desired.'))
        
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
