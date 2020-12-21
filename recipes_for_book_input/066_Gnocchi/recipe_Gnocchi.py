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
        
        ## From First for women magaizin, 2020-11-30
        
        r = MyRecipe('Gnocchi', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('GnocchiWithPeas', '2020_Dec_Gnocchi.jpg')
        r.setPrimaryPicture('GnocchiWithPeas')
        
        #  -- Add Ingredients --

        ##
        grpNameGnocchi = 'For the Gnocchi'
        r.addIngredient('Potato', 2, 'large Russet, about 1.75 pounds', grpNameGnocchi)
        r.addIngredient('Eggs', 1, 'large, scrambled', grpNameGnocchi)
        r.addIngredient('All Purpose Flour', 0.75, 'cups', grpNameGnocchi)
        r.addIngredient('Salt', 1.5, 'teaspoon', grpNameGnocchi)
        
        grpNameSauce = 'Sauce'
        r.addIngredient('Garlic', 5, 'cloves, diced', grpNameSauce)
        r.addIngredient('Peas', 1, 'cup, frozen', grpNameSauce)
        r.addIngredient('Unsalted Butter', 3, 'tablespoons', grpNameSauce)
        r.addIngredient('Whole Milk', 0.5, 'cups', grpNameSauce)
        r.addIngredient('Parmesan Cheese', 1, 'cup', grpNameSauce)
        r.addIngredient('Salt', 2, 'teaspoons, to taste', grpNameSauce)
        r.addIngredient('Black Pepper', 1, 'teaspoons, to taste', grpNameSauce)
        # Add Steps and Notes
        steps= [
            'Fill a large pot with water and bring to a boil. Salt can be added',
            'Place the Potatoes in the boiling water, and boil for about 45 minutes, until tender.',
            'Remove the potatoes one at a time, peel, and run though a food mill into a bowl. If you'
            ' don\'t have a mill, use a spoon and a strainer to rice into a bowl.',
            'Wait for the potatoes to cool - about 15 minutes.',
            'Start a pot of boiling water to cook the Gnocchi in - this can be the same water the potatoes were boiled in.',
            'Mix in flour, salt and egg. Mix together, and then gently kneed. The dough should be wet, but not sticky. You can add more flour if it\'s sticky',
            'Divide into about 12 pieces.',
            'Roll each piece into a snake like log, and cut into pieces.',
            'In groups of about 20, place into the boiling water. Wait for the Gnocchi to float, and then give them another 10 second to cook.',
            'Remove them with a slotted spoon, and place on a plate, or sauce if ready.'
        ]
        
        for s in steps:
            r.addStep( RecipeStep( s ) )
        
        stepsSauce = [
            RecipeStep('Heat a large sauce pan on medium heat. Put the frozen peas in the pan.'),
            RecipeStep('When the peas are no longer frozen, add in the butter and garlic. Cook until the garlic starts to just brown.'),
            RecipeStep('Add in the milk, cheese, salt and pepper. Stir vigorously until cheese melts. If it\'s too thick, add more milk and repeat.'),
            RecipeStep('Remove from heat, and mixe in Gnocchi.')
        ]
        r.addStep( RecipeStep('Peas and White Sauce', stepsSauce ) )

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
