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
        r = MyRecipe('Hot Water Crust Savory Pie', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('PotatoPie', 'IndianPotatoFilled.jpg')
        r.addPicture('PotatoPieCut', 'IndianPotatoFilledCut.jpg' )
        r.addPicture('ShepardPie', 'ShepardsPie.jpg' )
        r.addPicture('ShepardPiePlate', 'ShepardsPiePlate.jpg')
        r.addPicture('ShepardPiePlateClose', 'ShepardsPiePlateClose.jpg')
        ##r.setPrimaryPicture('ShepardPie')
        r.setRecipeFormat('FANCY_LONG_RECIPE') 
        
        r.AddDescription(
            'We decided to make this after watching a series of episodes of The Great British Bake Off. '
            'The base of the recipe is taken from one of Chetna\'s recipes from the first season on Netflix. '
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
        
        recipeGroupIndianPotato = 'Indian Potato Filling'
        r.addIngredient('Potato', 5, 'large', recipeGroupIndianPotato)
        r.addIngredient('Extra Virgin Olive Oil', 3, 'tablespoons',recipeGroupIndianPotato) 
        r.addIngredient('Garlic', 5, 'cloves, minced', recipeGroupIndianPotato)
        r.addIngredient('Ginger', 1, 'tablespoon, minced', recipeGroupIndianPotato)
        r.addIngredient('Red Onion', 1, 'medium, chopped', recipeGroupIndianPotato)
        r.addIngredient('Serrano Chile', 2, 'small, seeded and chopped', recipeGroupIndianPotato)
        r.addIngredient('Salt', 2, 'teaspoons', recipeGroupIndianPotato)
        r.addIngredient('Curry Powder', 2, 'tablespoons', recipeGroupIndianPotato)
        r.addIngredient('Cumin', 1, 'tablespoons', recipeGroupIndianPotato)
        
        r.addStep( RecipeStep(
            'To make the Shepherd\'s Pie Filling',
            [
                RecipeStep('In a large pot, add Potatoes, cover with water, and add Salt.'),
                RecipeStep('Bring to a boil, then lower to a simmer and cook for 25 minutes.'),
                RecipeStep('Drain the potatoes and remove the skins.'),
                RecipeStep('Mash along with Butter and Milk. Set aside.'),
                RecipeStep('In a frying pan on medium heat, cook the Carrots, Onions and Garlic until just softening, about 2 to 3 minutes, then set aside.'),
                RecipeStep('Defrost the peas in the microwave, covered with a paper towel to keep the moisture in, 2 to 4 minutes.'),
                RecipeStep('Heat the Crumbles in a frying pan until soft, add in the Worcestershire sauce. Remove from heat.'),
                RecipeStep(
                    'When ready to place in the pie crust, assemble by:',
                    [
                        RecipeStep('Place the Mashed Potatoes on the bottom.'),
                        RecipeStep('Then cover with the fried vegetable mixture.'),
                        RecipeStep('Place down the layer of peas.'),
                        RecipeStep('Place down the layer of seasoned Veggie Crumbles.'),
                    ]
                    ),
            ]
            ),
            ['ShepardPiePlateClose']
            )
        
        r.addStep( RecipeStep(
            'To make the Indian Potato Filling',
            [
                RecipeStep('Wash and clean the Potatoes. Pre-cook them in the microwave - either about 8 to 10 minutes, or using the built-in baked potato option.'),
                RecipeStep('Heat a frying pan on medium-high heat.'),
                RecipeStep('Cut the potatoes into large cubes and put into the frying pan with the oil. Fry until browned on the sides, 3 to 8 minutes.'),
                RecipeStep('Add in the Garlic, Ginger, Onion, Chile, Salt, Curry and Cumin. Continue to cook until the vegetables are soft, 2 to 5 minutes.'),
                RecipeStep('When ready to place in the pie crust, fill with the mixture evenly.')
            ]),
            ['PotatoPieCut']
        )
        
        r.addStep( RecipeStep(
            'To make the Pastry Dough',
            [
                RecipeStep('Combine the flours in a large bowl.'),
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
                RecipeStep('Grease a 20cm/8in springform cake tin with vegetable fat.'),
                RecipeStep('Working as quickly as possible, roll out a large circle of dough and, using the rolling pin to help you, line the prepared tin.'),
                RecipeStep('Spoon the filling into the pastry-lined tin. Press it down and level the surface.'),
                RecipeStep('Using the remaining pastry, roll out the pie lid on a lightly floured work surface.'),
                RecipeStep('Crimp the edges to seal and trim off any excess pastry. Make a couple of slits in the top of the pie to allow the steam to escape. '
                           'Use any leftover pastry to make decorations for the top of the pie.'),
                RecipeStep('Bake for 1 hour, or until the top is golden-brown.'),
                RecipeStep('Leave to cool in the tin for 10 minutes, then remove from the tin and leave to cool completely on a wire rack before serving.'),
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
