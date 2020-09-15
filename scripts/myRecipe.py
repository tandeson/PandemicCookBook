#!/usr/bin/env python
#*****************************************************************************
#
"""
    One-line summary of file purpose.
"""
#
#*****************************************************************************
#   Use of the software source code and warranty disclaimers are
#   identified in the Software Agreement associated herewith.
#*****************************************************************************

# For 'gen' tools, we can use version as documentation.
version = '$Revision$'[1:-2]

#*  Imports ******************************************************************
# from {module} import {function}
import sys

#*  Constants ****************************************************************
# PY-2.10
# DELIMITER = ","


#*  Class and Function Definitions *******************************************

#=============================================================================
class MyRecipe:
    """
    An object that collects everything needed to make a recipe

    Description of class: Low-level design, physical design
    discussions, build dependencies, assumptions, implementation
    issues, notes, etc.
    """

    #-------------------------------------------------------------------------
    def __init__(self, recipeName, sharedIngredientList):
        """
        Create MyRecipe object.

        Class that holds info about  a recipe
        """
        self.info = {
            'name': recipeName,
            'ingredients': [],
            'steps': [],
            'notes': [],
            }
        self.ingredients = sharedIngredientList
    
    #-------------------------------------------------------------------------
    def getName(self):
        """
        Get the Name of this Ingredient

        returns:
            string - name
        """
        return self.info['name']
    
    #-------------------------------------------------------------------------
    def addIngredient(self, ingredientName ):
        """
        Add an Ingredient to a recipe. 
        
        TODO( TA, "How to keep track of usage? - Auto by steps?" )

        args:
            ingredientName: Name of the Ingredient, needs to match data in C_INGREDIENTS

        returns:
            None
        """
        thisIngredientInfo = None
        for knownIngredient in self.ingredients:
            if ingredientName == knownIngredient.getName():
                thisIngredientInfo = knownIngredient
                break
        
        if (None == thisIngredientInfo):
            raise Exception(
                " ** Ingredient: %s is not in the list of Ingredient in C_INGREDIENTS. **\n" % 
                (ingredientName) 
                )
        
        knownListIng = []
        for alreadyAddedIngredient in self.info['ingredients']:
            knownListIng.append( alreadyAddedIngredient.getName() )
        
        if ingredientName not in knownListIng:
            self.info['ingredients'].append( thisIngredientInfo )
            thisIngredientInfo.inRecipe( self )
                
    
    #-------------------------------------------------------------------------
    def method(self):
        """
        One line description of method.

        args:
            argument descriptions

        returns:
            description of return objects
        """
        pass


#=============================================================================
def function():
        """
        One line description of method.

        args:
            argument descriptions

        returns:
            description of return objects
        """



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
