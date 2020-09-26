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
import time
import datetime

import sys
import importlib

from pathlib import Path

## Custom objects
from IngredientList import C_INGREDIENTS

## For rendering options
from mako.template import Template

#*  Constants ****************************************************************
C_DATETIME_STR_FMT_RULES = "%I:%M%p on %B %d, %Y" 

# Exit codes - "no error" must be 0
EXIT_OK, EXIT_ERR, EXIT_CTRL_C = range(3)

#=============================================================================
def main(argv=None):
    """
    Parse arguments, report start & stop time, and run the test.
    """
    
    # Handle command line arguments
    if argv is None:
        argv = sys.argv

    args = parseCommandLine( argv[1:] )

    try:
        print( "Start date & time is " + time.strftime("%c") )

        # Do the work
        mainControl(args)

    except KeyboardInterrupt:
        # Assume Control-C is intentional, and just exit w/o alerts
        return EXIT_CTRL_C

    print( "End date & time is " + time.strftime("%c") )
    return EXIT_OK


#=============================================================================
def parseCommandLine(args = sys.argv[1:]):
    """
    Parse command-line options. Returns arguments.

    """

    ## Documentation: https://docs.python.org/2/howto/argparse.html
    import argparse

    ## Parse Input Options.
    parser = argparse.ArgumentParser(description='Cookbook builder')
    
    ## -- Common Options
    parser.add_argument(
        '-i','--input_directory',
        action='store', default="recipes_for_book_input",
        help = "root directory where recipes are stored.")

    parser.add_argument(
        '-v','--verbose',
        action='store_true',
        help = "Verbose progress messages. Progress messages are "
                "not displayed by default except for system error messages.")
    
    ## Parse the options
    args = parser.parse_args()

    return (args)

#=============================================================================
def mainControl(args):
    """
    Main routine for the Cookbook Builder.

    Find all the recipe files, build a cookbook!
    """
    
    RecipeList = []
            
    # Sample of handling errors.
    if not os.path.isdir( args.input_directory ):
        sys.stderr.write("Directory '%s' does not exist.\n" % args.input_directory)
        sys.exit(1)
    else:
        inDirRootPath = Path( os.path.join(".", args.input_directory) )
        
        # Find all the python files
        pythonFiles = list( inDirRootPath.rglob("*.[pP][yY]"))
        
        # Find all the dir inside the input directory - ensure each has at least one recipe.
        inDirList = next( os.walk(inDirRootPath) )[1]
        
        ## Check for missing dir info
        dirMissingScripts = []
        for dirName in inDirList:
            if(args.verbose):
                print( " Checking: %s" % dirName )
            didFind = False
            for fileDir in pythonFiles:
                if(dirName in str(fileDir)): 
                    didFind = True
                    break
            if( False == didFind):
                dirMissingScripts.append(dirName)
                
        if (len(dirMissingScripts ) ):
            print("\n** Warning - the following directories do not have a recipe python script. **")
            for i in dirMissingScripts:
                print(i)
            print('\n')
                
        ## for dir with info - run them
        for pythonModuleFile in pythonFiles:
            strModulePath = str(pythonModuleFile).replace('\\','.')[:-3]
            
            result = importlib.import_module(strModulePath)

            newRecipe = result.makeRecipe( C_INGREDIENTS )
            newRecipe.setPathLoc( os.path.dirname( pythonModuleFile.absolute() ) )
            RecipeList.append( newRecipe )
            
    ## Any data clean up - post processing
    
    ## Generate outputs
    
    # -- HTML
    genHtmlSample = True
    if ( genHtmlSample ):
        
        for iRecipe in RecipeList:
            print( "Building HTML file for Recipe:%s" % ( iRecipe.getName() ) )
            
            strPathToTemplate = str( Path( os.path.join(
                            '.', 
                            'scripts', 
                            'makoHtmlSingleRecipeTemplate.html.t'
                        )).absolute() )
            
            mytemplate = Template(
                filename= strPathToTemplate
            )
            
            ## Write to a file ( erasing the old one, if there is one )
            strFullHtmlPath =  os.path.join( iRecipe.getPathLoc(), iRecipe.getName() + '.html' )
            if (os.path.exists(strFullHtmlPath) ): os.remove( strFullHtmlPath )
            fileHtmlOut = open(strFullHtmlPath, 'w+' )
            fileHtmlOut.write(
                mytemplate.render(
                    runDate= datetime.datetime.now().strftime(C_DATETIME_STR_FMT_RULES),
                    genToolName= __file__,
                    genToolTemplate= strPathToTemplate,
                    genToolVersion = '0.00 - dev',
                    inRecipeData = iRecipe,
                    )
            )
            fileHtmlOut.close()

    
    # -- LaTex


    return True

#*  Main Code Path ***********************************************************

if __name__ == "__main__":
    # Exit code is main() return value
    # (see http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
    sys.exit(main())


#*****************************************************************************
#*****************************************************************************
