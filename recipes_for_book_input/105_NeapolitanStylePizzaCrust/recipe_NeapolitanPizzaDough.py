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
        r = MyRecipe('Neopolitan Pizza Dough', 'Baking and Breads', sharedIngredentList)
        r.setPathLoc(dirPathRecipe)
        r.addPicture('Pizza', 'IMG_3019.jpeg')
        r.setPrimaryPicture('Pizza')
        #  -- Add Ingredients --

        ##
        r.addIngredient('Bread Flour', 2, 'cups, 232 grams')
        r.addIngredient('Instant Yeast', 0.25 , 'teaspoon')
        r.addIngredient('Sugar', 0.5, 'tablespoons')
        r.addIngredient('Salt', 1.25, 'teaspoon, 8 grams')
        r.addIngredient('Water', 0.75 ,'cup, 170 grams, warm')
        
        ## Steps
        steps = [
            'In a medium bowl, mix the dry ingredients, then add the water. Stir until just combined, making a rough but cohesive dough.',
            'Cover the bowl and allow the dough to rise at room temperature overnight, for at least 12 hours and up to 24 hours.',
            
            'Place a rack in the center of your oven and preheat the oven to 500 deg F to 550 deg F (if your oven goes to 550 deg F) with a baking steel or stone inside. '
            'The position of the rack is important, particularly if you\'re using parchment paper - too close to the broiler (you need at least 8" clearance) and the top '
            'of your pizza (and any visible edges of parchment) will burn before the bottom has had time to bake through. Make sure your oven is at the required '
            'temperature for at least 30 minutes before baking, so the steel or stone can fully preheat.',
            
            'Divide the dough in half. Working with one piece at a time, transfer the dough to a well-floured surface.',
            
            'Stretch and fold it, as follows: holding onto the dough at both ends, pull one end away from the other, then fold it back onto itself. Repeat on the other side. '
            'The dough will likely be sticky - don\'t worry about it looking neat as you fold. Be sure to keep your hands floured as you work. Repeat this process on the other '
            'side of the dough, so that all four corners of the dough have been stretched and folded. Next, pull the ends of the dough towards the middle, then turn it over. '
            'Using your fingers, pull the dough under itself to make a smooth, round ball with the seams tucked into the bottom.',
            
            'Repeat with the second piece of dough, and place each ball seam-side down into a floured bowl.',
            
            'Cover the bowls and allow the dough to rise for 45 minutes to an hour, while your oven preheats. In colder weather, place the bowls on the stove top (above the preheating oven) to stay warm.',
            
            'Generously flour a wooden peel, rubbing flour into the board to completely coat. If you\'re using a metal peel, or if this is your first attempt at homemade pizza, place a piece of parchment '
            'on your peel instead of using flour.',
            
            'Scoop the risen dough onto a well-floured work surface seam-side down (a bowl scraper is helpful here), using care to shape it as round as possible for easier stretching. If the dough feels '
            'wet, use a generous dusting of flour on top. For dough that feels drier, use slightly less flour.',
            
            'Use your fingertips to gently depress the dough, being careful not to touch the outer edge of the crust. This step is important - leaving the circumference untouched '
            'at this stage will result in a beautiful bubbly outer crust post-bake.',
            
            'Again, using care to not touch the outermost edge of the crust, lift the pizza from the work surface and use your knuckles to gently stretch the dough into a 10" to 12" '
            'circle. If the dough is at all sticky, use more flour. Use two hands at once to gently move the dough in a circle, allowing gravity to perform the stretch. Gravity is your '
            'friend! Let it do most of the work for you, as pulling will stretch the center more than the edges. If you find your dough is difficult to stretch, set it down on a floured '
            'surface for 5 to 10 minutes to allow the gluten to relax. Move the dough to the floured peel (or floured sheet of parchment) and adjust it so none is hanging off the edge. '
            'Remember - if the dough is sticky when you put it on the peel, it will stick to the peel! Make sure it\'s well-floured.',
            
            'Lightly sauce the dough, then top with the cheese of your choice. Add additional toppings as desired. Turn on the top broiler in your preheated oven, and transfer the pie '
            'to your preheated steel or stone.',
            
            'Gently slide pizza and parchment onto the steel or stone. The parchment will blacken around any edges showing, but remain intact under the pizza.',
            
            'Bake the pizza for approximately 6 minutes on the steel or 7 minutes on the stone (give or take), until bubbly and charred around the edges. Remove the pizza from the '
            'oven, and top it with fresh basil leaves, if desired. Repeat with the remaining dough and toppings.'
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
