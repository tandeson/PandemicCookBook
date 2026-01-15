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
<html>
<head>
<title>
Recipe: ${inRecipeData.getName()}
</title>
</head>
<style>
${makeHtmlStyle()}

:root {
  --ink: #1e1c19;
  --muted: #6b6762;
  --rule: #d6d0c4;
}

body {
  margin: 0;
  padding: 20px;
  color: var(--ink);
  background: #f2efe9;
  font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
}

.page {
  max-width: 980px;
  margin: 0 auto;
  padding: 14px 18px;
  background: #ffffff;
  border: 1px solid var(--rule);
}

.kicker {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.7em;
  color: var(--muted);
  margin-bottom: 2px;
}

.recipe-layout {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 18px;
  align-items: start;
}

.recipe-layout.no-photo {
  grid-template-columns: 1fr;
}

.recipe-photo img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.recipe-text {
  line-height: 1.35;
}

.recipe-text h1 {
  font-size: 2.1em;
  margin: 0 0 6px 0;
  line-height: 1.05;
}

.section {
  padding-top: 8px;
  margin-top: 8px;
}

.section:first-of-type {
  padding-top: 0;
  margin-top: 0;
}

.section + .section {
  border-top: 1px solid var(--rule);
}

.ingredients h2,
.steps h2,
.notes h3 {
  margin: 0 0 6px 0;
  font-size: 1.1em;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.ingredients table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95em;
}

.ingredients td {
  padding: 1px 4px;
  vertical-align: top;
}

.steps ul {
  margin: 0;
  padding-left: 1.2em;
  list-style: decimal;
}

.steps ul ul {
  list-style: lower-alpha;
  margin-top: 4px;
}

.steps li {
  margin-bottom: 0.45em;
}

.steps img {
  max-width: 360px;
  width: 100%;
  height: auto;
  border-radius: 4px;
  margin-top: 6px;
}

.notes-list {
  margin: 0;
  padding-left: 1.2em;
}

.note-pics {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 6px;
}

.note-pic img {
  width: 180px;
  height: auto;
  border-radius: 4px;
}

@media (max-width: 900px) {
  .page {
    padding: 16px;
  }
  .recipe-layout {
    grid-template-columns: 1fr;
  }
}

</style>

##============================================================================

<body>

<div class="page">

<% 
    hasPhoto = inRecipeData.getPicturePrimary() != None
    notesBlock = inRecipeData.genNotesBlock('html')
%>

<div class="recipe-layout${' no-photo' if not hasPhoto else ''}">
% if hasPhoto:
<aside class="recipe-photo">
    ${makeHtmlEmbedImgFromFile( inRecipeData.getPicturePrimary()['path']) }
</aside>
% endif

<section class="recipe-text">
  <div class="kicker">Recipe</div>
  <h1>${inRecipeData.getName()}</h1>

  <div class="section ingredients">
  ## Generate the Ingredients List  
  <h2>Ingredients</h2>
  ${inRecipeData.genIngredientsBlock()}
  </div>

  <div class="section steps">
  <h2>Steps</h2>
  ${inRecipeData.genStepsBlock('html')}
  </div>

  % if notesBlock:
  <div class="section notes">
    <h3>Notes</h3>
    ${notesBlock}
  </div>
  % endif
</section>
</div>

</div>

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
