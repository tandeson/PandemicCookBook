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
        r = MyRecipe('Pistachio Apricot Bars', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        
        #  -- Add Ingredients --
        
        ## 
        #--
        r.addIngredient('Unsalted Butter', 1, 'cup, (2 sticks)')
        r.addIngredient('Granulated White Sugar', 1, 'cup')
        r.addIngredient('Eggs', 1, 'medium')
        r.addIngredient('Vanilla', 1, 'teaspoon')
        r.addIngredient('All Purpose Flour', 2.5, 'cups')
        r.addIngredient('Pistachios', 0.5, 'cups, chopped')
        r.addIngredient('Apricot Preserves', 1, 'jar, 12-18 oz')
        
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 350 deg F.',
            'In a bowl, cream butter and sugar.',
            'Beat in egg and vanilla.',
            'Gradually mix in the flour.',
            'Stir in Pistachios.',
            'Press mixture into a greased 9x13 baking dish.',
            'spread with preserve.',
            'bake for 25 - 30 minutes.',
            'Cool on a wire rack, and then cut into bars.',
            'Garnish with Pistachios, if desired.'
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
