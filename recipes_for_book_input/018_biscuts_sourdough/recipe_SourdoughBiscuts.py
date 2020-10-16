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
        r = MyRecipe('Sourdough Biscuts', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('SourdoughBiscuts', '2020_05_06_biscutsBaked.jpeg')
        r.setPrimaryPicture( 'SourdoughBiscuts')
        
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('All Purpose Flour', 120, 'grams ( 1 cups)')
        r.addIngredient('Baking Powder', 2, 'teaspoons')
        r.addIngredient('Salt', 0.75, 'teaspoons')
        r.addIngredient('Unsalted Butter', 8, 'tablespoons (113 grams) cold')
        r.addIngredient('Sourdough Starter', 227, 'grams (1 cup)')
        
               
        # Add Steps and Notes
        steps = [
            'Preheat the oven to 425 deg F with a rack in the upper third. Line a baking sheet with parchment.',
            'Combine the Flour, Baking Powder and Salt. Work the butter into the flour until the mixture is unevenly crumbly.',
            'Add the starter, mixing gently until the dough is cohesive.',
            'Turn the dough out onto a lightly floured surface (a piece of parchment works well) and gently pat it into a 6" '
            'round about 1" thick.',
            'Use a cup or biscuit cutter to cut 4 - 6 rounds, cutting them as close to one another as possible. Mix the scraps'
            ' together and cut again to get about 8 rounds. ',
            'Place the biscuits onto the prepared baking sheet, leaving about 2" between them; they\'ll spread as they bake.',
            'Bake the biscuits in the upper third of your oven for 20 - 23 minutes, until they\'re golden brown.',
            'Remove the biscuits from the oven and serve warm.'
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
