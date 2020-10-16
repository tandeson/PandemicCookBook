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
        r = MyRecipe('Black Bean Tacos', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('BlackBeanTacosDone', '2020_09_12_BlackbeanTaco.jpg')
        r.setPrimaryPicture( 'BlackBeanTacosDone' )
        
        #  -- Add Ingredients --

        ##
        GrpNameBeans = "Seasoned Black Beans"
        r.addIngredient('Black Beans', 29, 'oz, canned', GrpNameBeans)
        
        r.addIngredient('Salt', 1, 'tablespoon', GrpNameBeans)
        r.addIngredient('Black Pepper', 0.25, 'tablespoon', GrpNameBeans)
        r.addIngredient('Cumin', 0.5, 'tablespoon', GrpNameBeans)
        r.addIngredient('Chili powder', 1, 'tablespoon', GrpNameBeans)
        r.addIngredient('Garlic Powder', 0.5, 'tablespoon', GrpNameBeans)
        r.addIngredient('Onion Powder', 0.5, 'tablespoon', GrpNameBeans)
        r.addIngredient('Water', 4, 'tablespoon', GrpNameBeans)
        
        r.addIngredient('Onion', 0.5, 'medium, chopped', GrpNameBeans)
        r.addIngredient('Garlic', 4, 'cloves, chopped', GrpNameBeans)
        
        r.addIngredient('Extra Virgin Olive Oil', 2 , 'tablespoons', GrpNameBeans)
        
        GrpNameTaco = "Taco Shells"
        r.addIngredient('Corn Tortillas', 8, 'qty', GrpNameTaco)
        
        GrpNameCondiments = "Condiments"
        r.addIngredient('Romaine Lettuce', 0.25, 'head, chopped', GrpNameCondiments)
        r.addIngredient('Feta Cheese', 3, 'oz (to taste)', GrpNameCondiments)
        r.addIngredient('Pickled Jalapenos', 3, 'oz (to taste)', GrpNameCondiments)
        r.addIngredient('Pickled Red onions', 3, 'oz (to taste)', GrpNameCondiments)
           
        # Add Steps and Notes
        r.addStep( RecipeStep(
            'Make the Seasoned Black Beans',[
                RecipeStep('Heat a frying pan on medium-high heat.'),
                RecipeStep(
                    'Prepare the Black Bean Seasoning.',[
                        RecipeStep('In a cup, mix the Salt, Pepper, Cumin, Chili Powder, Garlic Powder, Onion Powder and water. Mix thoroughly into a slurry.')
                    ]),
                RecipeStep('Put about 1 tablespoon of Olive Oil into the pan, and fry the Onions and Garlic until the Onions are translucent.'),
                RecipeStep('Rinse the Black Beans, and put them into the frying pan.'),
                RecipeStep('Put in the Black Bean Seasoning, and mix. It should be just liquid. If it isn\'t, add more water.'),
                RecipeStep('Cook it down, until the Beans, Onions, Garlic and Seasoning are mixed and sticking together.'),
                RecipeStep('Remove from frying pan and set aside.')
            ]),
        )
        
        r.addStep(RecipeStep(
            'Prepare the Taco shells',[
                RecipeStep('Heat a frying pan on medium-high heat.'),
                RecipeStep('Put about 1 tablespoon of Olive Oil into the pan.'),
                RecipeStep('Taking 1 or 2 Tortilla(s) at a time, fry them until crispy and slighly browned on each side.'),
                RecipeStep('Remove from the pan, and allow to drain / cool on a paper towel.')
                ])
            )
        
        r.addStep(RecipeStep( 'Place a Taco shell down. Layer on the Seasoned Black Beans and any Condiments you want.' ))
        r.addStep(RecipeStep( 'Enjoy!.' ))
        
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
