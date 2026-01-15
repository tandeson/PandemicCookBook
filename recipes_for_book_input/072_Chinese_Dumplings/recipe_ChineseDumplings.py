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
        r = MyRecipe('Vegetarian Dumplings', 'Main dishes', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('DumplingDish', 'DumplingsOnPlate.JPEG')
        r.setPrimaryPicture( 'DumplingDish' )
        r.AddDescription(
            'We tried this recipe for Chinese New Year in 2021, and loved it! It\'s'
            ' based on a recipe from the blog "Two Red Bowls" ~Thomas')
        r.setRecipeFormat('FANCY_LONG_RECIPE')
        ## ---
        
        grpDough ="Dough"
        r.addIngredient('All Purpose Flour', 376, 'grams,~3 cups', grpDough)
        r.addIngredient('Salt', 0.75, 'teaspoon', grpDough)
        r.addIngredient('Water', 255, 'grams, boiling, ~1 cup', grpDough)

        
        grpFilling = "Filling"
        r.addIngredient('Napa Cabbage', 160, 'grams, stem removed', grpFilling)       
        r.addIngredient('Salt', 0.75, 'teaspoon', grpFilling)
        r.addIngredient('Veggie Grillers Crumbles', 227, 'grams', grpFilling)
        r.addIngredient('Red Onion', 25, 'grams, minced', grpFilling)
        r.addIngredient('Soy Sauce', 28, 'grams', grpFilling)
        r.addIngredient('Sesame Oil', 2, 'teaspoons', grpFilling)
        r.addIngredient('Rice Vinegar', 1, 'tablespoon', grpFilling)
        r.addIngredient('Garlic', 2, 'teaspoons, minced', grpFilling)
        r.addIngredient('Ginger', 1, 'teaspoons, minced', grpFilling)
        r.addIngredient('Sugar', 2, 'teaspoons', grpFilling)
        r.addIngredient('Corn Starch', 7, 'grams', grpFilling)

        
        # Add Steps and Notes
        r.addStep( 
            RecipeStep( "To make the dough",[
                RecipeStep(
                    'In a medium bowl, whisk together the flour and salt. Place a'
                    ' wet towel under the bowl to keep it from sliding, then '
                    'trickle the water into the flour while stirring with '
                    'chopsticks or a spatula.'),
                RecipeStep(
                    'After all the water is added, continue to stir until the mixture'
                    ' becomes shaggy and the water is fully incorporated.'),
                RecipeStep(
                    'Once the dough is cool enough to comfortably touch, knead it by hand'
                    ' until it\'s smooth and taut, about 5 to 10 minutes. It should be fairly'
                    ' firm, not tacky, and shouldn\'t stick to your hands or the bowl. If it\'s'
                    ' sticky, add a few more tablespoons of flour as you knead.'),
                RecipeStep(
                    'Place the dough in an airtight container or zip-top bag and allow it to rest'
                    ' at room temperature for 15 to 30 minutes; or refrigerate up to 1 day.'),
                ] 
            )
        )
        
        r.addStep( 
            RecipeStep( "To make the filling",[
                RecipeStep(
                    'Rinse the cabbage, pat dry, then sprinkle 1/4 teaspoon salt over the cabbage and '
                    'let it sit for 10 to 15 minutes, or until it wilts and releases water. Squeeze the'
                    ' cabbage to drain the liquid. Salting the cabbage beforehand avoids soggy dumplings later.'),
                RecipeStep(
                    'In a medium bowl, mix together the drained cabbage, remaining 1/2 teaspoon salt, veggie '
                    'crumble, onion, soy sauce, sesame oil, rice vinegar, garlic, ginger, and sugar. Sprinkle'
                    ' the cornstarch evenly over the mixture and mix again until well combined. Cover and '
                    'refrigerate while you roll out the dumpling wrappers, no longer than 1 to 2 hours.'),
                ]
            )
        )
        
        r.addStep( 
            RecipeStep( "To shape the dumplings",[
                RecipeStep(
                    'Divide the dough into six pieces. Work with one piece at a time, with the remaining pieces '
                    'kept covered or in a sealed container.'),
                RecipeStep(
                    'Roll one piece of dough into a short cylinder about 1" in diameter. Cut the dough into six '
                    'to eight pieces (fewer for thicker wrappers and more for thinner ones).'),
                RecipeStep(
                    'Use a small rolling pin, dowel, or pastry pin to roll each slice of dough into a circle about'
                    ' 3 1/2" to 4" in diameter. Try to make the edges a little thinner than the center. Flour '
                    'generously and set aside, covered. Repeat with the rest of the dough.'),
                RecipeStep(
                    'Place 2 to 3 teaspoons of filling in the center of a wrapper. Dampen one half of the '
                    'wrapper\'s edge with water.'),
                RecipeStep(
                    'Fold the wrapper in half around the filling and pinch only the center together, leaving the'
                    ' ends open. Bring the open edges to the center, also, and pinch where the edges meet each other,'
                    ' creating four seams in a cross shape. Set aside and cover with a damp towel while you fold the rest.'),
                ]
            )
        )
        
        r.addStep( 
            RecipeStep( "To boil the dumplings",[
                RecipeStep(
                    'Bring a large, shallow pot of water to a boil. Add as many dumplings as can comfortably fit in a single '
                    'layer in the pot and let cook until the dumplings float, about 3 minutes. Simmer for 2 minutes more, until'
                    ' cooked through, then transfer to a plate and repeat with any remaining dumplings.'),
                RecipeStep('Quickly Fry the dumpling on medium heat unitl the outside browns just a little, and retun to the plate.'),
                RecipeStep('Serve warm. Refrigerate any leftovers, well wrapped, for several days; freeze for longer storage.'),
                ] 
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
