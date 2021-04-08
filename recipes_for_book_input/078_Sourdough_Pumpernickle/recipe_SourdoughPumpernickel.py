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
        r = MyRecipe('Sourdough Pumpernickel',"Baking and Breads", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('loaf_1', 'bread_1.jpg')
        r.addPicture('loaf_2', 'bread_2.jpg')
        r.setPrimaryPicture('loaf_2')
        #  -- Add Ingredients --

        ## 
        grpSpong = 'Sponge'
        r.addIngredient('Pumpernickel Flour', 213, 'grams', grpSpong)
        r.addIngredient('Sourdough Starter', 294, 'grams', grpSpong)
        r.addIngredient('Water', 227, 'grams, or lukewarm coffee', grpSpong)
        r.addIngredient('Onion', 64, 'grams, diced', grpSpong)
        
        grpDough = 'Dough'
        r.addIngredient('Vegetable Oil', 25, 'grams')
        r.addIngredient('Salt', 2, 'teaspoons', grpDough)
        r.addIngredient('Molasses', 85, 'grams', grpDough)
        r.addIngredient('Bread Flour', 482, 'grams ( 4 cups)', grpDough)
        
        # Add Steps and Notes
        r.addStep( RecipeStep('Make the sponge', [
            RecipeStep(
                'Put the Starter, water, coffee, pumpernickel and '
                'onion in a bowl. Stir together, cover and let rest at room'
                ' temperature overnight.')
            ]))
        
        r.addStep( RecipeStep('To make the dough', [
            RecipeStep('The next day, stir the oil, salt and molasses into the sponge. Stir in the flour 1 cup at a time, until the dough comes together.'),
            RecipeStep('Turn the dough out onto a lightly floured surface and knead, adding only enough additional flour to keep it from sticking to your hands.'),
            RecipeStep('Once the dough has come together, shape it into a ball (boule). Place the boule smooth side down in a flour-dusted or lined brotform or bowl.'),
            RecipeStep('Cover and let rise in a draft-free spot until puffy. This will take anywhere from 1 to 3 hours depending on the temperature of the space where the dough is rising and the strength of your starter. '),
            RecipeStep('About an hour before the boule is finished rising, preheat the oven to 425 deg F with a baking stone on the center rack. Place an empty cast-iron skillet on the lowest rack.'),
            RecipeStep('Transfer the boule to the hot stone, and add steam to the oven: Pour about 1 cup of boiling water into the cast iron frying pan. Steam will billow from the pan upwards to envelop the baking bread; be sure to wear good oven mitts to shield your hands and arms. Quickly close the oven door to trap the steam.'),
            RecipeStep('Bake the boule for 40 to 45 minutes, Remove the boule from the oven and cool it on a rack before slicing. '),
            
            ]))
        
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
