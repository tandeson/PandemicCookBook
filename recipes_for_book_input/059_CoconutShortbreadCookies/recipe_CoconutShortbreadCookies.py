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
        r = MyRecipe('Coconut Shortbread Cookies', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')  
        
        r.AddDescription(
           'Early in our dating, I found out that Bilyana likes coconut. I made '
           'these as a present for one of our dates. ~ Thomas'
        )
        #  -- Add Ingredients --
        
        ##
        #--
        r.addIngredient('Coconut Flour', 32, 'grams (1/4 cup)')
        r.addIngredient('All Purpose Flour', 39, 'grams (1/4 cup)')
        r.addIngredient('Granulated White Sugar', 50, 'grams (1/4 cup)')
        r.addIngredient('Unsalted Butter', 57, 'grams (4 tablespoons) soft')
        r.addIngredient('Salt', 0.25, 'teaspoon')
        r.addIngredient('Eggs', 1, 'large')
        
        
        # Add Steps and Notes
        steps = [
            'Pre-heat the oven to 400 deg F.',
            'Lightly grease a baking sheet, or line it with parchment.',
            'Mix all the dough ingredients, by hand or mixer, until a '
            'well-blended, cohesive dough forms.',
            'Scoop the dough by the tablespoon and pat into rounds 1/2" '
            'thick. Place the cookies on the prepared baking sheet, spacing them 1" apart.',
            'Bake for 10 to 14 minutes, until just browned on the bottom.',
            'Remove from the oven and let cool completely on the baking sheet.'
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
