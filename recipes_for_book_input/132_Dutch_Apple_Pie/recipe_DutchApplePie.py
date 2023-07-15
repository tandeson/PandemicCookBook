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
        r = MyRecipe('Dutch Apple Pie', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('dutchApplePie', 'IMG_3939.jpeg')
        r.setPrimaryPicture('dutchApplePie')
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')
        
        r.AddDescription("We made this once for Polly and and now it's part of the rotation.")
        
        #  -- Add Ingredients --
        grpTxtCrust = "Crust"
        r.addIngredient('All Purpose Flour', 120, 'grams, 1 cup', grpTxtCrust)
        r.addIngredient('Salt', 0.25, 'teaspoon', grpTxtCrust)
        r.addIngredient('Unsalted Butter', 8, 'tablespoons, cold', grpTxtCrust)
        r.addIngredient('Water', 28, 'grams, ice cold', grpTxtCrust)
        
        grpTxtFilling = "Filling"
        r.addIngredient('Apples', 900, 'grams, 4 large - sliced', grpTxtFilling)
        r.addIngredient('Granulated White Sugar', 149, 'grams', grpTxtFilling)
        r.addIngredient('All Purpose Flour', 30, 'grams', grpTxtFilling)
        r.addIngredient('Cinnamon', 1, 'teaspoon, to taste', grpTxtFilling)
        r.addIngredient('Nutmeg', 0.25, 'teaspoon, to taste', grpTxtFilling)
        
        grpTxtTopping = "Topping"
        r.addIngredient('All Purpose Flour', 120, 'grams, 1 cup', grpTxtTopping)
        r.addIngredient('Brown Sugar', 92, 'grams', grpTxtTopping)
        r.addIngredient('Unsalted Butter', 8, 'tablespoons, cold', grpTxtTopping)
                                  
        # Add Steps and Notes
        r.addStep( RecipeStep('Make the Crust',[
            RecipeStep('Place the flour and salt in a mixer bowl. Run the mixer at'
                       ' low speed unit until lumps the size of peas (or smaller) remain.'),
            RecipeStep('The water should be ice cold and added gradually while the mixer runs.'
                       ' When the dough starts to hold together a bit stop the mixer and gather'
                       ' it with your hands and form it into a ball.'),
            RecipeStep('Wrap and chill the dough for half an hour before rolling it out. While the'
                       ' dough is chilling, make the filling.')
            ]))
        
        r.addStep( RecipeStep('Make the Filling',[
            RecipeStep('Preheat the oven to 425 deg F'),
            RecipeStep('Mix the apples with the flour, sugar and spices.'),
            RecipeStep("Transfer the dough to a floured board. Roll the dough until it's 2\" larger "
                       "in diameter than the top edge of the pie pan. Transfer the dough to the pan,"
                       " and flute the edges.")
            ]))
        r.addStep( RecipeStep('Pour the Apple mixture into the prepared pie pan.') )
        r.addStep( RecipeStep('Make the Topping',[
            RecipeStep('Cut the butter up with a knife. Add it to the flour and sugar and use a mixer to'
                       ' get it to a breadcrum consistency.'),
            RecipeStep('Spread this mixture evenly over the top of the apples.')
            ]))
        
        r.addStep( RecipeStep('Place a baking sheet under to catch drips and bake for 15 minutes.'
                              ' Reduce heat to 350 deg F and bake for another 30 minutes. Allow to cool before serving.') )
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
