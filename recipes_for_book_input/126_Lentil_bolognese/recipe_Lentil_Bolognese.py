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
        
        r = MyRecipe('Lentil Bolognese', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')
        r.addPicture('LentilBolognese', 'lentil-bolognese-1.jpg')
        r.setPrimaryPicture('LentilBolognese')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Extra Virgin Olive Oil', 1.5, 'tablespoons')
        r.addIngredient('Onion', 1, 'large, diced')
        r.addIngredient('Garlic', 5, 'cloves, diced')
        r.addIngredient('Oregano', 1, 'teaspoon')
        r.addIngredient('Thyme', 1, 'teaspoon')
        r.addIngredient('Sea Salt', 1.5, 'teaspoon')
        r.addIngredient('Black Pepper', 1, 'pinch to taste')
        r.addIngredient('Tomato Paste', 5.3, 'oz tube, 150 grams')
        r.addIngredient('Wine', 0.5, 'cups, Red (optional)')
        r.addIngredient('Vegetable Broth', 3, 'cups')
        r.addIngredient('Red Lentils', 1, 'cup, soaked')
        r.addIngredient('Walnuts', 0.25, 'cups, crushed fine')
        r.addIngredient('Tomatoes',14, 'oz can, crushed')
        
        r.addIngredient('Pasta', 16, 'oz, tube - rigatoni or penne rigate, etc')
        r.addIngredient('Balsamic Vinegar', 1, 'tablespoon')
        r.addIngredient('Parsley', 1, 'bunch, italian, chopped')
           

        
        # Add Steps and Notes
        steps= [
            'Soak the 1 cup of lentils in water for 30 minutes, or up to 60 minutes. Meanwhile, '
            'prep all the other ingredients (i.e., chop the onions and garlic, chop the walnuts, '
            'etc.)',
            
            'Heat a deep pan on medium-high heat. Add the olive oil, and once it’s shimmering, add '
            'the onions and season with a pinch of salt. Stir occasionally and cook the onions until '
            'a light brown fond starts form on the surface of the pan, about 5 minutes. Add a few spoons '
            'of water to deglaze the pan, and stir. Continue cooking the onions, adding more water every '
            'few minutes and stirring frequently to prevent burning, until the onions are softened and '
            'golden brown, 9-10 minutes.',
            
            'Add the garlic, thyme, oregano, 1 1/2 teaspoons salt, and pepper to taste. Stir frequently '
            'and cook for 60-90 seconds.',
            
            'Stir in the tomato paste and cook for 2-3 minutes to caramelize, stirring very frequently, '
            'until it’s darker red in color.',
            
            'If using the red wine, pour the wine into the pan and deglaze, scraping up any browned bits. '
            'Cook for 1-2 minutes, until the smell of alcohol has burned off and the mixture is jammy.',
            
            'Pour in the broth to deglaze the pan, stirring any browned bits on the bottom of the pot '
            'and stirring the broth into the tomato paste to combine. Add the lentils and walnuts, and '
            'stir to incorporate. Heat until the mixture comes to a boil, then reduce the heat to '
            'medium-low to maintain a rapid simmer for 20 minutes, stirring occasionally.',
            
            'Add the crushed tomatoes and simmer for another 15-20 minutes, or until the lentils are tender '
            'but still al dente, stirring occasionally to prevent burning and sticking.',
            
            'Meanwhile, bring a large pot of water to a boil and salt generously. Add the pasta and cook until '
            'just al dente. Reserve a ladle or so of pasta water (may not need it). Drain the pasta but do not '
            'rinse it.',
            
            'Add the hot cooked pasta to the bolognese and toss until well coated in the sauce, adding a bit of '
            'pasta water as needed to ensure the sauce coats the noodles. Garnish with chopped parsley or basil, '
            'if using.',
        ]
        
        for s in steps:
            r.addStep( RecipeStep( s ) )

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
