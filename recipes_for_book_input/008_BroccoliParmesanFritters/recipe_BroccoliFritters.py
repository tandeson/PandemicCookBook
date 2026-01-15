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
        r = MyRecipe('Broccoli Parmesan Fritters',"Main dishes", sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('FrittersFrying', 'FrittersCooking.jpg')
        r.setPrimaryPicture('FrittersFrying')
        #  -- Add Ingredients --
        
        ## Yields about 9 
        
        ## --
        grpFritters = "Fritters"
        r.addIngredient('Broccoli', 3, 'cups, chopped', grpFritters)
        r.addIngredient('Eggs', 1, 'large', grpFritters)
        r.addIngredient('All Purpose Flour', 0.5, 'cups', grpFritters)
        r.addIngredient('Parmesan Cheese', 65, 'grams, grated', grpFritters)
        r.addIngredient('Garlic', 2, 'cloves, minced', grpFritters)
        r.addIngredient('Salt', 0.5, 'teaspoon', grpFritters)
        
        grpOptional = "Optional (pick one)"
        r.addIngredient('Red Pepper Flakes', 1, 'pinch',grpOptional)
        r.addIngredient('Black Pepper', 1, 'pinch',grpOptional)
        
        grpForFrying = "For Frying"
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoon', grpForFrying)
        
        r.addStep( 
            RecipeStep( 'Prepare your broccoli',
                [
                    RecipeStep('Separate the florets from the biggest stem(s)'),
                    RecipeStep(' Cut the florets into 1-inch chunks.'),
                    RecipeStep('To prepare the stems, peel them, as the skin'
                               ' can be thick and doesn\'t cook quickly, then slice them'
                               ' into 1/2-inch lengths.'),
                    RecipeStep('Steam your broccoli until tender but not mushy'),
                    RecipeStep('bring a 1/2-inch or so of water to a boil in a small saucepan,'
                               ' then add the broccoli, place a lid on it and simmer it for 5 '
                               'to 6 minutes'
                               ),
                    RecipeStep('Drain the broccoli, then set it aside to cool slightly.'),
                ]
                )
            )
        
        r.addStep( 
            RecipeStep('Make the Fritters',
            [
                RecipeStep('In the bottom of a large bowl, lightly beat your egg.'
                           'Add the flour, cheese, garlic, salt and pepper. Then add '
                           'the somewhat cooled broccoli and mash with a fork.'),
                RecipeStep('keep the bits recognizable, but small enough (1/4- to '
                           '1/2-inch chunks) that you can press a mound of the batter'
                           ' into a fritter in the pan.'),
                RecipeStep('Once mashed a bit, stir or fold the ingredients together '
                           'the rest of the way with a spoon. Adjust seasonings to taste.'),
                RecipeStep('Heat a large, heavy skillet over moderate heat.'),
                RecipeStep('Once hot, add oil about 2 to 3 tablespoons.'),
                RecipeStep('Once the oil is hot scoop a two tablespoon-size mound '
                           'of the batter and drop it into the pan, then flatten it'
                           ' slightly with your spoon or spatula.'),
                RecipeStep('Repeat with additional batter, leaving a couple inches'
                           ' between each.'),
                RecipeStep('Once brown underneath, about 2 to 3 minutes, flip each'
                           ' fritter and cook on the other side until equally '
                           'golden, about another 1 to 2 minutes.'),
                RecipeStep('Transfer briefly to paper towels to drain'),
                RecipeStep('Repeat with remaining batter, adding more oil as needed.'),
                RecipeStep(
                    'Can be Served with:',
                    [
                        RecipeStep('a dollop of yogurt.'),
                        RecipeStep('a dollop of ricotta.'),
                        RecipeStep('crumbled Feta.'),
                        RecipeStep('a Fried Egg.'),
                    ]),
            ]),
        )
    
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
