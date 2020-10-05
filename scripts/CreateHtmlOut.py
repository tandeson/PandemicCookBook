#!/usr/bin/env python
#*****************************************************************************
#
"""
    Build up a cook book by pulling together all the pieces
"""
#
#*****************************************************************************
#   Use of the software source code and warranty disclaimers are
#   identified in the Software Agreement associated herewith.
#*****************************************************************************

#*  Imports ******************************************************************

import os
import datetime

import sys

from pathlib import Path

## For rendering options
from mako.template import Template

#*  Constants ****************************************************************

#=============================================================================
def genHtmlOut(args, outAbsPath, cookbookData, gitRepo):
    
    gitSha = gitRepo.head.object.hexsha
        
    # -- HTML        
    outHtmlAbsPath = Path( os.path.join( outAbsPath, 'html') )
    outHtmlAbsPath.mkdir(parents=True, exist_ok=True)
    
    inTemplateFilePath = Path( os.path.join(
                        '.', 
                        'templates', 
                        'html'
                        ))

    #---------------------------------------------------------------
    # Do a Recipe Page for each Recipes
    for iRecipe in cookbookData['Recipes']['inputObjects'].keys() :
        if (args.verbose):
            print( "Building HTML file for Recipe:%s" % ( iRecipe ) )
        
        strPathToTemplate = str( Path( os.path.join(
                        inTemplateFilePath, 
                        'makoHtmlSingleRecipeTemplate.html.t'
                    )).absolute() )
        
        mytemplate = Template(
            filename= strPathToTemplate
        )
        
        strHtmlFileName = 'Recipe_' + iRecipe + '.html'     
        strFullHtmlPath =  os.path.join( outHtmlAbsPath , strHtmlFileName)
        cookbookData['Recipes']['html'][iRecipe] ={'file_name': strHtmlFileName}
        
        if (os.path.exists(strFullHtmlPath) ): os.remove( strFullHtmlPath )
        fileHtmlOut = open(strFullHtmlPath, 'w+' )
        fileHtmlOut.write(
            mytemplate.render(
                runDate= datetime.datetime.now().strftime( cookbookData['Recipes']['html_date_format']),
                genToolName= __file__,
                genToolTemplate= strPathToTemplate,
                genToolVersion = '0.00 - Git Hash:' + gitSha[:10] + ' Repo Clean:' + str(not gitRepo.is_dirty()),
                inRecipeData = cookbookData['Recipes']['inputObjects'][iRecipe],
                )
        )
        fileHtmlOut.close()
    
    #---------------------------------------------------------------
    # Do a Recipe Summary Page
    doRecipeList = True
    if ( doRecipeList ):
        strPathToTemplate = str( Path( os.path.join(
                        inTemplateFilePath,
                        'makoHtmlRecipeListTemplate.html.t'
                    )).absolute() )
        
        mytemplate = Template(
            filename= strPathToTemplate
        )
        
        strFullHtmlPath =  os.path.join( outHtmlAbsPath , 'Recipe_list' + '.html' )
        if (os.path.exists(strFullHtmlPath) ): os.remove( strFullHtmlPath )
        fileHtmlOut = open(strFullHtmlPath, 'w+' )
        fileHtmlOut.write(
            mytemplate.render(
                runDate= datetime.datetime.now().strftime(cookbookData['Recipes']['html_date_format']),
                genToolName= __file__,
                genToolTemplate= strPathToTemplate,
                genToolVersion = '0.00 - Git Hash:' + gitSha[:10] + ' Repo Clean:' + str(not gitRepo.is_dirty()),
                cookbookData = cookbookData,
                )
        )
        fileHtmlOut.close()
    
    #---------------------------------------------------------------
    # Do a Ingredients Page
    doIngredientsPage = True
    if (doIngredientsPage ):
        strPathToTemplate = str( Path( os.path.join(
                        inTemplateFilePath,
                        'makoHtmlIngredientsListTemplate.html.t'
                    )).absolute() )
        
        mytemplate = Template(
            filename= strPathToTemplate
        )
        
        strFullHtmlPath =  os.path.join( outHtmlAbsPath , 'Ingredients_list' + '.html' )
        if (os.path.exists(strFullHtmlPath) ): os.remove( strFullHtmlPath )
        fileHtmlOut = open(strFullHtmlPath, 'w+' )
        fileHtmlOut.write(
            mytemplate.render(
                runDate= datetime.datetime.now().strftime(cookbookData['Recipes']['html_date_format']),
                genToolName= __file__,
                genToolTemplate= strPathToTemplate,
                genToolVersion = '0.00 - Git Hash:' + gitSha[:10] + ' Repo Clean:' + str(not gitRepo.is_dirty()),
                cookbookData = cookbookData,
                )
        )
        fileHtmlOut.close()



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
