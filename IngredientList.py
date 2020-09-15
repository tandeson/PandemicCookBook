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
## Liquids

C_INGREDIENTS.append( 
    RecipeIngredient( 
        'Distilled Vinegar White', 
        'Generic white vinegar, usually just from the local supermarket.'
        )
    )

C_INGREDIENTS.append(
    RecipeIngredient(
        'Tap Water', 
        ''
        )
    )

#=============================================================================
## Packaged goods

grapeLeavesPickled = RecipeIngredient(
    'Grape Leaves', 
    'Pickled, used as a flavor or wrapping for meats, veggies, rice, etc.'
    )
grapeLeavesPickled.addVendor(
    'Orlando Grape Leaves 8 0z',
    'A Common example of pickled grape leaves, usually 8 oz is enough for most of our uses.',
    'https://www.amazon.com/Orlando-Grape-Leaves-0z-Pack/dp/B07CQBNYG7'
    )
C_INGREDIENTS.append( grapeLeavesPickled )

#=============================================================================
## Produce

C_INGREDIENTS.append(
    RecipeIngredient(
        'Garlic', 
        'typically a whole head from the local supermarket.'
        )
    )

C_INGREDIENTS.append(
    RecipeIngredient(
        'Fresh Green Beans', 
        'typically a whole head from the local supermarket.'
        )
    )

C_INGREDIENTS.append(
    RecipeIngredient(
        'Pickling Cucumbers', 
        'typically in the fresh produce section at the supermarket, or found in farmer\'s markets.'
        )
    )

#=============================================================================
## Spices

C_INGREDIENTS.append(
    RecipeIngredient(
        'Celery seed', 
        ''
        )
    )
    
C_INGREDIENTS.append(
    RecipeIngredient(
        'Dill', 
        'Spice - can be dryed or fresh. Easy to grow in the WA area.'
        )
    )

C_INGREDIENTS.append(
    RecipeIngredient(
        'Non-Iodized Salt', 
        ''
        )
    )

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
