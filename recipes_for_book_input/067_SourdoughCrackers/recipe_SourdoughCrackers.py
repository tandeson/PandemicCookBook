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
        r = MyRecipe('Sourdough Crackers','Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Crakers_1','2021_Crackers_1.jpg')
        r.addPicture('Crakers_2','2021_Crackers_2.jpg')
        r.setPrimaryPicture('Crakers_2')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')
        
        #  -- Add Ingredients --
        r.AddDescription('A common use for my leftover starter. Note that which Herb is used isn\'t critical - but I like how rosemary turns out. ~Thomas')
        
        ## 
        r.addIngredient('All Purpose Flour', 113, 'grams (1/2 cup)')
        r.addIngredient('Salt', 0.5, 'teaspoon')
        r.addIngredient('Sourdough Starter', 227, 'grams (1 cup)')
        r.addIngredient('Unsalted Butter', 57, 'grams, 4 tablespoons')
        r.addIngredient('Rosemary', 2 ,'tablespoons')
        r.addIngredient('Extra Virgin Olive Oil', 1, 'tablespoon aprox')
        r.addIngredient('Sea Salt', 2, 'tablespoons, coarse')
        # Add Steps and Notes
        steps = [
            'Mix together the flour, salt, sourdough starter, room temperature butter, and herbs to make a smooth (not sticky), cohesive dough.',
            'Divide the dough in half, and shape each half into a small rectangular slab. Cover with plastic wrap, and refrigerate '
            'for 30 minutes, or up to a couple of hours, until the dough is firm.',
            'Preheat oven to 350 deg F. Very lightly flour a piece of parchment, your rolling pin, and the top of the dough.',
            'Working with one piece at a time, roll the dough to about 1/16" thick.',
            'Transfer the dough and parchment together onto a baking sheet. Lightly brush with oil and then sprinkle the salt over the top of the crackers.',
            'Cut the dough into 1 1/4" squares; a rolling pizza wheel works well here.',
            'Prick each square with the tines of a fork.',
            'Bake the crackers for 20 to 25 minutes, until the squares are starting to brown around the edges. Midway through, reverse the baking sheets. ',
            'When fully browned, remove the crackers from the oven, and transfer them to a cooling rack.'
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
