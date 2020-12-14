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
        r = MyRecipe('Pad Kee Mao', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('OurPadKeeMaoMade', '2020_09_09_PadKeeMao_done.jpg')
        r.setPrimaryPicture( 'OurPadKeeMaoMade')
        
        r.AddDescription(
            'In July of 2020 we went and got takout for our 6 month anniversary at a Thai restaurant. '
            'This was our first restaurant food since the pandemic lockdown. This caused us to bemoan '
            'the fact that we couldn\'t get Thai food. Later that month, we found this recipe online and '
            'adapted it for us. Since then we\'ve made it multiple times! ~Thomas'
        )
        #  -- Add Ingredients --

        ## Noodles
        r.addIngredient('Dry Wide Rice Noodles', 150, 'grams', 'Noodles')
        
        grpProtien = "For seasoned Tofu"
        r.addIngredient('Fried Tofu', 7 , 'ounces, approximately', grpProtien )
        r.addIngredient('Soy Sauce', 1, 'teaspoon', grpProtien )
        r.addIngredient('Corn Starch', 1, 'teaspoon', grpProtien )
                      
        grpSauce = "For Pad Kee Mao sauce"
        r.addIngredient('Fish Sauce', 1, 'tablespoon', grpSauce)
        r.addIngredient('Oyster Sauce', 1, 'tablespoon', grpSauce)
        r.addIngredient('Evaporated Cane Sugar', 1, 'tablespoon', grpSauce)
        r.addIngredient('Rice Vinegar', 1, 'tablespoon', grpSauce)
        
        grpStirFry = 'For stir-fry'
        r.addIngredient('Vegetable Oil', 2, 'tablespoon', grpStirFry)
        r.addIngredient('Garlic', 3, 'large cloves, minced', grpStirFry) #18 grams
        r.addIngredient('Eggs', 2, 'medium', grpStirFry)
        r.addIngredient('Onion', 0.5, 'small, sliced', grpStirFry) #75 grams
        r.addIngredient('Red Bell Pepper', 1, 'pepper, sliced', grpStirFry) #50 grams
        r.addIngredient('Carrot', 10, 'baby, sliced', grpStirFry) #30 grams
        r.addIngredient('Bird Chillies', 2, 'optional, minced', grpStirFry)
        r.addIngredient('Tomatoes', 0.5, 'medium sliced', grpStirFry) # 70 grams
        r.addIngredient('Thai Basil', 20, 'grams (leaves only)', grpStirFry)
        
        ## Notes
        # We did not use the 
        #  * 70 g of Baby Corn ( 5 years, sliced in 1/2 )
        #  * 1 tablespoon green peppercorns in brine
        
        # Add Steps and Notes
        r.addStep( RecipeStep( 
            'Prepare the Noodles', 
            [
                RecipeStep( "Rehydrate the noodles in room temperature water for 2 hours"),
                RecipeStep( 
                    "Alternatively - you can also rehydrate them in boiling water for 10 "
                    "minutes, while stirring to keep them from sticking together. This "
                    "method leads to noodles that are more likely to fall apart.")
                ],
            ))
        
        r.addStep( RecipeStep( 
            'Prepare the Tofu', 
            [
                RecipeStep('Add the Tofu to a bowl'),
                RecipeStep('mix in the Soy Sauce and Corn Starch to combined.'),
                RecipeStep('Let this marinate while you prepare the other ingredients.'),
            ],
        ))
        
        r.addStep( RecipeStep(
            'Make the sauce by stirring together the Fish Sauce, Oyster Sauce, '
            'Sugar and rice vinegar until combined.'
            ))
        
        r.addStep( RecipeStep(
            'Cook and Combind',
            [
                RecipeStep('Heat a frying pan or wok over medium-high heat until hot'),
                RecipeStep('add in 1 tablespoon of oil, and swirl to codat the pan.'),
                RecipeStep(
                    'Add the Tofu, stir fry until brown, and remove the Tofu'
                    ' from the pan, leaving as much oil in the pan as possible'),
                RecipeStep('Add the garlic and fry until fragrant.'),
                RecipeStep('Add the eggs and then scramble.'),
                RecipeStep(
                    'When the Eggs are almost cooked, add another tablespoon of oil,'
                    ' along with the Onions, Bell Pepper and Carrot.'),
                RecipeStep('Fry until the Onions are translucent but still crips.'),
                RecipeStep(
                    'Add the rehydrated noodles and stir fry until the '
                    'noodles take on some color.'),
                RecipeStep(
                    'Add the sauce and stir-fry until the noodles are evenly coated '
                    'and the liquid has been absorbed.'),
                RecipeStep('Return the Tofu to the pan and add the Tomatoes and basil.'),
                RecipeStep('Quickly stir-fry to reheat the Tofu and wilt the Basil.')
            ],
            ))
        
        r.addStep( RecipeStep( 'Serve Immediately.') )
        
        r.addToDoNote( 'Add code to print out notes..')
        
        r.addNote(
            "Pad Kee Mao is traditionally made with Holy Basil, which has a different fragrance "
            "from the Thai Basil is used, but Thai Basil is easier to find."
            )
        
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
