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
        r = MyRecipe('Palmiers', 'Dessert', sharedIngredentList)
        r.setPathLoc( dirPathRecipe )
        r.setRecipeFormat('TWO_COLUMN_OPTIONAL_PICTURES')  
        r.addPicture('sweet_palmiers', 'IMG_3563.jpeg')
        r.setPrimaryPicture('sweet_palmiers')
        
        #  -- Add Ingredients --
        ##
        #--
        strGrpBase = "Shared"
        r.addIngredient('Blitz Puff Pastry', 0.5, 'batch', strGrpBase)
        
        strGrpSavory = "Savory Version"
        r.addIngredient('Mustard', 30, 'grams, Dijon', strGrpSavory)
        r.addIngredient('Smoked Paprika', 1, 'teaspoon', strGrpSavory)
        r.addIngredient('Parmesan Cheese', 50, 'grams, 1/2 cup', strGrpSavory)
        
        strGrpSweet = "Sweet Version"
        r.addIngredient('Chocolate Ganache', 0.25, 'batch', strGrpSweet)
        r.addIngredient('Granulated White Sugar', 50, 'grams', strGrpSweet)
        r.addIngredient('Cinnamon', 20, 'grams', strGrpSweet)
        
        # Add Steps and Notes
        r.addStep(RecipeStep('Preheat oven to 400 deg F. Line a baking sheet with parchment paper.'))
        r.addStep(RecipeStep('On a lighly floured surface, roll out the blitz puff pastry dough to an 8"x12" rectangle, about 1/8" thick.'))
        
        r.addStep(RecipeStep('For Savory',childStep=[
            RecipeStep('In a small bowl, stir together the mustard and paprika. Set aside.'),
            RecipeStep('Spread the mustard mixture in a thin, even layer to the edges of the pastry.'),
            RecipeStep('Sprinkle the parmesan evenly over the mustard.'),
        ]))
        
        r.addStep(RecipeStep('For Sweet',childStep=[
            RecipeStep('In a small bowl, stir together the sugar and cinnamon. Set aside.'),
            RecipeStep('Sprinkle the mixture over the pastry evenly.')
        ]))
            
        r.addStep(RecipeStep(
            'Using both hands, gently lift one long edge of the pastry and fold it over itself in 1" sections.'
            ' Alternate sides, until they both touch, forming a U shape.'
            ))
        r.addStep(RecipeStep('Slice the pastry into 1/2" thick slices. Place them about 2" apart on the pan.'))
        r.addStep(RecipeStep('Bake for 15 to 20 minutes or until puffed and deep golden brown.'))
        r.addStep(RecipeStep('For Sweet',childStep =[
            RecipeStep('Re-heat the ganache in the microwave. Dip 1/2 the palmiers in and sprinkle with sugar.')
        ]))
        r.addStep(RecipeStep('Transfer the palmiers to a wire rack to cool completely.'))
        
    
        # Notes
        
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
