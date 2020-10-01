#!/usr/bin/python2.6
#*****************************************************************************
#    Copyright (c) 2009 Fluke Corporation. All rights reserved.
#*****************************************************************************
#
#   File            - $URL: https://engsvnhost.tc.fluke.com/repos/igdev.dmm/wallace/branches/hw_revx/trunk/tools/build/sharedmodules/html_helpers.py $
#   Version Number  - $Revision: 24247 $
#   Last Updated    - $Date: 2011-01-19 13:21:26 -0800 (Wed, 19 Jan 2011) $
#   Updated By      - $Author:rt $
#
#   Authored By     - rt gibson
#
"""
    Encapsulate the html helper utilities functionality.

"""
#
#*****************************************************************************
#   Use of the software source code and warranty disclaimers are
#   identified in the Software Agreement associated herewith.
#*****************************************************************************

#*  Imports ******************************************************************
from PIL import Image
import base64
import io

#*  Constants ****************************************************************


# Exit codes - "no error" must be 0
EXIT_OK, EXIT_ERR, EXIT_CTRL_C = range(3)

#*  Class and Function Definitions *******************************************

#=============================================================================
def makeHtmlStyle():
    '''
    Helper function, allows easy setting of common style..
    
    creates a <footer> tag
        
    '''
    styleString  = (
"          * {\n"
"    box-sizing: border-box;\n"
"  }\n"
"\n"  
"  th, td {\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"  }\n"
"  a { color: #0044B3; }\n"
"  a:visited { color: #597BB3; }\n"
"  a:hover { color: #0044B3; }\n"
"\n"
"  h1 {\n"
"      margin: 0;\n"
"      padding: 0;\n"
"      font-size: 2em;\n"
"      font-weight: bold; \n"
"      line-height: 1.2em;\n"
"  }\n"
"\n"
"  h2, h3, h4, h5, h6\n"
"  {\n"
"      margin: 1.5em 0 0 0;\n"
"      padding: 0;\n"
"      color: black;\n"
"      line-height: 1.2em;\n"
"  }\n"
"\n"
"  h2 {font-size: 2.0em;}\n"
"  h3 {font-size: 1.3em;}\n"
"  h4 {font-size: 1.1em;}\n"
"  h5, h6 {font-size: 1em;}\n"
"\n"
"  footer {\n"
"    background-color: #777;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    color: white;\n"
"  }"
    )    
    return styleString
# The following was removed - proposing that it be left out of the common
# style
#"  /* section numbering (Firefox-only) */\n"
#"  h1 { counter-reset: section;      /* Set section to 0 */ }\n"
#'  h2:before { content: counter(section) ". "; counter-increment: section; }\n'
#"\n"
#
#"  h2 {font-size: 1.6em;}\n"
# 

#=============================================================================
def makeHtmlEmbedImgFromFile(filePath):
    """
    Take in a file path - send back base64 encoded file data for webpage
    
    ensure the size is small-ish ( 200, 200 pixels )
    """
    size = 300,300    
    im = Image.open( filePath )
    im.thumbnail(size, Image.ANTIALIAS)
    
    buffer = io.BytesIO()
    im.save(buffer, format='PNG')
    buffer.seek(0)
    
    data_uri = base64.b64encode(buffer.read()).decode('ascii')
    
    html = '<img src="data:image/png;base64,{0}">'.format(data_uri)
    
    return html
    
#=============================================================================
def makeHtmlLink(text,targetName):
    '''
    Helper function, allows easier linking.
    '''
    
    return "<a href=\"#" + targetName + "\">" + text + "</a>"

#=============================================================================
def makeHtmlLinkTarget(targetName):
    '''
    Helper function, allows easier linking.
    
    see makeHtmlLink
    '''
    
    return "<a name=\"" + targetName +"\"></a>"
 
#=============================================================================
def makeHtmlTable(data):
    '''
      This function takes in a set of data, and uses it to make a table.
      
      The first entry is assumed to be the header.
      
      data = [
       (Title 1, Title 2, Title 3, .... , Title n),
       (Data 1, Data 2, Data 3, .... , Data n),
       ...
       n
      ]
    '''
      
    strTable = "<table>\r"
    for index,tableList in enumerate(data) : 
        strTable += " <tr>\r"
        if int(index) == 0 :
            strTable += " <thead>\r" 
        for item in tableList :
            strTable += "  <td>"
            strTable += str(item)
            strTable += "</td>\r"
        if int(index) == 0 :
            strTable += " </thead>\r" 
        strTable += " </tr>\r"
    strTable += "</table>\r"
    
    return strTable

 
