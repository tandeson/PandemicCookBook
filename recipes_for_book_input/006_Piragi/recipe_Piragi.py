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
        r = MyRecipe('Pierogi (Piragi)', "Baking and Breads", sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.addPicture('PerogiBatch', '2020_08_25_PerogiBatch_edited.JPG')
        r.addPicture('PerogiInHalf', '2020_08_25_PerogiInHalf_edited.JPG')
        r.setPrimaryPicture( 'PerogiBatch')
        r.setRecipeFormat('FANCY_LONG_RECIPE') 
                
        r.AddDescription(
            'This recipe was shared with me by my friend Xenia Hertzenberg. We were co-workers at the '
            'time and I\'d used a Pizza Dough recipe to make something like Pierogi after a trip to a '
            'Russian bakery near Pike\'s Place Market. The next day she brought in this recipe from '
            'her uncle, who I think is Russian. ~Thomas'
            )
        #  -- Add Ingredients --

        ## Dough
        grpName = "for the dough"
        r.addIngredient('Whole Milk', 1.25, 'cups', grpName)
        r.addIngredient('Unsalted Butter', 12, 'tablespoons', grpName)
        r.addIngredient('Granulated White Sugar', 0.4, 'cups + 1 tsp', grpName)
        r.addIngredient('Salt', 1, 'teaspoon', grpName)
        r.addIngredient('Active Dry Yeast', 1, 'package (2 1/4 oz)',grpName)
        r.addIngredient('Bread Flour', 5, 'cups', grpName)
        
        grpNameFilling = "for the filling"
        r.addIngredient('Avocado Oil',1, 'tablespoon', grpNameFilling)
        r.addIngredient('Bacon', 1, 'lb, cut into 1/8" cubes', grpNameFilling)
        r.addIngredient('Ham', 0.5, 'lb, cut into 1/8" cubes', grpNameFilling)
        r.addIngredient('White Onion', 1, 'small, minced', grpNameFilling)
        r.addIngredient('Heavy Cream', 1, 'tablespoon', grpNameFilling)
        r.addIngredient('Eggs', 1, 'large', grpNameFilling)
        
        # Add Steps and Notes
        doughSteps = [
            'Heat milk, butter, 1/3 cup sugar and salt in a 2 quart '
            'saucepan over medium heat until sugar dissolves; set aside.',
            'Whisk together remaining sugar, yeast, and 1/4 cup warm water '
            ' in a bowl of a stand mixer fitted with a dough hook.',
            'Let the yeast mixture sit until foamy - about 10 minutes.',
            'Whisk in milk mixture, add flour, and mix on low speed until '
            'dough forms.',
            'Increase speed to medium-high and knead until smooth - about 8 minutes.',
            'Cover bowl with plastic wrap; let sit until doubled in size about 1 1/2 hours.'
            ]
        lstDoughSteps = []
        for s in doughSteps:
            lstDoughSteps.append( RecipeStep( s ) )
        r.addStep( RecipeStep('Make dough', lstDoughSteps) )
        
        fillingSteps = [
            'Heat oil in a 4-quart saucepan over medium heat.',
            'Add bacon/ham mixture. Cook stirring until fat renders - about 6 minutes.',
            'Add Onion and cook, stirring, until the onion is lighly caramelized'
            ' but bacon/ham is not crisp - about 6 minutes',
            'Remove from heat, season with salt and pepper.',
            'Let cool completely.'
            ]
        
        lstfillingSteps = []
        for s in fillingSteps:
            lstfillingSteps.append( RecipeStep( s ) )
        r.addStep( RecipeStep('Make filling', lstfillingSteps) )
        
        assembleBakeSteps = [
            'Heat oven to 400 deg F.',
            'Separate Egg into white and yoke.',
            'Make Egg wash by whisk together cream and egg yolk in a small bowl and '
            'set aside',
            'lighly beat egg white, and set aside',
            'Transfer dough to a floured work surface and cut in half.',
            'Work with one half at a time, roll the dough unti 1/4" thick.',
            'Using a 2 1/2" round cutter, cut out dough rounds.',
            'Place 1 teaspon of filling in center of each round.',
            'Using your fingers, moisten edges of round with egg white',
            'fold over to enclose filling, and pinch edges together to seal.',
            'Transfer turnovers, seam side down, to parchment paper '
            'lined baking sheet, spaced about 3" apart.',
            'Using a pastry brush, brush egg wash over each bun.',
            'Bake until golden brown, 12 - 15 minutes.'
            ]
        lstassembleBakeSteps = []
        for s in assembleBakeSteps:
            lstassembleBakeSteps.append( RecipeStep( s ) )
        r.addStep( RecipeStep('Assemble and Bake', lstassembleBakeSteps) )
        
        r.addStep( RecipeStep('Enjoy!'), ['PerogiInHalf'] )
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
