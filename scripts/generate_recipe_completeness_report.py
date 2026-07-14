#!/usr/bin/env python3
"""Generate an HTML completeness audit for all recipe source files."""

import argparse
import ast
import hashlib
import html
import json
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECIPE_ROOT = ROOT / "recipes_for_book_input"
DEFAULT_OUTPUT = ROOT / "planning" / "recipe_completeness_report.html"


def call_name(node):
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Name):
        return node.id
    return ""


def static_string(node):
    """Return a string for literals and os.path.join of literals."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Call) and call_name(node.func) == "join":
        parts = [static_string(arg) for arg in node.args]
        if all(part is not None for part in parts):
            return str(Path(*parts))
    return None


def argument_string(call, index):
    if len(call.args) <= index:
        return None
    return static_string(call.args[index])


def audit_recipe(source):
    tree = ast.parse(source.read_text(encoding="utf-8-sig"), filename=str(source))
    record = {
        "name": source.stem,
        "section": "Unknown",
        "source": source,
        "pictures": {},
        "primary": None,
        "description": False,
        "todos": [],
        "notes": 0,
        "steps": 0,
        "bg_status": "missing",
        "bg_file": None,
    }

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = call_name(node.func)
        if name == "MyRecipe":
            record["name"] = argument_string(node, 0) or record["name"]
            record["section"] = argument_string(node, 1) or record["section"]
        elif name == "addPicture":
            picture_name = argument_string(node, 0)
            picture_path = argument_string(node, 1)
            if picture_name:
                record["pictures"][picture_name] = picture_path
        elif name == "setPrimaryPicture":
            record["primary"] = argument_string(node, 0)
        elif name == "AddDescription":
            record["description"] = bool(argument_string(node, 0))
        elif name == "addToDoNote":
            record["todos"].append(argument_string(node, 0) or "Dynamic TODO expression")
        elif name == "addNote":
            record["notes"] += 1
        elif name == "addStep":
            record["steps"] += 1

    primary = record["primary"]
    if not primary:
        record["photo_status"] = "no primary selected"
    elif primary not in record["pictures"]:
        record["photo_status"] = "primary name is not registered"
    else:
        relative_path = record["pictures"][primary]
        if relative_path is None:
            record["photo_status"] = "primary path is dynamic; not statically checked"
        elif (source.parent / relative_path).is_file():
            record["photo_status"] = "current"
        else:
            record["photo_status"] = "primary file is missing"

    bg_files = sorted(source.parent.glob("bulgarian_*.json"))
    if bg_files:
        record["bg_file"] = bg_files[-1]
        try:
            data = json.loads(bg_files[-1].read_text(encoding="utf-8-sig"))
            stored_hash = data.get("recipe_file_hash")
            current_hash = hashlib.sha256(source.read_bytes()).hexdigest()
            if stored_hash is None:
                record["bg_status"] = "missing hash"
            elif stored_hash != current_hash:
                record["bg_status"] = "stale"
            else:
                record["bg_status"] = "current"
        except (OSError, json.JSONDecodeError):
            record["bg_status"] = "invalid JSON"

    return record


def relative_link(path):
    relative = path.relative_to(ROOT)
    return "../" + relative.as_posix()


def source_link(record):
    label = html.escape(record["source"].relative_to(ROOT).as_posix())
    return f'<a href="{html.escape(relative_link(record["source"]))}">{label}</a>'


def recipe_rows(records, extra_cell):
    rows = []
    for record in records:
        rows.append(
            "<tr>"
            f'<th scope="row">{html.escape(record["name"])}</th>'
            f"<td>{html.escape(record['section'])}</td>"
            f"<td>{extra_cell(record)}</td>"
            f"<td>{source_link(record)}</td>"
            "</tr>"
        )
    return "\n".join(rows)


def build_report(records):
    missing_primary = [r for r in records if r["photo_status"] != "current"]
    no_registered_pictures = [r for r in records if not r["pictures"]]
    bg_issues = [r for r in records if r["bg_status"] != "current"]
    missing_descriptions = [r for r in records if not r["description"]]
    todo_records = [r for r in records if r["todos"]]
    no_steps = [r for r in records if not r["steps"]]
    section_counts = Counter(r["section"] for r in records)
    total = len(records)
    generated_date = date.today().strftime("%B %d, %Y").replace(" 0", " ")
    bg_issue_word = "issue" if len(bg_issues) == 1 else "issues"

    section_summary = "".join(
        f"<li><strong>{html.escape(section)}</strong>: {count}</li>"
        for section, count in sorted(section_counts.items())
    )
    todo_rows = recipe_rows(
        todo_records,
        lambda r: "<ul>" + "".join(
            f"<li>{html.escape(item)}</li>" for item in r["todos"]
        ) + "</ul>",
    )
    photo_rows = recipe_rows(
        missing_primary,
        lambda r: (
            "Select one of the existing registered photos as primary"
            if r["pictures"]
            else "Make and photograph the dish; register and select the household photo"
        ) + f" <span class=\"muted\">({len(r['pictures'])} registered)</span>",
    )
    bg_rows = recipe_rows(
        bg_issues,
        lambda r: html.escape(r["bg_status"]),
    )
    description_rows = recipe_rows(
        missing_descriptions,
        lambda r: "Add household context only if it contributes useful history, serving advice, or technique notes",
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Recipe Completeness Report</title>
  <style>
    :root {{ --ink:#24211d; --muted:#70685e; --paper:#fffdf8; --wash:#eee7d9; --good:#426947; --warn:#9a4b30; --rule:#d7cbb8; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; color:var(--ink); background:var(--wash); font:15px/1.45 Arial,sans-serif; }}
    main {{ width:min(1180px,calc(100% - 28px)); margin:24px auto; padding:clamp(20px,4vw,48px); background:var(--paper); border:1px solid var(--rule); }}
    h1,h2,h3 {{ font-family:Georgia,serif; line-height:1.15; }}
    h1 {{ margin:.15em 0; font-size:clamp(2rem,5vw,3.4rem); }}
    h2 {{ margin-top:2.3rem; padding-bottom:.35rem; border-bottom:1px solid var(--rule); }}
    a {{ color:#81402e; text-underline-offset:3px; }}
    .eyebrow {{ color:var(--warn); text-transform:uppercase; letter-spacing:.12em; font-weight:700; font-size:.75rem; }}
    .lede,.muted {{ color:var(--muted); }}
    .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px; margin:24px 0; }}
    .card {{ padding:16px; background:white; border:1px solid var(--rule); }}
    .card strong {{ display:block; font:700 2rem/1 Georgia,serif; }}
    .good strong {{ color:var(--good); }} .warn strong {{ color:var(--warn); }}
    table {{ width:100%; border-collapse:collapse; background:white; }}
    th,td {{ padding:9px 10px; border-bottom:1px solid #e7dfd2; text-align:left; vertical-align:top; }}
    thead th {{ background:#f3ede2; }} tbody th {{ width:23%; }}
    td:last-child {{ overflow-wrap:anywhere; font-size:.84rem; }}
    ul {{ margin:.25rem 0; padding-left:1.25rem; }}
    details {{ margin:16px 0; padding:12px; border:1px solid var(--rule); background:#faf6ee; }}
    summary {{ cursor:pointer; font-weight:700; }}
    .callout {{ padding:16px 18px; border-left:5px solid var(--warn); background:#f8efe7; }}
    footer {{ margin-top:34px; color:var(--muted); font-size:.86rem; }}
    @media (max-width:760px) {{ table,thead,tbody,tr,th,td {{ display:block; }} thead {{ display:none; }} tr {{ padding:8px 0; border-bottom:2px solid var(--rule); }} th,td {{ border:0; padding:4px 7px; }} }}
  </style>
</head>
<body>
<main>
  <p class="eyebrow">Pandemic Cookbook audit</p>
  <h1>Recipe Completeness Report</h1>
  <p class="lede">Generated {generated_date} from every <code>recipe_*.py</code> file found recursively. This includes recipes stored in nested folders.</p>
  <p><a href="recipe_ideas.html">Open the recipes-to-try list</a></p>

  <div class="cards">
    <div class="card"><strong>{total}</strong>Total recipes</div>
    <div class="card good"><strong>{total - len(missing_primary)}</strong>Primary photos ready</div>
    <div class="card warn"><strong>{len(missing_primary)}</strong>Need photo attention</div>
    <div class="card good"><strong>{total - len(bg_issues)}</strong>Bulgarian files current</div>
    <div class="card warn"><strong>{len(todo_records)}</strong>Recipes with TODOs</div>
    <div class="card good"><strong>{total - len(no_steps)}</strong>Recipes with steps</div>
  </div>

  <div class="callout"><strong>Highest-value cleanup:</strong> photograph the {len(no_registered_pictures)} recipes with no registered picture, resolve the remaining primary-photo selections, and address the {len(bg_issues)} Bulgarian translation {bg_issue_word}.</div>

  <h2>Missing or unresolved primary pictures ({len(missing_primary)})</h2>
  <p>{len(no_registered_pictures)} recipes have no registered pictures. Hot Water Crust Savory Pie has registered photos but its primary-picture selection is commented out.</p>
  <table><thead><tr><th>Recipe</th><th>Section</th><th>Recommended action</th><th>Source</th></tr></thead><tbody>{photo_rows}</tbody></table>

  <h2>Bulgarian translation issues ({len(bg_issues)})</h2>
  <p>{total - len(bg_issues)} recipes have a parseable Bulgarian JSON file whose stored source hash matches its recipe file.</p>
  <table><thead><tr><th>Recipe</th><th>Section</th><th>Status</th><th>Source</th></tr></thead><tbody>{bg_rows}</tbody></table>
  <p class="muted">The existing <code>helper_check_bulgarian_hashes.py</code> checks only top-level recipe folders, so it currently reports success without seeing nested Cabbage Rolls.</p>

  <h2>Open recipe TODOs ({len(todo_records)})</h2>
  <table><thead><tr><th>Recipe</th><th>Section</th><th>TODO</th><th>Source</th></tr></thead><tbody>{todo_rows}</tbody></table>

  <h2>Descriptions and other signals</h2>
  <ul>
    <li>{total - len(missing_descriptions)} recipes have a household description; {len(missing_descriptions)} do not.</li>
    <li>{total - len(no_steps)} recipes contain at least one top-level step call; {len(no_steps)} do not.</li>
    <li>Descriptions are treated as optional editorial enrichment, not a publication blocker.</li>
  </ul>
  <details><summary>Show recipes without a description ({len(missing_descriptions)})</summary><table><thead><tr><th>Recipe</th><th>Section</th><th>Suggested action</th><th>Source</th></tr></thead><tbody>{description_rows}</tbody></table></details>

  <h2>Recipe count by section</h2>
  <ul>{section_summary}</ul>

  <footer>Regenerate with <code>python3 scripts/generate_recipe_completeness_report.py</code>. The audit parses recipe source without executing recipes or modifying generated cookbook output.</footer>
</main>
</body>
</html>
"""


def generate_report(recipe_root=RECIPE_ROOT, output=DEFAULT_OUTPUT):
    """Audit recipe sources and write the HTML report."""
    recipe_root = Path(recipe_root)
    if not recipe_root.is_absolute():
        recipe_root = ROOT / recipe_root

    output = Path(output)
    if not output.is_absolute():
        output = ROOT / output

    records = [audit_recipe(path) for path in sorted(recipe_root.rglob("recipe_*.py"))]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_report(records), encoding="utf-8")
    return output, len(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output, recipe_count = generate_report(output=args.output)
    print(f"Wrote {output} ({recipe_count} recipes audited)")


if __name__ == "__main__":
    main()
