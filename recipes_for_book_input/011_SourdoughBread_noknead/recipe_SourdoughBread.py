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
        r = MyRecipe('Sourdough Bread',"Baking and Breads", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BreadLoafs', '2020_04_13_Loafs.JPG')
        r.addPicture('SlicedRounds', '2020_05_13_Roudloaf_Sliced.JPG')
        r.addPicture('Rounds', '2020_05_13_RoundLoafs.JPG')
        r.setPrimaryPicture( 'BreadLoafs')
        
        #  -- Add Ingredients --

        ## Garlic
        r.addIngredient('Bread Flour', 602, 'grams ( 5 cups)')
        r.addIngredient('Salt', 12, 'grams')
        r.addIngredient('Diastatic Malt Powder', 12, 'grams')
        r.addIngredient('Potato Flour', 20, 'grams')
        
        r.addIngredient('Sourdough Starter', 227, 'grams')
        r.addIngredient('Water', 400, 'grams, lukewarm')
        
        r.addIngredient('Vegetable Oil', 1, 'tablespoon')
           
        # Add Steps and Notes
        steps = [
            'In large bowl, mix together the dry ingredients - Bread Flour, Salt, Diastic Malt Powder and Potato Flour. '
            'Mix the dry ingredients together.',
            'Add in the Water and Sourdough Starter, and mix with a spoon. The mixture will be sticky and wet.',
            'Cover, and leave the bowl for 1 hour. At the end, wet your hand, and gently fold the dough over on itself several times.'
            ' Repeat this process 3 times, for a total of 3 hours.',
            'Place the bowl in the refrigerator and let the dough rest. I prefer about 48 hours, but as low as 12 hour is ok.',
            'When you\'re ready to make bread, turn the dough out onto a well-floured work surface, and shape it into a rough '
            'ball. Leave the dough seam-side up, cover it, and let it rest on a floured surface for 15 minutes.',
            'Next, shape the dough to fit the vessel in which you\'ll bake it. I typically use the King Arthur Bread Baking '
            'bowl - lightly oiled with Vegetable Oil. I have also used a Pyrex 1.5 quart bread pan, with parchment paper lining'
            ' to make it easy to remove the loaf.',
            'Let the loaf warm to room temperature and rise; this should take about 2 1/2 to 3 hours. It won\'t appear to '
            'rise upwards that much, but will relax and expand.',
            'With a rack positioned in the middle, start preheating the oven to 500 deg F one hour before you\'re ready to bake. Place a'
            ' cast iron pan in the bottom of the oven to put water in to keep the oven humid.',
            'Just before baking, dust the loaf with a fine coat of flour and use a lame or a sharp knife to make one or several 1/2"'
            ' deep slashes through its top surface. If you\'re baking a long loaf, one arched slash down the loaf lengthwise is nice,'
            ' or if baking a round, a crosshatch or crisscross pattern works well.',
            'Reduce the oven temperature to 450 deg F and bake the bread for 45 minutes.',
            'Remove the bread from the oven and transfer it to a rack to cool completely.',
            'Store leftover bread in a plastic bag at room temperature for several days; freeze for longer storage.'
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
