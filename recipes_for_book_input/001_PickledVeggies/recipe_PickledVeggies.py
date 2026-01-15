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
        r = MyRecipe('Dill Pickles or Veggies', "Appetizers", sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('picklesDone', '2020_09_09_Pickles_post.jpg')
        r.addPicture('picklesReady', '2020_09_09_Pickles_pre.jpg')
        r.setPrimaryPicture( 'picklesDone')
        r.setRecipeFormat('FANCY_LONG_RECIPE')
        
        r.AddDescription(
            'Bilyana\'s Friend Lisa shared this with us, and it was one of our first experiments.'
            )
        #  -- Add Ingredients --
        r.addToDoNote( "Needs to list vegies for pickling - amounts")
        r.addToDoNote( "Jar sizes? used Kerr Wide Mouth Mason jars - not sure oz? 15 on glass on bottom.")
        
        ## Pickling liquid
        ingGrpName = "Pickling Liquid"
        r.addIngredient('Distilled White Vinegar', 1, 'quart', ingGrpName)
        r.addIngredient('Water', 3, 'quart', ingGrpName)
        r.addIngredient('Non-Iodized Salt', 1, 'cup', ingGrpName)
           
        ## Flavoring
        ingGrpName = "For inside the jars (1 per jar)"
        r.addIngredient('Garlic', 1, 'clove', ingGrpName)
        r.addIngredient('Grape Leaves', 1, 'leaf', ingGrpName)
        r.addIngredient('Celery seed', 0.25, 'teaspoon', ingGrpName)
        r.addIngredient('Dill', 0.25, 'teaspoon', ingGrpName)
        
        # Add Steps and Notes
        vegJarFullStep = RecipeStep("Load jar with vegetables")
        vegJarFullStep.attachPic( r.getPicturePath('picklesReady'))
        
        stepPrepVeg = RecipeStep(
            "Prepare the Veggies for Pickling",
            [   
                RecipeStep(
                    "Clean the pickling cucumbers and " 
                    "prick each with a fork in a few places"),
                RecipeStep(
                    "Snap the beans"),
                RecipeStep(
                    "Layer 1 clove garlic, 1 grape leaf, 1/4 tsp dill, 1/4 tsp celery seed."),
                vegJarFullStep,    
                ]
            )
        r.addStep( stepPrepVeg )
        
        stepPrepLiquid = RecipeStep(
            "Prepare the liquid",
            [
                RecipeStep(
                    "NOTE: Adjust this radio to match the number of Jars you plan to pickle."),
                RecipeStep(
                    "Mix 1 qt Vinegar, 3 qts water, 1 cup non-iodized salt"),
                RecipeStep(
                    "Bring to a boil")
                ]
            )
        
        r.addStep( stepPrepLiquid )
        stepPrepJar = RecipeStep(
            "In each Jar",
            [
                RecipeStep(
                    "Pour boiling pickling liquid to the top of the jar"),
                RecipeStep(
                    "Close jars firmly"),
                ]
            )
        r.addStep( stepPrepJar )
        
        stepSecure = RecipeStep(
            "Prep for storage",
            [
                RecipeStep(
                    "Fill a large pot with water, and bring to "
                    "a rolling boil. There should be enough water to cover "
                    "the jars, without spilling."),
                RecipeStep(
                    "Keep jars in for 10 minutes."),
                RecipeStep(
                    "Remove from water. Allow them to cool, and then store")
                ]
            )
        r.addStep( stepSecure )
        
        r.addStep( 
            RecipeStep(
                "The pickles can be used in as little as 1 month, "
                "however the original recipe calls for waiting 3 months."
                )
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
