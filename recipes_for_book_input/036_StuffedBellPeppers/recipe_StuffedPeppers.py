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
        r = MyRecipe('Stuffed Bell Peppers', 'Main dishes',  sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture( 'PepperPlate', '2020_PepperWithSweetPotatoes.jpg' )
        r.setPrimaryPicture( 'PepperPlate' )
        
        #  -- Add Ingredients --
        
        grpRecipeBase = "Base"
        r.addIngredient('Red Bell Pepper', 4, 'large', grpRecipeBase)
        r.addIngredient('Extra Virgin Olive Oil', 2, 'tablespoons', grpRecipeBase)
        r.addIngredient('Yellow Onion', 1, 'medium, chopped', grpRecipeBase)
        r.addIngredient('Garlic', 5, 'cloves, chopped', grpRecipeBase)
        r.addIngredient('Garlic Powder', 1, 'teaspoon', grpRecipeBase)
        r.addIngredient('Onion Powder', 1 , 'teaspoon', grpRecipeBase)
        r.addIngredient('Shredded Mexican Cheese', 0.5, 'cups', grpRecipeBase)
        
        grpRecipeFauxMeat = 'For Faux Meat'
        r.addIngredient('Veggie Grillers Crumbles', 1, 'pound', grpRecipeFauxMeat)
        r.addIngredient('Cauliflower', 2, 'cups, riced', grpRecipeFauxMeat)
        r.addIngredient('Italian Seasoning', 1, 'teaspoon', grpRecipeFauxMeat )
        r.addIngredient('Marinara Sauce', 1.5, 'cups', grpRecipeFauxMeat )
                               
        grpRecipeBeans = 'For Beans'
        r.addIngredient('Black Beans', 1.5, 'can, 15 oz', grpRecipeBeans)
        r.addIngredient('Quinoa', 1.5, 'cups, cooked', grpRecipeBeans)
        r.addIngredient('Cumin', 0.75, 'teaspoon', grpRecipeBeans)
        r.addIngredient('Smoked Paprika', 0.75, 'teaspoon', grpRecipeBeans)
        r.addIngredient('Diced Tomatoes', 1, 'cap, aprox 15 oz')
        
        # Add Steps and Notes
        r.addStep( RecipeStep('Preheat the oven to 400 deg F.' ))
        r.addStep( RecipeStep('Chop the tops off the peppers, and seed.'))
        r.addStep( RecipeStep('Put in a pan with Oil Spray, Place open side up.'))
        r.addStep( RecipeStep(
            'Bake until soft, about 30 minutes',
            [ RecipeStep( 'At about 20 min  of cooking, remove from oven and pour out liquid inside peppers.' ) ]
            ))
            
        r.addStep( RecipeStep('In a pan over medium heat cook the onion and garlic until soft.'))
        r.addStep( RecipeStep('For Faux Meat',
            [
                RecipeStep('Add meat, Cauliflower and seasoning.'),
                RecipeStep('cook, stirring for 8 - 10 minutes'),
                RecipeStep('reduce heat to low, add Marinara. Cook, stirring, about 2 minutes.')
            ] ))
        
        r.addStep( RecipeStep('For Beans',
            [
                RecipeStep('Add the bean, tomatoes, Quinoa and seasoning.'),
                RecipeStep('Cook, stirring for 8 - 10 minutes.')
            ]))
            
        r.addStep( RecipeStep('Remove from heat, fill Peppers with mixture.' ))
        r.addStep( RecipeStep('Sprinkle with cheese.' ))
        r.addStep( RecipeStep('Bake until cheese melts, about 5 - 10 minutes.' ))
        
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
