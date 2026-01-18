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
        
        ## From First for women magazine, 2020-11-30
        
        r = MyRecipe('Gingerbread House', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('2020_Gingerbread', '2020_GingerbreadHouse.jpg')
        r.setPrimaryPicture('2020_Gingerbread')
        #  -- Add Ingredients --

        ##
        grpNameDough = "Dough"
        r.addIngredient('Unsalted Butter', 3, 'tablespoons, 43 grams', grpNameDough)
        r.addIngredient('Buttermilk', 85, 'grams, about 1/2 cup', grpNameDough)
        r.addIngredient('Brown Sugar', 0.5, 'cups, 114 grams', grpNameDough)
        r.addIngredient( 'Molasses', 0.5, 'cups, 85 grams', grpNameDough)
        r.addIngredient('Eggs', 1, 'medium', grpNameDough)
        r.addIngredient('All Purpose Flour', 2.5, 'cups, 301 grams', grpNameDough)
        r.addIngredient('Baking Soda', 0.5, 'teaspoon', grpNameDough)
        r.addIngredient('Ginger', 1.5, 'teaspoon', grpNameDough)
        r.addIngredient('Cinnamon', 1.5, 'teaspoon', grpNameDough)
        r.addIngredient('Salt', 1, 'teaspoon', grpNameDough)
        
        grpNameIcing = 'Construction icing'
        r.addIngredient('Eggs', 1, 'white only', grpNameIcing)
        r.addIngredient('Cream of Tartar', 0.25, 'teaspoon', grpNameIcing)
        r.addIngredient('Powdered Sugar', 1.3, 'cups, 152 grams', grpNameIcing)
        
        # Add Steps and Notes
        
        stepsIcing = [
            RecipeStep('In a large bowl, whip the egg whites with the cream of tartar until foamy.'),
            RecipeStep('Sprinkle in the sugar gradually, whipping all the while. The more you whip the icing, the '
                       'stiffer it\'ll be and the faster it\'ll harden up.'),
            RecipeStep('Cover the bowl of icing, taking out only as much as you\'ll need immediately. The easiest way'
                       ' to store the icing for long periods of time is in a plastic pastry bag, or zip-top food storage bag.'),
        ]
        r.addStep( RecipeStep( 'To Make the Royal Icing', stepsIcing ) )
        
        stepsDough= [
            RecipeStep('In a large saucepan, heat the buttermilk and butter until the butter is just melted; remove from the heat.'),
            RecipeStep('Add the brown sugar and molasses, then beat in the egg.'),
            RecipeStep('Whisk the baking soda, spices, and salt with 1 cup of the flour.'),
            RecipeStep('Add this to the wet mixture and mix until incorporated.'),
            RecipeStep('Add flour 1 cup at a time until you have a smooth, stiff dough. It should be stiff enough to be flexible, '
                       'and neither crumbly nor sticky.'),
            RecipeStep('Divide the dough in half, flatten each half, and wrap in plastic. Refrigerate for at least 1 hour.'),
            RecipeStep('If desired, food coloring can be added, as can flavoring such as lemon extract, vanilla extract, etc.')
        ]
        r.addStep( RecipeStep( 'To Make the Dough', stepsDough ) )
        
        r.addStep( RecipeStep('Make a plan for your construction, cutting out paper shapes if desired.'))
        r.addStep( RecipeStep('Preheat the oven to 350 deg F.'))
        r.addStep( RecipeStep('Cut your construction pieces as needed, pulling away the scraps to be re-rolled. Transfer the dough, parchment and all, to a baking sheet.'))
        r.addStep( RecipeStep('Bake the dough for 10 to 12 minutes, until set and very lightly browned at the edges.'))
        r.addStep( RecipeStep('Remove from the oven and trim any rough edges while the pieces are still warm. Cool completely before using for construction.'))
        
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
