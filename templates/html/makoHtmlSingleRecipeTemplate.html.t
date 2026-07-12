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

%>\
##  Constants ****************************************************************
<%
# PY-2.10
# DELIMITER = ","
%>\
##============================================================================
<html lang="${labels['html_lang']}">
<head>
<meta charset="utf-8">
<title>
${labels['recipe_kicker']}: ${inRecipeData.getDisplayName()}
</title>
</head>
<style>

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
}

% endif

nav {
  float: left;
  width: 30%;
  background: #ccc;
  padding: 20px;
  font-family: ${labels['html_font_family']};
}

article {
  float: left;
  padding: 20px;
  width: 70%;
  font-family: ${labels['html_font_family']};
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
% if inRecipeData.getPicturePrimary() != None:
<headerPic>
    ${makeHtmlEmbedImgFromFile( inRecipeData.getPicturePrimary()['path']) }
</headerPic>
% endif

<header>
  <h2>
  ${labels['recipe_kicker']}: ${inRecipeData.getDisplayName()}
  </h2>
</header>
</bodySectionBlock>

<bodySectionBlock>

<nav>

## Generate the Ingredients List
<h1>${labels['ingredients']}</h1>
${inRecipeData.genIngredientsBlock()}
</nav>

<article>
<h2>${labels['directions']}</h2>
${inRecipeData.genStepsBlock('html')}
<%
notesBlock = inRecipeData.genNotesBlock('html')
%>
% if notesBlock:
<h3>${labels['notes']}</h3>
${notesBlock}
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
