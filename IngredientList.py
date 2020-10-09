#!/usr/bin/env python
#*****************************************************************************
#
"""
    What does this do?
"""
#
#*****************************************************************************
#   Use of the software source code and warranty disclaimers are
#   identified in the Software Agreement associated herewith.
#*****************************************************************************

#*  Imports ******************************************************************
import sys
from scripts.recipeIngredient import RecipeIngredient

#*  Constants ****************************************************************

# Exit codes - "no error" must be 0
EXIT_OK, EXIT_ERR, EXIT_CTRL_C = range(3)

C_INGREDIENTS = []

#=============================================================================
## Packaged goods
grpNameCanned = 'Canned Goods'

C_INGREDIENTS.append( RecipeIngredient(
    'Dry Wide Rice Noodles',
    grpNameCanned
    ))

grapeLeavesPickled = RecipeIngredient(
    'Grape Leaves',
    grpNameCanned, 
    'Pickled, used as a flavor or wrapping for meats, veggies, rice, etc.'
    )
grapeLeavesPickled.addVendor(
    'Orlando Grape Leaves 8 0z',
    'A Common example of pickled grape leaves, usually 8 oz is enough for most of our uses.',
    'https://www.amazon.com/Orlando-Grape-Leaves-0z-Pack/dp/B07CQBNYG7'
    )
C_INGREDIENTS.append( grapeLeavesPickled )

#=============================================================================
grpNameCondiments = 'Condiments'

C_INGREDIENTS.append( RecipeIngredient( 
    'Apple Cider Vinegar',
     grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Distilled White Vinegar', 
     grpNameCondiments,
    'Generic white vinegar, usually just from the local supermarket.'
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Evaporated Cane Sugar', 
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Fish Sauce',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Oyster Sauce',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Rice Vinegar',
    grpNameCondiments, 
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Soy Sauce',
    grpNameCondiments, 
    ))
#=============================================================================
grpNameDairy = 'Dairy'

C_INGREDIENTS.append( RecipeIngredient(
    'Heavy Cream',
    grpNameDairy,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Whole Milk',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Unsalted Butter',
    grpNameDairy,
    ))
#=============================================================================
grpNameDryGoods = 'Dry Goods'

C_INGREDIENTS.append( RecipeIngredient(
    'Active Dry Yeast',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'All Purpose Flour',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Baking Soda',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Bread Flour',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(    
    'Black-Eyed Peas',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Brown Sugar',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Butterscotch chips',
    grpNameDryGoods,
    ))
         
C_INGREDIENTS.append( RecipeIngredient(
    'Corn Starch',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Dark Chocolate chips',
    grpNameDryGoods,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Sugar',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Granulated White Sugar',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Oatmeal',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Rice Crispies',
    grpNameDryGoods,
    ))

#=============================================================================
grpNameHousehold = 'Household'

C_INGREDIENTS.append( RecipeIngredient(
    'Water',
    grpNameHousehold,
    ))

#=============================================================================
grpNameProtien = 'Meat, Poultry, Fish, Eggs, Tofu'

C_INGREDIENTS.append( RecipeIngredient(
    'Bacon',
    grpNameProtien
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Eggs',
    grpNameProtien
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Fried Tofu', 
    grpNameProtien
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Ham', 
    grpNameProtien
    ))
    
#=============================================================================
grpNameOils = 'Oils'

C_INGREDIENTS.append( RecipeIngredient(
    'Avocado Oil',
    grpNameOils
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Extra Virgin Olive Oil',
    grpNameOils, 
    'Other olive oils can be used, but extra virgin is pressed without chemicals used to strip out the oil.'
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Vegetable Oil',
    grpNameOils
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Shortening',
    grpNameOils
    ))
#=============================================================================
grpNameProduce = 'Produce'

C_INGREDIENTS.append( RecipeIngredient(
    'Bird Chillies',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Carrot',
    grpNameProduce
    ))

C_INGREDIENTS.append(RecipeIngredient(
    'Fresh Green Beans',
    grpNameProduce, 
    'typically a whole head from the local supermarket.'
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Garlic',
    grpNameProduce, 
    'typically a whole head from the local supermarket.'
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Onion',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Pickling Cucumbers',
    grpNameProduce,
    'typically in the fresh produce section at the supermarket, or found in farmer\'s markets.'
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Red Bell Pepper',
    grpNameProduce
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Red Onion',
    grpNameProduce
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Tomatoes',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'White Onion',
    grpNameProduce,
    ))
      
#=============================================================================
## Spices
grpNameSpices = "Spices"

C_INGREDIENTS.append( RecipeIngredient(
    'Asafetida',
    grpNameSpices, 
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Cayenne Pepper',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Coriander Powder',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Celery seed',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(   
   'Cumin Seeds',
    grpNameSpices, 
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Dill',
    grpNameSpices,
    'Spice - can be dryed or fresh. Easy to grow in the WA area.'
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Garam Masala',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Lemon Juice',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Non-Iodized Salt',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Salt',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Thai Basil',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Turmeric',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Vanilla',
    grpNameSpices,
    ))
#=============================================================================
#=============================================================================
def main(argv=None):
    """
    Parse arguments, report start & stop time, and run the test.
    """
    return EXIT_OK

#*  Main Code Path ***********************************************************
if __name__ == "__main__":
    # Exit code is main() return value
    # (see http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
    sys.exit(main())

#*****************************************************************************
#*****************************************************************************
