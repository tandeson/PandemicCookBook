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
import os

from pathlib import Path

## HTML Helper functions
from scripts.html_helpers import makeHtmlEmbedImgFromFile
from CookbookConst import C_BOOK_SECTIONS, C_RECIPE_FORMATING

from pylatex import Itemize, Figure, Command, NewLine, NoEscape, Package
from pylatex.utils import bold

## TODO - TEMP RMEOVE?
from scripts.CreateLaTexOut import buildPdfImg

#*  Constants ****************************************************************
# PY-2.10
# DELIMITER = ","


#*  Class and Function Definitions *******************************************

#=============================================================================
class RecipeStep:
    """
    Represents a Step in a recipe

    needs to be pretty .. flexalbe.
    """
    #-------------------------------------------------------------------------
    def __init__(self, directionText, childStep = [] ):
        """
        Created a new Recipe Step!
        
        use the string format rules to place ingredient text. as in "mix in {} to {}".
         - This allows the ingreident object to control the units and formatting.
        """
        self.info = {
            'inText':directionText,
            'childStep': childStep,
            'inPic': []
        }
    
    #-------------------------------------------------------------------------
    def attachPic(self, picPath):
        """
        Attached a picture to this step
        """
        self.info['inPic'].append( picPath )
        
    #-------------------------------------------------------------------------
    def genStepBlock(self, genOutFormat='html', baseFilePath='', LaTexDoc=None, callDepth=0, LaTexItemize=None):
        """
        Generate the formatted for the steps section
        """
        strStep = None
        
        if('html' == genOutFormat):
            strPics = ''
            for picLoc in self.info['inPic']:
                    strPics += makeHtmlEmbedImgFromFile( picLoc )
            strStep = '<li>' + self.info['inText'] + '<br>' + strPics + '</li>'
            
            
            if len(self.info['childStep']):
                strStep += '<ul>'
                for stepInfo in self.info['childStep']:
                    strStep += stepInfo.genStepBlock( genOutFormat, baseFilePath )
                strStep += '</ul>'
        
        elif( 'LaTex' == genOutFormat or 'LaTex_noFig' == genOutFormat):
            ### TODO - Need to handle images
            imgFigList = []
            for picLoc in self.info['inPic']:
                if ('LaTex' == genOutFormat):
                    imgFig = Figure(position='h!')
                    imgFig.add_image( 
                        str( Path( picLoc ).absolute() ), 
                        width=NoEscape(r"0.3\textwidth")
                        )
                    imgFigList.append( imgFig )
                elif('LaTex_noFig' == genOutFormat):
                    imgFigList.append( Command('begin',['center'] ) )
                    imgFigList.append(
                        Command(
                            'includegraphics',
                            [NoEscape(str( Path( picLoc ).absolute().as_posix() ))],
                            NoEscape(r'width=0.3\textwidth')
                            )
                        )
                    imgFigList.append( Command('end',['center'] ) )
                
            if( self.info['inText']): LaTexItemize.add_item(  self.info['inText'] )
            
            for iFig in imgFigList:
                LaTexItemize.append( iFig ) 
            if( len( self.info['childStep'])):
                itemize = Itemize()   
                for stepInfo in self.info['childStep']:
                    stepInfo.genStepBlock( genOutFormat, baseFilePath,LaTexDoc=LaTexDoc, LaTexItemize=itemize)
                LaTexItemize.append( itemize )
                strStep = LaTexItemize
         
        elif( 'LaTex_indented_InjectHere' == genOutFormat):
            if( self.info['inText']):
                strOut = ''
                if(callDepth > 0 ): strOut += '- '
                strOut += self.info['inText']
                LaTexDoc.append( strOut )
                LaTexDoc.append( NewLine() )
            
            for picLoc in self.info['inPic']:
                LaTexDoc.append( Command('begin',['center'] ) )
                LaTexDoc.append(
                    Command(
                            'includegraphics',
                            [NoEscape(str( Path( picLoc ).absolute().as_posix() ))],
                            NoEscape(r'width=0.3\textwidth')
                        )
                    )
                LaTexDoc.append( Command('end',['center'] ) )
            
            if( len( self.info['childStep'])):
                LaTexDoc.append( Command('vspace', [NoEscape(r'-10pt')] ) )
                LaTexDoc.append( Command('begin',['addmargin', str('%sem' % (callDepth+1))], packages=[ Package('scrextend')]))
                for stepInfo in self.info['childStep']:
                        stepInfo.genStepBlock( genOutFormat, baseFilePath,LaTexDoc=LaTexDoc, callDepth=callDepth+1)
                LaTexDoc.append( Command('end', ['addmargin']))
        else:
            raise Exception("Unknown format %s" % (genOutFormat) )
        
        return strStep
    
#=============================================================================
class MyRecipe:
    """
    An object that collects everything needed to make a recipe

    Description of class: Low-level design, physical design
    discussions, build dependencies, assumptions, implementation
    issues, notes, etc.
    """

    #-------------------------------------------------------------------------
    def __init__(self, recipeName, SectionNameStr, sharedIngredientList):
        """
        Create MyRecipe object.

        Class that holds info about  a recipe
        """
        self.info = {
            'name': recipeName,
            'pictures': {},
            'primaryPic': None,
            'RecipeSection': SectionNameStr,
            'RecipeLaTexFormat': None,
            
            'ingredients': { 
                },
            'ingredientsGrpOrder': [],
            
            'steps': [],
            
            'notes': [],
            
            'todo': [],
            }
        self.ingredients = sharedIngredientList
        
        if self.info['RecipeSection'] not in C_BOOK_SECTIONS:
            raise Exception(
                " ** Recipe Section: %s is not in the list of Ingredient in C_BOOK_SECTIONS. **\n" % 
                (self['RecipeSection']) 
                )
        
        self.setRecipeFormat( 'TWO_COLUMN_OPTIONAL_PICTURES' )

    #-------------------------------------------------------------------------
    def getName(self):
        """
        Return the name of this Recipe

        returns:
            string - name
        """
        return self.info['name']
    
    #-------------------------------------------------------------------------
    def getSection(self):
        """
        Get the name of the Section this Recipe lives under.

        returns:
            string - name
        """
        return self.info['RecipeSection']
    
    #-------------------------------------------------------------------------
    def getRecipeFormat(self):
        """
        Get the Format to use for this recipe.

        returns:
            string - name
        """
        return self.info['RecipeLaTexFormat']
    
    #-------------------------------------------------------------------------
    def setRecipeFormat(self, newFormat):
        """
        Get the Format to use for this recipe.

        returns:
            string - name
        """
        if newFormat not in C_RECIPE_FORMATING:
            raise Exception(
                " ** Recipe Formating: %s is not in the list of Ingredient in C_RECIPE_FORMATING. **\n" % 
                (self.info['RecipeLaTexFormat']) 
                )
        else:
            self.info['RecipeLaTexFormat'] = newFormat
            
    #-------------------------------------------------------------------------
    def addIngredient(self, ingredientName, ingredientAmount, ingredientUnits, ingredientGroupName = ''):
        """
        Add an Ingredient to a recipe. 
        
        TODO( TA, "How to keep track of usage? - Auto by steps?" )
        ## Maybe with Python Measurements:
          https://python-measurement.readthedocs.io/en/latest/topics/measures.html

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
        
        # See if we need to add this group
        if( ingredientGroupName not in self.info['ingredients'].keys() ):
            self.info['ingredients'][ingredientGroupName] = []
            self.info['ingredientsGrpOrder'].append( ingredientGroupName )
        
        # Look for ingredient in our known list.
        for alreadyAddedIngredient in self.info['ingredients'][ingredientGroupName]:
            knownListIng.append( alreadyAddedIngredient['ingredients'].getName() )
                    
        self.info['ingredients'][ingredientGroupName].append( 
            {
                'ingredients':thisIngredientInfo,
                'units': ingredientUnits,
                'amount': ingredientAmount
                } 
            )
        
        if ingredientName not in knownListIng:
            thisIngredientInfo.inRecipe( self )
                

    #-------------------------------------------------------------------------
    def addPicture(self, pictureName, picLocation, roundEdges=True, scaleAmt=1.0):
        """
        Add a picture to this recipe
        """
        if pictureName  not in self.info['pictures'].keys():
            self.info['pictures'][pictureName] = {
                'path_orig': os.path.join( self.info['dir_path'], picLocation)
                }
        
            newImgPath = buildPdfImg(
                Path( os.path.join( self.info['dir_path'], '..', '..', 'output', 'img')).resolve(), 
                self.info['pictures'][pictureName]['path_orig'],
                roundEdges, scaleAmt )
            
            self.info['pictures'][pictureName]['path'] = newImgPath
    #-------------------------------------------------------------------------
    def getPicturePath(self, picName):
        return self.info['pictures'][picName]['path']
    
    #-------------------------------------------------------------------------
    def setPrimaryPicture(self, pictureName):
        """
        Sets the primary pictures to use with this recipe
        """
        if pictureName in self.info['pictures'].keys():
            self.info['primaryPic'] = pictureName
    
    #-------------------------------------------------------------------------
    def getPicturePrimary(self):
        if self.info['primaryPic']:
            return self.info['pictures'][ self.info['primaryPic'] ]
        else:
            return None
                
    #-------------------------------------------------------------------------
    def setPathLoc(self, PathLoc):
        """
        Remember where the recipe file lived.

        args:
            Path of where the recipe file was found

        returns:
            Nothing
        """
        self.info['dir_path'] = PathLoc
    
    #-------------------------------------------------------------------------
    def getPathLoc(self):
        """
        Remember where the recipe file lived.

        args:
            None

        returns:
            Path from Recipe
        """
        return self.info['dir_path']
    
    #-------------------------------------------------------------------------
    def addToDoNote(self, strToDoNote):
        """
        Keep track of missing information
        """
        self.info['todo'].append( strToDoNote)
    
    #-------------------------------------------------------------------------
    def getToDoNotes(self):
        """
        Keep track of missing information
        """
        return self.info['todo']
        
    #-------------------------------------------------------------------------
    def genIngredientsBlock(self, genOutFormat='html'):
        """
        One line description of method.

        args:
            argument descriptions

        returns:
            description of return objects
        """
        dataBack = None
        
        if ( genOutFormat == 'html'):
            dataBack = ''
            for ingredientGrp in self.info['ingredientsGrpOrder']:
                dataBack += '<h2>' + ingredientGrp + '</h2>'
                
                dataBack += '<table>'
                for ingredient in self.info['ingredients'][ingredientGrp]:
                    strIngred = ingredient['ingredients'].genIngredientBlock( 
                        ingredient['amount'],
                        ingredient['units'],
                        genOutFormat )
                    dataBack +=  strIngred
                dataBack += '</table>'
        
        elif (genOutFormat == 'LaTex'):
            dataBack = []
            for ingredientGrp in self.info['ingredientsGrpOrder']:
                
                if( len(ingredientGrp) ):
                    dataBack.append( ('',  '' , '') )
                    dataBack.append( ('', bold(ingredientGrp), '') )
                    
                for ingredient in self.info['ingredients'][ingredientGrp]:
                    dataBack.append( 
                        (
                            ingredient['amount'],
                            ingredient['units'],
                            ingredient['ingredients'].getName(),
                            ingredient['ingredients'].getRecipeToMake()
                        ) 
                    )
        
        else:
            raise Exception("Unknown gen format: %s" % (genOutFormat) )
        
        return dataBack
    

    #-------------------------------------------------------------------------
    def addStep(self, nextStep, picNameList=[]):
        """
        Add a step to this recipe - note that steps can be nested, etc. 
        """
        
        for picName in picNameList:
            if picName in self.info['pictures'].keys():
                nextStep.attachPic( self.info['pictures'][picName]['path']  )
        
        self.info['steps'].append( nextStep )
    
    #-------------------------------------------------------------------------
    def addNote(self, strNote, picNameList=[]):
        """
        Add a note to this recipe - note that steps can be nested, etc. 
        """
        noteData = {
            'txt': strNote, 
            'picPathList': [] 
        }
        
        for picName in picNameList:
            if picName in self.info['pictures'].keys():
                noteData['picPathList'].append( self.info['pictures'][picName]['path'] )
        
        self.info['notes'].append( noteData )
        
    #-------------------------------------------------------------------------
    def genStepsBlock(self, genOutFormat='html', LaTexDoc=None):
        """
        """
        dataBack = None
        if( 'html' == genOutFormat):
            dataBack = '<ul>'
            for step in self.info['steps']:
                dataBack += step.genStepBlock( genOutFormat, self.getPathLoc() )
            dataBack += '</ul>'
        elif( 'LaTex' == genOutFormat or 'LaTex_noFig' == genOutFormat):
            if ( len( self.info['steps']) ):
                itemize = Itemize() 
                for step in self.info['steps']:
                    step.genStepBlock( genOutFormat, self.getPathLoc(), LaTexDoc=LaTexDoc, LaTexItemize=itemize)
                dataBack = itemize
        elif( 'LaTex_indented_InjectHere' == genOutFormat):
            if ( len( self.info['steps']) ):
                for step in self.info['steps']:
                    step.genStepBlock( genOutFormat, self.getPathLoc(), LaTexDoc=LaTexDoc, callDepth=0)
        else:
            raise Exception(" Unknown Generation format %s" % genOutFormat)
        
        return dataBack
    
    #-------------------------------------------------------------------------
    def AddDescription(self, descriptText):
        """
        Add Recipe Description
        """
        self.info['description'] = descriptText

    #-------------------------------------------------------------------------
    def GetDescription(self):
        if 'description' in self.info.keys():
            return self.info['description']
        else:
            return None
    
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
