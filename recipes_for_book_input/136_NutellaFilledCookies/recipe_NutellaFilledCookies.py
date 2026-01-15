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
        r = MyRecipe('Nutella Filled Cookies', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture("Nutella_1", "IMG_4262.jpeg")
        r.setPrimaryPicture("Nutella_1")
        #r.setRecipeFormat('FANCY_WIDE_PIC_OVER_DIRECTIONS') 
        #  -- Add Ingredients --
        
        ## 
        #--
        grpFilling = "Filling"
        r.addIngredient('Nutella', 149, 'grams, (1/2 cup)', grpFilling)
        
        grpDough = 'Dough'
        r.addIngredient('Nutella', 298, 'grams (1 cups)', grpDough)
        r.addIngredient('All Purpose Flour',120,'grams (1 cups)', grpDough)
        r.addIngredient('Salt', '1/4', 'teaspoon', grpDough)
        r.addIngredient('Eggs', 1, 'large', grpDough)
        r.addIngredient('Water', 1, 'tablespoons', grpDough)
        r.addIngredient('Espresso Powder', 0.5, 'teaspoons', grpDough)
        
        # Add Steps and Notes
        steps = [
            "Scoop small balls of Nutella (chestnut-sized, about 1\" diameter) onto a parchment-lined baking sheet."
            " Your goal is about 2 level measuring teaspoons of Nutella. You should have about 12 small balls.",
            
            "Place the baking sheet into the freezer (uncovered is fine) and freeze",
            
            "Preheat the oven to 350 deg F. Lightly grease a baking sheet, or line it with parchment.",

            "Mix together all of the dough ingredients; the mixture will be cohesive, fairly soft, but not"
            " sticky; think modeling clay.",
            
            "Using a scale, take out about 42 grams of dough an roll ito a ball.",
            
            "Flatten a ball of dough. Place one of the frozen Nutella balls in the center. Wrap the dough around"
            " the Nutella like a dumpling, enclosing it completely. Roll the ball of dough between your palms to"
            " seal any cracks and round it out. Repeat with the remaining dough and frozen Nutella balls.",
            
            "Place the cookies on the prepared baking sheet; they won't spread much, so should all fit on one sheet.",
            
            "Bake the cookies for 10 to 12 minutes; when done, they will have lost much of their shine.",
            
            "Remove the cookies from the oven; serve warm, or at room temperature. For the full melting-center, lava-like"
            " effect, serve warm; if they're at room temperature, the centers will be solid.",
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
