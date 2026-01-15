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
        r = MyRecipe('Blitz Puff Pastry', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('FinishedDough', 'FinishedDough.jpeg')
        r.addPicture('ButterCut', 'Notes-Butter_Cut.jpg', roundEdges=False)
        r.addPicture('Folding', 'Notes-Folding.jpeg', roundEdges=False)
        r.setPrimaryPicture('FinishedDough')
        #  -- Add Ingredients --
        
        ## 
        #--
        r.addIngredient('All Purpose Flour', 240, 'grams, (2 cups)')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Unsalted Butter', 227, 'grams, (1 cup)')
        r.addIngredient('Water', 119, 'grams')
        
        # Add Steps and Notes
        r.addStep( RecipeStep( 'In a medium bowl, combine the flour and salt.' ) )
        r.addStep( 
            RecipeStep('Cut Butter into Dice sized cubes, and toss in the flour mixture.'
                       ' Then pull them back out, and flatten them using a plastic dough scrapper'
                       ' into quarter sized pieces.'),
            ['ButterCut']
            )
        
        r.addStep( RecipeStep( 'Add the water ( about 1/3 at a time )and mix to combine.' ) )
        r.addStep( RecipeStep( 'Turn the dough out ont a lighly floured work surface and pat it into a rectangle.' ) )
        r.addStep( RecipeStep( 'Gently roll the dough into a 6" x 20" rectangle.' ), ['Folding'] )
        r.addStep( RecipeStep( 'Fold the dough into thirds, and do a business fold. '
                               'Turn 90 deg, roll out again and then do a offset fold. '
                               'Turn 90 deg, roll out again and then do a book fold.' ) )
        
        r.addStep( RecipeStep( 'Cut the dough in 1/2 - and place each piece in a ziplock bag. '
                               'Wait at least 30 minutes before using - or up to a few days. Can be frozen for '
                               'up to 3 months.' ) )
        #r.addStep( RecipeStep( '' ) )
        
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
