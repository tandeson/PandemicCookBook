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
        r = MyRecipe('Pico de Gallo','Spreads and Dips', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('PicoDeGalloBowl', 'PicoDeGalloBowl.JPEG')
        r.setPrimaryPicture( 'PicoDeGalloBowl' )
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Red Onion', 0.5, 'large, chopped fine')
        r.addIngredient('Jalapeno Pepper', 2, 'seeded and chopped fine')
        r.addIngredient('Lime', 1, 'medium, juiced')
        r.addIngredient('Salt', 1, 'teaspoon')
                
        r.addIngredient('Tomatoes', 3, 'seeded and finely chopped ')
        r.addIngredient('Cilantro', 0.25, 'bunch, chopped fine')
        
        # Add Steps and Notes
        steps = [
            'Mix the Onion, Jalapeno, Salt and Lime in a bowl. Let sit for 5 minutes.',
            'Add the chopped tomatoes and cilantro to the bowl and stir to combine. Taste, and add more salt if needed.',
            'Let the mixture marinate for 15 minutes or several hours in the refrigerator before serving for best results.'
    
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
