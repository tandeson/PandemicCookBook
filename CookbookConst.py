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

#*  Constants ****************************************************************

#*  Constants ****************************************************************

# Exit codes - "no error" must be 0
EXIT_OK, EXIT_ERR, EXIT_CTRL_C = range(3)

#*  Sections *****************************************************************
C_BOOK_SECTIONS = [
    'Spreads and Dips',
    'Appetizers',
    'Soups',
    'Salads',
    'Baking and Breads', 
    'Main dishes',
    'Dessert', 
]

## Consider:
# spreads and dips
# baked goods

#*  Sections *****************************************************************
C_RECIPE_FORMATING = [
    ## Default used at first creation
   'TWO_COLUMN_OPTIONAL_PICTURES',
   
   ## Taken from Web example 
   'FANCY_WIDE_PIC_OVER_DIRECTIONS',
   'FANCY_TALL_PIC_OVER_INSTRUCTIONS',
   ]

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
