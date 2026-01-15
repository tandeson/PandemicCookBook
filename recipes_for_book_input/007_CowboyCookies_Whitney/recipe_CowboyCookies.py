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
        r = MyRecipe('Cowboy Cookies', "Dessert", sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('CowboyCookies', 'cowboycookiesBeingMade.jpg')
        r.setPrimaryPicture('CowboyCookies')
        
        r.AddDescription(
           'My friend Whitney Hudson used to bring these cookies into work. I\'d never '
           'had a cookie with Rice Crispies in it before - and it adds a wonderful crunch! '
           'When she took a job at Microsoft, she gave this recipe to me as a parting gift. '
           'This is 1/2 of what the original recipe called for - as it made what she described as '
           '"a Lutheran Funeral" of cookies. ~Thomas'
        )
        #  -- Add Ingredients --
        
        ## Makes about 2 dozen?
        #--
        r.addIngredient('Shortening', 1, 'cup')
        r.addIngredient('Granulated White Sugar', 1, 'cup')
        r.addIngredient('Brown Sugar', 1, 'cup')
        r.addIngredient('Eggs', 2, 'medium')
        r.addIngredient('Vanilla', 1, 'teaspoon')
        r.addIngredient('All Purpose Flour', 1.5, 'cups')
        r.addIngredient('Baking Soda', 1, 'teaspoon')
        r.addIngredient('Salt', 1, 'teaspoon')
        r.addIngredient('Rice Crispies', 1, 'cup')
        r.addIngredient('Oatmeal',1.5, 'cups')
        r.addIngredient('Dark Chocolate chips', 6, 'oz')
        r.addIngredient('Butterscotch chips', 6, 'oz')
        
        # Add Steps and Notes
        steps = [
            'Pre-heat the oven to 350 deg F.',
            'Cream together shortening, sugar and brown sugar.',
            'Add the Eggs and Vanilla and beat together,',
            'In a separate bowl - sift and mix together Flour,'
            ' Baking Soda and Salt',
            'Mix the wet and dry mixtures together.',
            'To the dough, add the Rice Crispies, Oatmeal, '
            'Chocolate Chips and Butterscotch Chips.'
            'Mix well',
            'Use a spoon to scoop into large teaspoon sized balls'
            ' on a baking sheet covered in parchment paper.',
            'Bake for 10-12 minutes.'
            'Remove, and allow to cool.'
            ]
        
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        r.addToDoNote("Add optional notes.")
        # Notes
        ## Can put in heath toffee chips
        ## Can put in walnuts.
        
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
