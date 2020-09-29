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
from scripts.html_helpers import makeHtmlStyle
from scripts.html_helpers import makeHtmlEmbedImgFromFile

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
${makeHtmlStyle}
<title>
Recipe: ${inRecipeData.getName()}
</title>
<head>
<style>

* {
  box-sizing: border-box;
  font-family: "Courier New", Courier, monospace;
}

% if inRecipeData.getPicturePrimary() == None:

/* Style the header */
header {
  background-color: #666;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
}

% else:

/* Style the header */
headerPic {
  background-color: #666;
  color: white;
  width: 300px;
  float: left;
}

/* Style the header */
header {
  background-color: #666;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
  width: calc(100% - 300px);
  float: left;
  height: 300px;
}

% endif

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

footer {
  background-color: #777;
  padding: 10px;
  text-align: center;
  color: white;
}

</style>

##============================================================================

<body>

% if inRecipeData.getPicturePrimary() != None:
<headerPic>
    ${makeHtmlEmbedImgFromFile( inRecipeData.getPathLoc() + '\\' + inRecipeData.getPicturePrimary()['path']) }
</headerPic>
% endif

<header>
  <h2>
  Recipe: ${inRecipeData.getName()}
  </h2>
</header>

<bodySectionBlock>

<nav>

## Generate the Ingredients List  
<h1> Ingredients </h1>
${inRecipeData.genIngredientsBlock()}
</nav>

<article>
<h2>Directions</h2>
${inRecipeData.genStepsBlock('html')}
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

## end of examples
            
##****************************************************************************
