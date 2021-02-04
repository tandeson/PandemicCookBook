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
        r = MyRecipe('Sourdough Hamburger Bun', 'Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --
        
        r.addIngredient('Sourdough Starter', 170, 'grams')
        r.addIngredient('Water', 170, 'grams, lukewarm')
        r.addIngredient('Active Dry Yeast', 1, 'teaspoon')
        r.addIngredient('All Purpose Flour', 240, 'grams ( 2 cups)')
        r.addIngredient('Rye Flour', 28, 'grams (0.25 cups)')
        r.addIngredient('Potato Flour', 25, 'grams, 2 tablespoons')
        r.addIngredient('Bakers Special Dry Milk', 14, 'grams, 2 tablespoons')
        r.addIngredient('Salt', 1.5, 'teaspoons')
        r.addIngredient('Sugar', 1, 'tablespoon')
        r.addIngredient('Unsalted Butter', 57, 'grams, 4 tablespoons, soft')
           
        # Add Steps and Notes
        steps = [
            'In a large bowl, Combine the flours, dry milk, salt, yeast and sugar.',
            'Add in the starter and water. Mix well, until it\'s a sticky, cohesive dough.',
            'Add the butter, and kneed until the dough is smooth and elastic - 8 to 12 minutes.',
            'Cover the dough and let it rest in a warm place (75 deg F to 80 deg F) for about 2 hours. '
            'To de-gas and even out the temperature of the dough, stretch and fold it in the bowl two or'
            ' three times during the rest. You can be fairly flexible in your timing of these; one '
            'stretch and fold per hour is ideal.',
            'Turn the dough out onto a lightly floured work surface and divide it into six equal pieces; '
            'if you have a scale, each piece should weigh about 120 grams.',
            'Shape the dough pieces into tight balls and place them on a lightly greased or parchment-lined'
            ' baking sheet. Press the balls gently to flatten them slightly.', 
            'Cover the buns and let them rise until puffy, about 2 hours in a warm place.',
            'Twenty minutes before you\'re ready to bake, preheat the oven to 375 deg F.',
            'Bake the buns for 20 to 25 minutes, until golden brown.',
            'Remove the buns from the oven and allow them to cool before serving.'
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
