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
        r = MyRecipe('Egg Roll in a Bowl', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('EggrollInABowl','EggrollInABowl.JPEG')
        r.addPicture('EggrollInABowlWFork', 'EggrollInABowlWFork.JPEG')
        r.setPrimaryPicture('EggrollInABowl')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        ## ---
        
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoon')
        r.addIngredient('Veggie Grillers Crumbles', 1, 'pound')
        r.addIngredient('Green Onion', 5, 'whole')               
        r.addIngredient('Red Pepper Flakes', 1, 'tablespoon')
        r.addIngredient('Ginger', 2, 'tablespoons, minced')
        r.addIngredient('Garlic', 5, 'cloves, minced')
        r.addIngredient('Shredded Cabbage', 3, 'cups, 1 package')
        r.addIngredient('Carrot', 1, 'shredded') 
        r.addIngredient('Bean Sprouts', 2, 'cups, 1 package')
        
        r.addIngredient('Rice Vinegar', 2, 'tablespoons')
        r.addIngredient('Soy Sauce', 0.25, 'cup')
        r.addIngredient('Sesame Oil', 2, 'tablespoons')
        r.addIngredient('Cilantro', 1, 'bunch')
        
        # Add Steps and Notes
        steps = [
            'Heat a large skillet to medium heat and add the cooking oil. Add green onions, garlic, ginger and red pepper flakes and cook for a minute or two.',
            'Defrost the Veggie Crumbles in the microwave according to the packaging, and set aside.',
            'Add the cabbage and carrot to the pan and cook until it starts to get tender.',
            'Add the bean sprouts and cook for a minute more before adding the Veggie Crumbles, rice vinegar, sesame oil and soy sauce, tossing until the mixture is coated.',
            'Garnish with Cilantro.'
            
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
