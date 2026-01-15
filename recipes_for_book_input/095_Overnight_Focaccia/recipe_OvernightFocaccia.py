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
        r = MyRecipe('Overnight Focaccia', 'Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('thanksgiving_focaccia', '2021_Focaccia.jpg')
        r.setPrimaryPicture('thanksgiving_focaccia')
        
        r.AddDescription('Andrew suggested this bread for Thanksgiving 2021 - and it was a hit! ~ Thomas')
        #  -- Add Ingredients --

        ## 
        r.addIngredient('Bread Flour', 512, 'grams (4 cups)')
        r.addIngredient('Salt', 10, 'grams (2 teaspoons)')
        r.addIngredient('Active Dry Yeast', 8, 'grams (2 teaspoons)')
        r.addIngredient('Water', 455 , 'grams (2 cups) lukewarm')
        r.addIngredient('Extra Virgin Olive Oil', 4, 'tablespoons')
        r.addIngredient('Rosemary', 1, 'tablespoon')
        
        # Add Steps and Notes
        r.addStep( RecipeStep( 
            'Mix together the Flour, Salt and Yeast. Mix until combined.',
            ))
        
        r.addStep( RecipeStep( 
            'Add in the Water and mix until the liquid is absorbed and '
            'the ingredients form a sticky dough ball. Rub the surface with olive oil, '
            'Cover the bowl and place in the refrigerator for at least 12 hours or up to 3 days.',
            ))
        
        r.addStep( RecipeStep(
            'Line two 8- or 9-inch pie plates or a 9x13-inch pan (see notes above) with parchment '
            'paper or grease with butter or coat with nonstick cooking spray.' 
            ))
         
        r.addStep( RecipeStep(
            'Pour a tablespoon of oil into the center of each pan or 2 tablespoons of oil if using '
            'the 9x13-inch pan. Using two forks, deflate the dough by releasing it from the sides of '
            'the bowl and pulling it toward the center. Rotate the bowl in quarter turns as you deflate, '
            'turning the mass into a rough ball. Use the forks to split the dough into two equal pieces '
            '(or do not split if using the 9x13-inch pan). Place one piece into one of the prepared pans. '
            'Roll the dough ball in the oil to coat it all over, forming a rough ball. Repeat with the '
            'remaining piece. Let the dough balls rest for 3 to 4 hours depending on the temperature of '
            'your kitchen.' 
            ))

        r.addStep( RecipeStep( 
            'Preheat the Oven to 425 deg F. Sprinkle the rosemary over the dough and pour over remaining '
            'olive oil. Grease hands, and dimple the dough.'
            ))
        
        r.addStep( RecipeStep( 
            'Transfer the pans or pan to the oven and bake for 25 to 30 minutes, until the under side is '
            'golden and crisp. Remove the pans or pan from the oven and transfer the focaccia to a cooling '
            'rack. Let it cool for 10 minutes before cutting and serving'
            ))
        
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
