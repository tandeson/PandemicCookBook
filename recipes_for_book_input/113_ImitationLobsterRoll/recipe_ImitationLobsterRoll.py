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
        r = MyRecipe('Imitation Lobster Roll', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)        
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        ## ---
        grpLobsterBase = 'Immitation Lobster'
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoons', grpLobsterBase)
        r.addIngredient('Old Bay Seasoning', 1, 'tablespoon',grpLobsterBase)
        r.addIngredient('Lemon Juice', 1, 'tablespoon',grpLobsterBase)
        r.addIngredient('Garlic', 3, 'cloves, minced',grpLobsterBase)
        r.addIngredient('Heart of Palm', 2, '14 oz cans, drained and chopped',grpLobsterBase)
        
        grpCreamyDressing = 'Creamy Dressing'
        r.addIngredient('Mayonnaise', 0.75, 'cups', grpCreamyDressing)
        r.addIngredient('Lemon Juice', 3, 'tablespoon',grpCreamyDressing)
        r.addIngredient('Celery', 2, 'stalks, finely chopped',grpCreamyDressing)
        r.addIngredient('Red Onion', 1, 'small, finely diced',grpCreamyDressing)
        r.addIngredient('Dill', 1.5, 'tablespoon',grpCreamyDressing)
        r.addIngredient('Unsalted Butter', 2, 'Tablespoons, melted'), grpCreamyDressing

        ## Steps
        steps = [
            'In a bowl, mix olive oil, Old Bay Seasoning, lemon juice and minced garlic. '
            'Add to bowl of chopped hearts of palm and marinate for as long as you can, '
            'overnight is best.',
            
            'To make the vegan creamy dressing, whisk the vegan mayonnaise and lemon juice '
            'in a bowl. Add chopped celery, red onion and dill. Whisk until well combined. '
            'Feel free to put the dressing in the fridge to firm up until you want to heat '
            'up your marinated hearts of palm.',
            
            'When you\'re ready to eat your lobster roll and the hearts of palm have had time '
            'to marinate, heat a non-stick pan over medium-high heat. Add the hearts of palm '
            'and marinade and saute for 5-8 minutes, stirring occasionally. Cook until slightly '
            'brown on all sides. Set aside to cool.',
            
            'Add the cooked marinated hearts of palm “lobster” with the chilled dressing to coat.',
            
            'Serve in a soft roll, wrap or just eat it as a salad.'
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
