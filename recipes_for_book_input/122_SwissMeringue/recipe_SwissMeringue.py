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
        r = MyRecipe('Swiss Meringue', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('PipedMeringue', 'IMG_3786.jpeg')
        r.setPrimaryPicture('PipedMeringue')
        #  -- Add Ingredients --
        
        ## 
        #--
        r.addIngredient('Eggs Whites', 100, 'grams, about 2 eggs worth')
        r.addIngredient('Powdered Sugar', 200, 'grams')
        r.addIngredient('Vanilla', 2, 'teaspoons')

        # Add Steps and Notes
        steps = [
            'Place the egg whites and powdered sugar in the bowl of a stand mixer. Place over a water '
            'bath and bring the mixture to 140 deg F, whisking constantly.',
            
            'Remove from the heat and place in the stand mixer. Using a whisk attachment beat the meringue '
            'until it has completely cooled down, it is smooth and shiny and holds stiff peaks.',
            
            'Add Vanilla and mix (or - subsitude your own flavor).',
            
            'Pre-heat the oven to 210 deg F. Transfer the Swiss meringue to a piping bag with a number 10 piping tip. '
            'Place a parchment paper on the baking tray and pipe out small meringues. Make sure that the meringues are '
            'staggered so that air circulates as they bake.',
            
            'Place the meringue cookies in the oven and bake for about 45 minutes. This will leave them crispy on the '
            'outside and soft inside. For fully baked - go about 2 hours. When done, turn off the oven and let them sit '
            'inside until the oven has completely cooled off.'
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
