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
        r = MyRecipe('Banana Bread', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BannanaBreadSlice1', 'IMG_2317.jpeg')
        r.addPicture('BannanaBreadSlice2', 'IMG_2318.jpeg')
        r.setPrimaryPicture('BannanaBreadSlice1')
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')  
        #  -- Add Ingredients --

        ## 
        r.addIngredient('All Purpose Flour', 160 , 'grams (1 1/3 cups)')
        r.addIngredient('Salt', 0.75, 'teaspoons')
        r.addIngredient('Baking Soda', 0.5, 'teaspoons')
        r.addIngredient('Baking Powder', 0.25, 'teaspoons')
        r.addIngredient('Cinnamon', 1, 'tablespoon')
        r.addIngredient('Nutmeg', 0.5, 'teaspoon')
        
        r.addIngredient('Unsalted Butter', 5.5, 'tablespoons')
        r.addIngredient('Granulated White Sugar', 135, 'grams (2/3 cup)')
        
        r.addIngredient('Eggs', 2, 'large, lightly beaten')
        
        r.addIngredient('Banana', 1, 'cup, very ripe mashed (about 2)')
        r.addIngredient('Walnuts', 0.5, 'cups, coarsely chopped')
        r.addIngredient('Dark Chocolate chips', 0.5, 'cups')
        
        # Add Steps and Notes
        steps = [
            'Preheat the oven to 350 deg F.',
            'Grease an 8 1/2 x 4 1/2 inch (6-cup) loaf pan.',
            'Whisk together the Flour, Salt, Baking Soda, Baking Powder, Cinnamon and Nutmeg.',
            'In a separate bowl, beat Butter and Sugar on high speed until lightened in color and texture 2 to 3 minutes.',
            'Beat in the flour mixture until blended and the consistency of brown sugar.',
            'Gradually beat in the Eggs.',
            'Fold in Bananas, Chocolate Chips and Walnuts until just combined.',
            'Scrape the batter into the pan and spread evenly.',
            'Bake until a toothpick inserted in the center comes out clean, 50 - 60 minutes.',
            'Let cool in the pan on a rack for 5 - 10 minutes before unmolding to cool completely on the rack.'
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
