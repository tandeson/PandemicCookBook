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
        r = MyRecipe('Roast Garlic', "Appetizers", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('JustGarlic', '2020_09_09_RoastGarlic.jpg')
        r.addPicture('GarlicSnacks', '2020_09_09_RoastGarlicDone.jpg')
        r.setPrimaryPicture( 'JustGarlic')
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')
        
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Garlic', 4, 'heads')
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons')
           
        # Add Steps and Notes
        steps = [
            'cut off aproximaly the top 1/4 of the garlic head',
            'place each garlic head on a small square of alumnium foil',
            'drizzle olive oil over the top of the garlic heads',
            'wrap up each garlic head individually in the aluminum foil',
            'heat the oven to 375 deg F',
            'bake the garlic heads for at least 45 minutes', 
            'allow to cool, then squeeze out the garlic using your fingers.'
            ]
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        r.addStep( 
            RecipeStep( "Serve with chips! Goes well with cool Ranch Doritos." ),
            ['GarlicSnacks']
            )
        
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
