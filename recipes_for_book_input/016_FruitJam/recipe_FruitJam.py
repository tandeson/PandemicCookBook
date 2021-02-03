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
        r = MyRecipe('Fruit Jam','Spreads and Dips', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('JamOnBread', '2020_09_14_BlueberryJam.JPG')
        r.setPrimaryPicture( 'JamOnBread')
        r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS')
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Sugar', 1, 'cup')
        r.addIngredient('Blueberries', 4, 'cups')
        
        # Add Steps and Notes
        steps = [
            'Note: The important part of this Recipe is the ratio, feel free to '
            ' scale it up or down.',
            'Cut the berries into large chunks, discarding any heavily bruised sections.',
            'Place the fruit and sugar in a 2 to 3 quart heavy-bottomed saucepan over medium'
            ' heat and mash the fruit a little with a potato masher or large fork into a chunky'
            ' texture',
            'Bring the mixture up to a boil, stirring frequently. Continue to boil while keeping'
            ' an eye on it, still stirring frequently, until the fruit is jammy and thick, about'
            ' 20 minutes.',
            'Turn off the heat and carefully transfer the jam into 2 clean (8-ounce) glass jars.',
            'Bring a large pot full of water to a full boil. Place the Jam Jars in the water, and '
            'wait for 10 minutes.',
            'Remove and cool. The Jam should be good for up to 2 years.'
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
