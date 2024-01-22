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
        r = MyRecipe('Pate a Choux', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )

        
        #  -- Add Ingredients --
     
        #--
        r.addIngredient('Whole Milk', 119, 'grams')
        r.addIngredient('Water', 119, 'grams')
        r.addIngredient('Unsalted Butter', 113, 'grams')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('All Purpose Flour', 120, 'grams')
        r.addIngredient('Eggs', 4, 'large, at room temperature')
        
        # Add Steps and Notes
        steps = [            
            'Combine the milk, water, chopped butter, and salt in a medium saucepan and bring to a boil'
            ' over medium-high heat.',
            
            'Remove the pan from the heat and quickly stir in the flour, all at once.', 
            
            'When the flour is dissolved and the mixture is smooth, return the pan to the heat. Cook over'
            ' medium-low heat, stirring constantly, until the mixture sizzles and the starches gelatinize'
            ' on the bottom of the pot, and starts to form a crust (about 3 minutes). The mixture will be quite'
            ' thick, similar in consistency to dry mashed potatoes.',
            
            'Transfer the mixture into the bowl of a stand mixer fitted with the paddle attachment.',
            
            'With the mixer on low speed, add the eggs , one at a time, mixing until each is incorporated before'
            ' adding the next. Scrape down the sides of the bowl once or twice as necessary. Be careful not to'
            ' overmix the dough or it will become oily and will not puff in the oven the way it should. The dough will'
            ' be thick like mayonnaise.',
            
            'To test for proper consistency, scoop some batter up with your spatula and tip the spatula to see how fast'
            ' it runs down the flat surface. It should run off very slowly and form a "V". If it is too thick and not running'
            ' at all, stir in a little warm water, 1 tablespoon at a time, until it looks a bit looser.',
            
            'Use the Pate a Choux right away or cover the bowl with a wet kitchen towel or plastic wrap and let it stand at'
            ' room temperature until ready to use, up to 4 hours. Refrigerate any unused dough for up to 3 days.'
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
