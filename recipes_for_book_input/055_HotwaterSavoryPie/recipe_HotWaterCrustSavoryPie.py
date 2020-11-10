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
        r = MyRecipe('Hot Water Crust Savory Pie', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('PotatoPie', 'IndianPotatoFilled.jpg')
        r.addPicture('PotatoPieCut', 'IndianPotatoFilledCut.jpg' )
        r.addPicture('ShepardPie', 'ShepardsPie.jpg' )
        r.addPicture('ShepardPiePlate', 'ShepardsPiePlate.jpg')
        r.addPicture('ShepardPiePlateClose', 'ShepardsPiePlateClose.jpg')
        r.setPrimaryPicture('ShepardPiePlateClose')
        
        r.AddDescription(
            'We decided to make this after watching a series of Episodes of the Great British Bake off. '
            'The base of the recipe is taken from one of Chetna\'s from the first season on Netflix. '
            ' ~Thomas'
        )
        #  -- Add Ingredients --
        recipeGroupPastry = 'Hot Water Crust Pastry'
        r.addIngredient('All Purpose Flour', 450, 'grams', recipeGroupPastry)
        r.addIngredient('Bread Flour', 100, 'grams', recipeGroupPastry)
        r.addIngredient('Unsalted Butter', 5, 'tablespoons', recipeGroupPastry)
        r.addIngredient('Water', 200, 'mL (7 oz)', recipeGroupPastry)
        r.addIngredient('Salt', 0.5, 'teaspoon, fine', recipeGroupPastry)
        r.addIngredient('Shortening', 100, 'grams', recipeGroupPastry)
                        
        recipeGroupShepardsPie = 'Shepherd\'s Pie Filling'
        r.addIngredient('Potato', 3, 'large', recipeGroupShepardsPie)
        r.addIngredient('Salt', 2, 'teaspoons', recipeGroupShepardsPie)
        r.addIngredient('Whole Milk', 0.5, 'cups', recipeGroupShepardsPie)
        r.addIngredient('Unsalted Butter', 2, 'tablespoons', recipeGroupShepardsPie)
        r.addIngredient('Carrot', 1, 'cup, chopped', recipeGroupShepardsPie)
        r.addIngredient('Garlic', 5, 'cloves, chopped', recipeGroupShepardsPie)
        r.addIngredient('Yellow Onion', 1, 'medium, chopped', recipeGroupShepardsPie)
        r.addIngredient('Peas', 8, 'oz, frozen', recipeGroupShepardsPie)
        r.addIngredient('Worcestershire Sauce', 1, 'tablespoon', recipeGroupShepardsPie)
        r.addIngredient('Veggie Grillers Crumbles', 1, 'package, about 12 oz',recipeGroupShepardsPie),
        
        r.addStep( RecipeStep(
            'To make the Shepherd\'s Pie Filling',
            [
                RecipeStep('In a large pot, add Potatoes and cover with water and add Salt.'),
                RecipeStep('Bring to boil, and then lower to a simmer - cook for 25 minutes.'),
                RecipeStep('Dry Potatos, and remove the skins.'),
                RecipeStep('Mash along with Butter and Milk. Set Aside'),
                RecipeStep('In a Frying pan on medium heat, cook the Carrots, Onions and Garlic until just softening. About 2 - 3 minutes. and set aside.'),
                RecipeStep('Defrost the peas in the microwave, covered with a paper towel to keep the moisure in, 2 - 4 minutes.'),
                RecipeStep('Heat the Crumbles in a frying pan until soft, add in the Worcestershire sauce. Remove from heat.'),
                RecipeStep(
                    'When ready to place in the pie crust, assemble by:',
                    [
                        RecipeStep('Place the Mashed Potatoes on the bottom.'),
                        RecipeStep('Then cover with the fried Veggitable mixture.'),
                        RecipeStep('Place down the layer of peas.'),
                        RecipeStep('Place down the layer of seasoned Veggies Crumbles.'),
                    ]
                    ),
            ]
            ))
        
        r.addStep( RecipeStep(
            'To make the Pastry Dough',
            [
                RecipeStep('combine the flours in a large bowl.'),
                RecipeStep('Add the butter and, using your fingertips, rub it into the flour until it resembles breadcrumbs.'),
                RecipeStep('In a pan, heat water, the salt and fat until just boiling.'),
                RecipeStep('Pour the liquid onto the flour mixture and mix using a wooden spoon.'),
                RecipeStep('Tip the dough out onto a lightly floured work surface and knead to a smooth dough.'),
            ]
            ))
        
        r.addStep( RecipeStep(
            'To make a Pie',
            [
                RecipeStep('Preheat the oven to 400 deg F.'),
                RecipeStep('Grease a 20cm/8in springform cake tin with vegetable fat'),
                RecipeStep('Working as quickly as possible, roll out a large circle of dough and, using the rolling pin to help you, line the prepared tin.'),
                RecipeStep('Spoon the filling into the pastry lined tin. Press it down and level the surface.'),
                RecipeStep('Using the remaining pastry, roll out the pie lid on a lightly floured work surface.'),
                RecipeStep('Crimp the edges to seal and trim off any excess pastry. Make a couple of slits in the top of the pie to allow the steam to escape. '
                           'Use any leftover pastry to make decorations for the top of the pie.'),
                RecipeStep('Bake for 1 hour, or until the top is golden-brown.'),
                RecipeStep('Leave to cool in the tin for 10 minutes then remove from the tins and leave to cool completely on a wire rack before serving.'),
            ]
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
