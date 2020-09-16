##****************************************************************************
##   Generate a HTML file to test out he Single Recipe
##
##****************************************************************************
<%
# For 'gen' tools, we can use version as documentation.
version = '$Revision$'[1:-2]
templateName = '$URL$'[5:-2]
%>\
##  Imports ******************************************************************
<%
# PY-4.10
# from {module} import {function}
## HTML Helper functions
from scripts.html_helpers import makeHtmlTable
from scripts.html_helpers import makeHtmlLink
from scripts.html_helpers import makeHtmlLinkTarget
from scripts.html_helpers import makeHtmlStyle
%>\
##  Constants ****************************************************************
<%
# PY-2.10
# DELIMITER = "," 
GEN_TOOL_NAME = "rangegen"
TITLE = "Your Html title"
HEADING_1 = "Examples of List, table, and links"
%>\

##============================================================================
## Recommended: Identify template used to generate html output.
<font size='1' color=GRAY>
<p>
Template: ${templateName}<BR>
<i>
    Generated: ${runDate} on ${computerName} by ${userName}
    using ${GEN_TOOL_NAME}.py ${version}
</i>
</p>
</font>
<hr color='GRAY' width="100%" size="2">
##============================================================================
<html>
<head>
<title>
Test File
</title>
<head>
<body>

##============================================================================
## Beginning of example code  
<h2>Example of indented content List</h2>

## End of example List

## Extra lines just so the to show that the links work.
<BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR>

<h2>Example as a table</h2>


## end of examples
            
##****************************************************************************
