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
Ingredients List
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
  Ingredients List
  </h2>
</header>

</bodySectionBlock>

<bodySectionBlock>

<article>

<%
   listGrps = list( cookbookData['ingredients']['text_tree'].keys() )
   listGrps.sort()
%>\
%for grpName in listGrps:
<h2> ${grpName} </h2>

<%
 listIngredientNames = list( cookbookData['ingredients']['text_tree'][grpName].keys() )
 listIngredientNames.sort()
%>\
<ul>
%for ingredientName in listIngredientNames:
<li> ${ingredientName} </li>
%endfor // listIngredientNames
</ul>


%endfor // listGrps

### ---------------

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
