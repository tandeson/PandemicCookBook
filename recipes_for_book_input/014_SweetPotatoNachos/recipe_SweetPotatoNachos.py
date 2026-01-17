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
        r = MyRecipe('Sweet Potato Nachos',"Appetizers", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('FullNachos', '2020_09_14_NachosFull.JPG')
        r.setPrimaryPicture( 'FullNachos')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Sweet Potatoes', 3, 'cleaned, sliced to 1/4"')
        r.addIngredient('Extra Virgin Olive Oil', 1 , 'tablespoon')
        r.addIngredient('Shredded Mexican Cheese', 1.5 , 'cups')
        r.addIngredient('Black Beans', 15, 'oz, canned')
        r.addIngredient('Cilantro', 0.25, 'cup')
        r.addIngredient('Salt', 1, 'tablespoon')
        r.addIngredient('Black Pepper', 0.25, 'tablespoon' )
        
        
        r.addIngredient('Pickled Jalapenos', 3, 'oz (to taste)')
        r.addIngredient('Pickled Red Onions', 3, 'oz (to taste)')
        
        # Add Steps and Notes
        steps = [
            'Preheat the oven to 400 deg F.',
            'Place the sweet potato rounds on a large baking sheet. You '
            'don\'t want to overcrowd the sweet potatoes. Toss the sweet '
            'potatoes in olive oil and season with salt and pepper. Bake for '
            '20 minutes. Use a spatula to flip the sweet potato rounds. Bake for '
            'an additional 10 minutes or until sweet potatoes are crisp.',
            'Remove the pan from the oven and sprinkle cheese and black beans '
            'over the sweet potatoes. Bake until cheese is melted, about 5 to 7 minutes.',
            'Remove the pan from the oven and top with Cilantro, Pickled Red Onions and Pickled Jalapenos.',
            ]
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        r.addStep( 
            RecipeStep( "Serve with Guacamole and enjoy!" )
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
