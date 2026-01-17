#!/usr/bin/env python
#*****************************************************************************
#
"""
    Object that Represent an Ingredient
    
    CONSIDER: https://github.com/vizigr0u/sugarcube for units
              conversion.
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
from scripts.translation_runtime import translate_text

#*  Constants ****************************************************************
# PY-2.10
# DELIMITER = ","


#*  Class and Function Definitions *******************************************


#=============================================================================
class RecipeIngredient:
    """
    Represents a ingredient used in a recipe

    Held here so we can track back to which specifc one, and possible units?
    """

    #-------------------------------------------------------------------------
    def __init__(self, IngredientName, IngredientGroup, IngredientDescrption='',recipeToMakeName=None):
        """
        Create RecipeIngredient object.

        Description.
        """
        self.info = {
            'name': IngredientName,
            'group': IngredientGroup,
            'description': IngredientDescrption,
            'exampleVendors': [],
            'recipeList': {},
            'recipeToMakeName': recipeToMakeName
            }

    #-------------------------------------------------------------------------
    def getName(self):
        """
        Get the Name of this Ingredient

        returns:
            string - name
        """
        return self.info['name']

    #-------------------------------------------------------------------------
    def getDisplayName(self):
        """
        Get the translated name of this ingredient for output.
        """
        return translate_text(self.info['name'])
    
    #-------------------------------------------------------------------------
    def getGroup(self):
        """
        Get the Name of this Ingredient

        returns:
            string - name
        """
        return self.info['group']

    #-------------------------------------------------------------------------
    def getDisplayGroup(self):
        """
        Get the translated group name for output.
        """
        return translate_text(self.info['group'])
    
    #-------------------------------------------------------------------------
    def getRecipeToMake(self):
        '''
        Return the name of a recipe to make this - or None if there isn't any
        '''
        return self.info['recipeToMakeName']
    
    #-------------------------------------------------------------------------
    def addVendor(self, vendorName, vendorDescription, vendorLink):
        """
        One line description of method.

        args:
            argument descriptions

        returns:
            description of return objects
        """
        self.info['exampleVendors'].append( 
            {
                'name': vendorName,
                'description': vendorDescription,
                'link': vendorLink
                }
            )
    
    #-------------------------------------------------------------------------
    def inRecipe(self, recipeUsingThisIngredient):
        """
        Keeps track of which recipe use this ingredient.

        returns:
            string - name
        """
        if recipeUsingThisIngredient.getName() not in self.info['recipeList'].keys():
            self.info['recipeList'][recipeUsingThisIngredient.getName() ] = recipeUsingThisIngredient
    
    #-------------------------------------------------------------------------
    def getRecipeList( self ):
        """
        Get the list of recipes for this ingredeient
        """
        return self.info['recipeList']
        
    #-------------------------------------------------------------------------
    def genIngredientBlock(self, inAmount, inUnits, genOutFormat='html'):
        """
        One line description of method.

        args:
            argument descriptions

        returns:
            description of return objects
        """
        strBack = ''
        strAmnt = "%8.2f" % (inAmount)
        
        if ( genOutFormat == 'html_text'):    
            strLayout = "{0:6} {1:8} "
            strBack += strLayout.format(strAmnt, inUnits).replace(' ','&nbsp')
            strBack += self.getDisplayName()
            
        elif (genOutFormat == 'html'):
            strBack = str( '<tr>'
                '<td> %s </td>' % (strAmnt) +
                '<td>' + translate_text(inUnits) + '</td>' +
                '<td>' + self.getDisplayName() + '</td>' +
                '</tr>' )
        else:
            raise Exception(" Unable to generate format: %s" % ( genOutFormat) )
        
        return strBack

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
