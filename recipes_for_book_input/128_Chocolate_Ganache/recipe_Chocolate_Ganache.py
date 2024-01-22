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
        r = MyRecipe('Chocolate Ganache', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        
        #  -- Add Ingredients --
        r.AddDescription("This makes a lot (about 2 cups) - consider scaling down depending on what you are making."
                  " It's from the Eclaire class at King Arthur.")
        ## 
        #--
        r.addIngredient('Dark Chocolate chips', 227, 'grams, 1 1/3 cups')
        r.addIngredient('Honey', 1, 'teaspoon')
        r.addIngredient('Heavy Cream', 237, 'grams, 1 cup')
        r.addIngredient('Unsalted Butter', 7, 'grams, 1.5 teaspoons - room temperature')

        # Add Steps and Notes
        steps = [
            'Put the chocolate in a bowl and set aside.',
            'Heat the Honey and Cream in a saucepan until boling. Remove from heat and pour'
            ' over the chocolate. Allow this to sit for 30 seconds.',
            'Stir with a whisk ( or a immersion blender ), starting in the center of the bowl.'
            ' Stay in the middle until the mixture starts to combine, then move out to the rest of the bowl.',
            'Stir until all chocolate has melted. Add in the butter and stir to combine.',
            'Ganache is now ready to use as a glaze - or it can be stored in the refrigerator (3 weeks) or frozen ( 3 months).'
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
