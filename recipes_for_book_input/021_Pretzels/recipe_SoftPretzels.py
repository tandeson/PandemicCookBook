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
        
        Based on Recipe provided in class at King Arthur Baking School in Skagit Valley WA.
        Yeilds: 12 Pretzels
        """
        r = MyRecipe('Soft Pretzels','Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('PretzelBasket', '2020_01_16_Pretzels_andPretzelRolls.jpeg')
        r.addPicture('ShapePretzel','pretzel_shape_From_web.jpg', False)
        r.setPrimaryPicture('PretzelBasket')

        #  -- Add Ingredients --
        r.addToDoNote('Add info on Pretzel rolls.. - basically same recipe.')
        r.addToDoNote('Replace Shaping picture with my own from making these again...')
        
        ## Garlic
        grpDough = 'Pretzel Dough'
        r.addIngredient('All Purpose Flour', 600 , 'grams (5 cups)', grpDough)
        r.addIngredient('Water', 354, 'grams (1.5 cups)', grpDough)
        r.addIngredient('Unsalted Butter', 28, 'grams, soft', grpDough)
        r.addIngredient('Salt', 12, 'grams', grpDough)
        r.addIngredient('Active Dry Yeast', 5 , 'grams (1.5 teaspoons)', grpDough)            
        r.addIngredient('Diastatic Malt Powder', 1, 'gram (1/4 teaspoon)', grpDough)
        
        grpBath = 'Bath'
        r.addIngredient('Water', 4, 'quarts', grpBath)
        r.addIngredient('Baking Soda', 130, 'grams (1/2 cup)', grpBath)
         
        # Add Steps and Notes
        steps = [
            'Combine all the ingredients in the bowl of a stand mixer.',
            'Mix for about 3 minutes on slow speed, and then turn up to medium speed '
            '( around speed 4 on a Kitchen Aid) for 5-6 minutes.',
            'Cover the bowl and allow the dough to rest for 30-40 minutes.'
             ]
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        r.addStep( RecipeStep(
            'Divide the dough into 12 pieces, weighing approximately 80 grams each. Roll '
            'each piece into a cylinder about 24 inches long, with the center being thicker than the ends.'
            ' Pick the dough up by the ends and twist twice. Take the ends and press down on each side.'),
            ['ShapePretzel']
            )
        
        steps = [
            'Place pretzels on a parchment lined baking sheet, cover and leave at room temperature for 30 minutes.',
            'Preheat oven to 400 deg F',
            'Chill the risen pretzels, still covered, for 30 minutes.',
            'While the pretzels are chilling, make the baking soda bath by combining the water and Baking Soda.'
            ' Bring to a rolling boil in a wide pan.',
            'Simmer the pretzels ( a few at a time) in the baking soda water for 10 seconds per side.',
            'Place on a parchment lined baking sheet, and sprinkle lightly with coarse salt, if desired.'
            ' Alternatively, you can also coat with Cinnamon Sugar.',
            'Bake for 14 to 18 minutes, until deep golden brown.',
            'If desired, brush with melted butter while still warm.',
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
