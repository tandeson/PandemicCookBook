# Repository Guidelines

## Project Structure & Module Organization
- `CreateCookbook.py` is the main entry point for building the cookbook.
- `recipes_for_book_input/` holds recipe folders; each recipe has a `*.py` that exposes `makeRecipe()`.
- `scripts/` contains helpers (HTML/LaTeX generation and recipe models like `myRecipe.py`).
- `templates/` stores output templates used by the renderer.
- `output/` is the default build target for generated HTML/PDF artifacts.
- `planning/` stores planning notes and batch tracking for recipe updates.
- `CoverWork/` and `generate_coverPhotoFromPrimaryPic.py` support cover image creation.

## Build, Test, and Development Commands
- Build cookbook HTML/PDF:
  - `python3 CreateCookbook.py -i recipes_for_book_input -o output -n Pandemic_Cookbook`
  - Uses Mako + pylatex to generate output; PDF requires a working LaTeX toolchain.
- Cover image helper:
  - `python3 generate_coverPhotoFromPrimaryPic.py`
- Dependency note: Python 3.x, `Mako`, `Pillow`, `GitPython`, `pylatex` (per `ReadMe.txt`).

## Coding Style & Naming Conventions
- Python code uses 4-space indentation.
- Classes typically use `CamelCase` (e.g., `MyRecipe`), functions use `snake_case`.
- Constants are uppercase with underscores (e.g., `C_DATETIME_STR_FMT_RULES`).
- Keep recipe file names descriptive and aligned with the recipe name.

## Tools
- `pylatex` is used to generate PDF output; `xelatex` is required for Bulgarian output.
- `Mako`, `Pillow`, and `GitPython` are required per `ReadMe.txt`.
- Use `scripts/helper_update_ingredient_name.py` for ingredient name updates so references stay in sync.
- When doing command line runs - pick the tool with the higest chance of good outcomes (bash, python, etc)

## Testing Guidelines
- If you see a place for automated test, add them. 
- For full systems Validation, run `CreateCookbook.py` and reviewing generated HTML/PDF in `output/`.
- For new recipes, verify formatting, ingredient ordering, and rendering in the output.

## Planning
- We are reviewing recipes in small batches to fix spelling, grammar, and clarity in text strings.
- We are adding and validating Bulgarian translations during these batches.
- Batch tracking lives in `planning/recipe_batch_notes.md`.
- Bulgarian translation JSON files (`bulgarian_YYYY-MM-DD.json`) can be created/edited without requesting approval; you will review before commit.

## Commit & Pull Request Guidelines
- The commit message should cover the what and why of the change. It can be short, but it is more importand to cover what and why then to be brief
- PRs should include a brief description, list of new/updated recipes, and a screenshot or PDF snippet from `output/` when applicable.

## Security & Configuration Tips
- Avoid committing generated files in `output/` unless explicitly required.
- Treat recipe input as code: prefer minimal imports and keep `makeRecipe()` deterministic.
