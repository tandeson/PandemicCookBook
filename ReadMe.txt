Home Recipe Project.
2020-10-04

= Overview =
This is a project where Thomas A. and Bilyana Y. are collecting recipes they commonly use and put them into one place. It's for fun, during the 2020 Pandemic. The goal is to get to a PDF that can be printed, so there is a cookbook in the kitchen that holds what we actually make at home.

= Project tools =
The project is primarly written in Python, using the 3.x language. It uses the following packages:

 * Python 3.x.x
  * Mako (formating data into output file format)
  * Pillow (for Image to base64)
  * GitPython ( for verion and repo dirty info)
  * pylatex ( for LaTex compliation )
 * Custom ( Recipe )
  * MyRecipe (Object that holds one recipe)
   * RecipeIngredients (An Ingredient)
   * RecipeStep ( a Step in a Recipe)

= Usage =
The Input directory "recipes_for_book_input" hold directories. The tool automatically searches for a *.py file, and then tries to call makeRecipe(). Which returns a formatted recipe object.

The intent is that notes about recipes are collected into a directory, and then once ready - the recipe itself is created to get a common format.

= Output Targets =
The goal is to generate a HTML output to allow for validation of the tool, and a PDF output that can eventually be printed.
