# Repository Guidelines

## Project Structure & Module Organization
- `CreateCookbook.py` is the main entry point for building the cookbook.
- `recipes_for_book_input/` holds recipe folders; each recipe has a `*.py` that exposes `makeRecipe()`.
- `scripts/` contains helpers (HTML/LaTeX generation and recipe models like `myRecipe.py`).
- `templates/` stores output templates used by the renderer.
- `output/` is the default build target for generated HTML/PDF artifacts.
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

## Testing Guidelines
- No automated test suite is present in the repository.
- Validate changes by running `CreateCookbook.py` and reviewing generated HTML/PDF in `output/`.
- For new recipes, verify formatting, ingredient ordering, and rendering in the output.

## Commit & Pull Request Guidelines
- Recent commits use short, descriptive sentences (e.g., “Added Nutella Cookies”).
- Keep commits focused on a single recipe or change set.
- PRs should include a brief description, list of new/updated recipes, and a screenshot or PDF snippet from `output/` when applicable.

## Security & Configuration Tips
- Avoid committing generated files in `output/` unless explicitly required.
- Treat recipe input as code: prefer minimal imports and keep `makeRecipe()` deterministic.
