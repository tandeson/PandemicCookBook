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
        r = MyRecipe('New York Style Cheesecake', 'Dessert', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.setRecipeFormat('FANCY_TALL_PIC_OVER_INSTRUCTIONS')  
        
        r.AddDescription(
            'This recipe was shared with me by Lindsay Bruce back in college. It comes '
            'from her father, who spent his life in restaurant kitchens. It\'s been a '
            'standby for years. It can easily be modified by adding toppings like raspberries or '
            'chocolate. ~Thomas'
        )
        #  -- Add Ingredients --
        
        ## 
        grpCrust = "Graham Cracker Crust"
        r.addIngredient('Graham Cracker Crumbs', 1.5 , 'cup', grpCrust)
        r.addIngredient('Granulated White Sugar', 0.3 , 'cup', grpCrust)
        r.addIngredient('Salted Butter', 0.3, 'cups', grpCrust)
        
        grpFilling = "Filling"
        r.addIngredient('Cream Cheese', 40 , 'oz, softened', grpFilling)
        r.addIngredient('Whipping Cream', 0.25, 'cup', grpFilling)
        r.addIngredient('Eggs', 5, 'large', grpFilling)
        r.addIngredient('Eggs Yolks', 2, 'large', grpFilling)
        r.addIngredient('Granulated White Sugar', 2 , 'cups', grpFilling)
        r.addIngredient('Lemon', 1, 'medium, zest and juice', grpFilling)
        r.addIngredient('All Purpose Flour', 2 , 'tablespoons',grpFilling)
        r.addIngredient('Vanilla', 1, 'teaspoon', grpFilling)
        

        # Add Steps and Notes
        r.addStep( RecipeStep( 
            'Make the Crust.', [
            RecipeStep( 'Preheat Oven to 350 deg F.'),
            RecipeStep( 'Mix the Graham Cracker Crumbs, Sugar and Butter together in a bowl.'),
            RecipeStep( 'Gently press the mixture into the bottom of a 9" spring form pan. Use a spoon to smooth.'),
            RecipeStep( 'Bake for 8-10 minutes, and set aside.')
            ]
            ))
        
        r.addStep( RecipeStep( 'Preheat the oven to 325 deg F.') )
        r.addStep( RecipeStep( 
            'Combine all the filling ingredients in a bowl - Cream Cheese, Heavy Cream, Eggs, Sugar, Lemon, Flour and Vanilla. '
            'Mix until combined, but no more, as extra air in the mix will cause cracking.'
            ))
        r.addStep( RecipeStep('Pour the filling mixture into the crust.') )
        r.addStep( RecipeStep(
            'Create a cover for the bottom of the springform pan using layers of plastic wrap and aluminum foil. '
            'Make 4 to 6 layers. This will allow the cake to sit in a water bath during baking.'))
        r.addStep( RecipeStep(
            'Fill a cookie sheet with water and place in the oven. Set the cake pan in the water bath. Bake for 1 hour and 45'
            ' minutes.'))
        r.addStep( RecipeStep('Cool for at least 6 hours.'))
        
            
        
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
