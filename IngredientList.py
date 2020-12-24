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
grpNameAlcohol = 'Alcohol'

C_INGREDIENTS.append( RecipeIngredient(
    'Wine',
    grpNameAlcohol,
    ))

#=============================================================================
## Packaged goods
grpNameCanned = 'Canned Goods'

C_INGREDIENTS.append( RecipeIngredient(
    'Artichoke Hearts',
    grpNameCanned,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Black Beans',
    grpNameCanned,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Black Olives',
    grpNameCanned,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Capers',
    grpNameCanned,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Chickpeas',
    grpNameCanned,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Coconut Milk',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Diced Tomatoes',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Dry Wide Rice Noodles',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Enchilada Sauce',
    grpNameCanned,
    'Usually I get Las Palmas mild or medium sauce. '
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

C_INGREDIENTS.append( RecipeIngredient(
    'Kidney Beans',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Marinara Sauce',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Peanut Butter',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Pizza Sauce',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Pumpkin Puree',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Sauerkraut',
    grpNameCanned
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Tomato Paste',
    grpNameCanned
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Worcestershire Sauce',
    grpNameCanned
    ))


#=============================================================================
grpNameCondiments = 'Condiments'

C_INGREDIENTS.append( RecipeIngredient( 
    'Agave Nectar',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Apple Cider Vinegar',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Apricot Preserves',
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
    'Honey',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Molasses',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Mustard',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Oyster Sauce',
    grpNameCondiments,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Pickles',
    grpNameCondiments, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Pickled Jalapenos',
    grpNameCondiments, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Red Wine Vinegar',
    grpNameCondiments, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Pickled Red onions',
    grpNameCondiments, 
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Rice Vinegar',
    grpNameCondiments, 
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Sriracha',
    grpNameCondiments, 
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Soy Sauce',
    grpNameCondiments, 
    ))
#=============================================================================
grpNameDairy = 'Dairy'

C_INGREDIENTS.append( RecipeIngredient(
   'Blue Cheese',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
   'Brie',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Buttermilk',
    grpNameDairy,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Cheddar Cheese',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
   'Cottage Cheese',
   grpNameDairy,
    ))
   
C_INGREDIENTS.append( RecipeIngredient(
   'Cream Cheese',
   grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Evaporated Milk',
    grpNameDairy,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
   'Feta Cheese',
   grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Greek Yogurt',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Heavy Cream',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Parmesan Cheese',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Salted Butter',
    grpNameDairy,
    ))

C_INGREDIENTS.append( RecipeIngredient(
   'Shredded Mexican Cheese',
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

C_INGREDIENTS.append( RecipeIngredient(
    'Whipping Cream',
    grpNameDairy,
    ))
    
#=============================================================================
grpNameDryGoods = 'Dry Goods'

C_INGREDIENTS.append( RecipeIngredient(
    'Arborio Rice',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Active Dry Yeast',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'All Purpose Flour',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Almond Flour',
    grpNameDryGoods,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Bakers Special Dry Milk',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Baking Powder',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Baking Soda',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Bread',
    grpNameDryGoods,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Breadcrumbs',
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
    'Brown Lentils',
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
    'Cashews',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Coconut Flour',
    grpNameDryGoods,
    ))
   
C_INGREDIENTS.append( RecipeIngredient(
    'Corn Starch',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Corn Tortillas',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Dark Chocolate chips',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(    
    'Diastatic Malt Powder',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Doritos',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'French\'s Original Crispy Fried Onions',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Graham Cracker Crumbs',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Granulated White Sugar',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Instant Yeast',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Oatmeal',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Orzo',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Peanuts',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
   'Powdered Sugar',
    grpNameDryGoods,
    ))
   
C_INGREDIENTS.append( RecipeIngredient(
    'Pistachios',
    grpNameDryGoods,
    ))
    
dryPizzaDoughFlavor = RecipeIngredient(
    'Pizza Dough Flavor',
    grpNameDryGoods
    )
dryPizzaDoughFlavor.addVendor(
    'King Arthur Baking', 
    'For over the top flavor in your homemade pizza or Italian bread dough. Features cheese powder, garlic, and natural flavors.',
     'https://shop.kingarthurbaking.com/items/pizza-dough-flavor-4-oz')
C_INGREDIENTS.append( dryPizzaDoughFlavor )
 
C_INGREDIENTS.append( RecipeIngredient(
    'Potato Flour',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Quinoa',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Red Cabbage',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Red Lentils',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Rice',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Rice Crispies',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Rye Flour',
    grpNameDryGoods,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Split Peas',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Sugar',
    grpNameDryGoods,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Walnuts',
    grpNameDryGoods,
    ))

#=============================================================================
grpNameHousehold = 'Household'

C_INGREDIENTS.append( RecipeIngredient(
    'Water',
    grpNameHousehold,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Sourdough Starter',
    grpNameHousehold,
    ))

#=============================================================================
grpNameProtien = 'Meat, Poultry, Fish, Eggs, Tofu'

C_INGREDIENTS.append( RecipeIngredient(
    'Bacon',
    grpNameProtien
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Chopped Clams',
    grpNameProtien
    ))

C_INGREDIENTS.append( RecipeIngredient( 
    'Eggs',
    grpNameProtien
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Eggs Yolks',
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

C_INGREDIENTS.append( RecipeIngredient(
    'Tofu',
    grpNameProtien
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Veggie Grillers Crumbles',
    grpNameProtien,
    'I Commonly use MorningStar farms, this is a replacement for ground beef.'
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
    'Sesame Oil',
    grpNameOils
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Shortening',
    grpNameOils
    ))

#=============================================================================
grpNameOther = 'Other'

C_INGREDIENTS.append( RecipeIngredient(
    'Mayonnaise',
    grpNameOther
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Premade Pastry Shell',
    grpNameOther
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Peas',
    grpNameOther
    ))
        
C_INGREDIENTS.append( RecipeIngredient(
    'Pizza Dough',
    grpNameOther,
    recipeToMakeName='Sourdough Pizza Dough'
    ))


#=============================================================================
grpNameProduce = 'Produce'

C_INGREDIENTS.append( RecipeIngredient(
    'Apples',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Avocados',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Banana',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Bird Chillies',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
   'Blueberries',
   grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Broccoli',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Brussel Sprouts',
    grpNameProduce
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Carrot',
    grpNameProduce
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Cauliflower',
    grpNameProduce
    ))

C_INGREDIENTS.append(RecipeIngredient(
    'Celery',
    grpNameProduce, 
    ))

C_INGREDIENTS.append(RecipeIngredient(
    'Cilantro',
    grpNameProduce, 
    ))

C_INGREDIENTS.append(RecipeIngredient(
    'Collard Greens',
    grpNameProduce, 
    ))

C_INGREDIENTS.append(RecipeIngredient(
    'Cucumber',
    grpNameProduce, 
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
    'Ginger',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Green Chillies',
    grpNameProduce,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Jalapeno Pepper',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Kale',
    grpNameProduce,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Leek',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Lemon',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Lime',
    grpNameProduce,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Mushrooms',
    grpNameProduce,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Onion',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Parsley',
    grpNameProduce,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Pickling Cucumbers',
    grpNameProduce,
    'typically in the fresh produce section at the supermarket, or found in farmer\'s markets.'
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Potato',
    grpNameProduce
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
    'Roma Tomato',
    grpNameProduce
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Romaine Lettuce',
    grpNameProduce
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Serrano Chile',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Spinach',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Sweet Potatoes',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Tomatoes',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'White Onion',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Yellow Onion',
    grpNameProduce,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Zucchini',
    grpNameProduce,
    ))
      
#=============================================================================
## Spices
grpNameSpices = "Spices"

C_INGREDIENTS.append( RecipeIngredient(
    'Ancho Chili powder',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Asafetida',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Bebere',
    grpNameSpices, 
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Black Mustard Seeds',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Black Pepper',
    grpNameSpices, 
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Cardamom',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Cayenne Pepper',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Chili powder',
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
    'Cinnamon',
    grpNameSpices, 
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Cream of Tartar',
    grpNameSpices, 
    ))
    
C_INGREDIENTS.append( RecipeIngredient(   
    'Cumin',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(   
   'Cumin Seeds',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Curry Leaves',
    grpNameSpices, 
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Curry Powder',
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
    'Garlic Powder',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Green Onion',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Italian Seasoning',
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
    'Nutmeg',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Onion Powder',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Oregano',
    grpNameSpices,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Paprika',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Poultry Seasoning',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Red Pepper Flakes',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Rosemary',
    grpNameSpices,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Salt',
    grpNameSpices,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Sea Salt',
    grpNameSpices,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Smoked Paprika',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Sesame seeds',
    grpNameSpices,
    ))
    
C_INGREDIENTS.append( RecipeIngredient(
    'Thai Basil',
    grpNameSpices,
    ))

C_INGREDIENTS.append( RecipeIngredient(
    'Thyme',
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

C_INGREDIENTS.append( RecipeIngredient(
    'Vegetable Broth',
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
