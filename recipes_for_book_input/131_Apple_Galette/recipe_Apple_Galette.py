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
        r = MyRecipe('Apple Galette', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')  
        r.addPicture('galette', 'IMG_3510_resize.jpg')
        r.setPrimaryPicture('galette')
        
        #  -- Add Ingredients --
        ##
        #--
        r.addIngredient('Blitz Puff Pastry', 1, 'batch')
        r.addIngredient('Apples', 4, 'medium cored and sliced')
        r.addIngredient('Eggs Whites', 1, 'large egg')
        r.addIngredient('Granulated White Sugar', 50, 'grams')
        
        # Add Steps and Notes
        r.addStep(RecipeStep('Preheat oven to 400 deg F. Line a baking sheet with parchment paper.'))
        r.addStep(RecipeStep('On a lighly floured surface, roll out the blitz puff pastry dough to an 8"x12" '
                             'rectangle, about 1/8" thick.'))
        r.addStep(RecipeStep('Trim the edges,  then cut 1/2" border strips from the sides of the base.'))
        r.addStep(RecipeStep('Lightly brush the sides of the base with egg white to adhere the border strips.'))
        r.addStep(RecipeStep('Arrange the  apple slices overlapping slightly, on the pastry base.'))
        r.addStep(RecipeStep('Sprinkle the apple slices with the sugar, to taste. Chill in the freezer for 15 minutes.'))
        r.addStep(RecipeStep('Bake the galette for 25 minutes, or until the pastry is deep golden brown '
                             'and puffed and the apples are tender.'))
        
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
