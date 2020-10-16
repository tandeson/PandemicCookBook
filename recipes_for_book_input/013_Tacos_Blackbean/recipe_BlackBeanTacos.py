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
        
        GrpNameTaco = "Taco Shells"
        r.addIngredient('Corn Tortillas', 8, 'qty', GrpNameTaco)
        r.addIngredient('Extra Virgin Olive Oil', 2 , 'tablespoons', GrpNameTaco)
        
        GrpNameCondiments = "Condiments"
        r.addIngredient('Romaine Lettuce', 0.25, 'head, chopped', GrpNameCondiments)
        r.addIngredient('Feta Cheese', 3, 'oz', GrpNameCondiments)
        ## Pickled Onions
        ## Pickled Jalapeanos
           
        # Add Steps and Notes
        steps = [
            '...',
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
