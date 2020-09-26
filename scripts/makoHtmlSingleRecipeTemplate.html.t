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

/* Style the header */
header {
  background-color: #666;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
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
section:after {
  content: "";
  display: table;
  clear: both;
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

<header>
  <h2>
% if inRecipeData.getPicturePrimary() != None:
    ${makeHtmlEmbedImgFromFile( inRecipeData.getPathLoc() + '\\' + inRecipeData.getPicturePrimary()['path']) }
% endif

  Recipe: ${inRecipeData.getName()}
  </h2>
</header>

<section>

<nav>

## Generate the Ingredients List  
<h1> Ingredients </h1>
${inRecipeData.genIngredientsBlock()}
</nav>
<article>
<h2> Future home of instructions </h2>
</article>

</section>

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
