##****************************************************************************
##   Generate a HTML file to test out he Single Recipe
##
##****************************************************************************
<%
# For 'gen' tools, we can use version as documentation.

%>\
##  Imports ******************************************************************
<%
# PY-4.10
# from {module} import {function}
from scripts.html_helpers import makeHtmlStyle
from scripts.html_helpers import makeHtmlEmbedImgFromFile
from scripts.html_helpers import makeHtmlLink

%>\
##  Constants ****************************************************************
<%
# PY-2.10
# DELIMITER = "," 
%>\
<hr color='GRAY' width="100%" size="2">
##============================================================================
<html>

<head>
<title>
Recipe List
</title>
<head>

<style>

/* Style the header */
header {
  background-color: #666;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
  width:100%
}

nav {
  float: left;
  width: 30%;
  background: #ccc;
  padding: 20px;
}

article {
  float: left;
  padding: 20px;
  width: 70%;
}

/* Clear floats after the columns */
bodySectionBlock {
  content: "";
  clear: both;
  display: flex;
  flex-direction: row;
}

${makeHtmlStyle()}

</style>

##============================================================================

<body>

<bodySectionBlock>

<header>
  <h2>
  Recipe List
  </h2>
</header>

</bodySectionBlock>

<bodySectionBlock>

<article>

<h2>Recipes</h2>
<ul>
% for recipName in cookbookData['Recipes']['sorted_names']:
    <li>
        <a href="${cookbookData['Recipes']['html'][recipName]['file_name']}"> ${recipName} </a>
    </li>
    %if len( cookbookData['Recipes']['inputObjects'][recipName].getToDoNotes() ):
    <ul>
        %for todoItem in cookbookData['Recipes']['inputObjects'][recipName].getToDoNotes():
            <li> TODO: ${todoItem} </li>
        % endfor
    </ul>
    %endif
    
% endfor
</ul>

% if len(cookbookData['errors']['dirMissingScripts']):
<h2> Empty Directories </h2>
<ul>
<%
  strListDir = []
  for errDir in cookbookData['errors']['dirMissingScripts']:
      strListDir.append( errDir )
  
  strListDir.sort()
%>\

% for errDir in strListDir:
<li>${errDir}</li>
% endfor

</ul>
% endif

</article>

</bodySectionBlock>



##============================================================================
## Footer
## Recommended: Identify template used to generate html output.
<footer>
<p>
Template: ${genToolTemplate}<BR>
<i>
    Generated: ${runDate} <br>
    using tool: ${genToolName} <br>
    version: ${genToolVersion} <br>
</i>
</p>
</footer>

</body>

</html>
## end of examples
            
##****************************************************************************
