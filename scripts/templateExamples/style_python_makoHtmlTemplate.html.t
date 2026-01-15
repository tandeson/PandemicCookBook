##****************************************************************************
##   One-line summary of file purpose.
##
##
##****************************************************************************
##  Use of the software source code and warranty disclaimers are
##  identified in the Software Agreement associated herewith.
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
from html_helpers import makeHtmlTable
from html_helpers import makeHtmlLink
from html_helpers import makeHtmlLinkTarget
from html_helpers import makeHtmlStyle
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
${TITLE}
</title>
${makeHtmlStyle()}
<head>
<body>
${makeHtmlLinkTarget("topOfDoc")}
<h1>
${HEADING_1}
</h1>
##============================================================================
## Beginning of example code  
<h2>Example of indented content List</h2>
${makeHtmlLinkTarget('List_MAP')}   
<ul>
%for example in ['List', 'Table']:
    <li>${example} </li>
    <ul>
<%doc> 
## <- added only to trigger color highlight in eclipse to flag doc tag block.
 Recommended inline python block format.
 Indent as if part of overall control flow.
</%doc>\
<%
    anEnding = ''
    if 'Table' == example:
        for ending in ['_', '1']:
            anEnding +=  ending
            
%>\
      <li>${makeHtmlLink(
                "link to example " + example + anEnding ,
                example + "_MAP"
            )}</li>
    </ul>
%endfor
</ul>
${makeHtmlLink("back to Top of page ", "topOfDoc")}
## End of example List

## Extra lines just so the to show that the links work.
<BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR>
<%doc>
## Example of a table
</%doc> 
${makeHtmlLinkTarget('Table_MAP')}
<%
functionList = [
    (
      "Example",
      "link",
    )
]
for example in ['List', 'Table']:
    functionList.append(
        (
            example,
            makeHtmlLink(
                "link to example " + example,
                example + "_MAP"
            )
        )
    )
              
%>\
<h2>Example as a table</h2>
${makeHtmlTable(functionList)}

${makeHtmlLink("back to Top of page ", "topOfDoc")}
## end of examples
            
##****************************************************************************
##****************************************************************************
