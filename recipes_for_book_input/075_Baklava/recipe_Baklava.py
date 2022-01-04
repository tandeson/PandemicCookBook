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
        r = MyRecipe('Baklava', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('BaklavaSheet', '2021_BaklavaFromNoruz.jpeg')
        r.setPrimaryPicture('BaklavaSheet')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS') 
        #  -- Add Ingredients --
        
        ## 
        #--
        r.addIngredient('Walnuts', 3, 'cups, finely chopped')
        r.addIngredient('Granulated White Sugar', 1.5 , 'cups')
        r.addIngredient('Cinnamon', 1 , 'teaspoon')
        r.addIngredient('Unsalted Butter', 0.75, 'cup, melted')
        r.addIngredient('Phyllo Dough', 0.5, '16-oz package')
        r.addIngredient('Water', 0.75, 'cups')
        r.addIngredient('Honey', 3 ,'tablespoons')
        r.addIngredient('Lemon', 1, 'for shredded peel and juice')
        r.addIngredient('Cinnamon', 1 , 'stick, 2 inches')
        
        # Add Steps and Notes
        steps = [
            'Preheat oven to 325 deg F.',
            'In a large bowl, stir together walnuts, 1/2 cup sugar and ground cinnamon.',
            'Brush the bottom of a 13x9x2 inch baking pan with some of the melted butter. Unroll phyllo dough; cover with a moist towel.'
            ' As you work, keep dough covered in order keep it from drying out. Layer 5 sheets of phyllo in the prepared baking pan, brushing'
            ' each sheet generously with some of the melted butter. Layer in 1/3 of the filling. Repeat layer phyllo sheet and filling two more times, '
            'brushing each sheet with more butter. Layer 5 more sheets on the top. Drizzel remaining butter across the top.',
            'Using a sharp knife, cut into 24 to 48 rectangle pieces.',
            'Bake for 35 - 45 minutes or until golden brown. Remove from oven, and cool slightly on a wire rack in the pan.',
            'For syrup: In a medium sauce pan, stir together the remaining sugar, honey, water, lemon peel, lemon juice and cinnamon stick.',
            ' Bring to boiling; reduce heat. Simmer, uncovered, for 20 minutes. Remove cinnamon stick, and pour evenly over the baklava in the pan.'
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
