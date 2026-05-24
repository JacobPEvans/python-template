# Template Instantiation Checklist

This repo is a **fork-and-edit** Python project template. After forking, walk
through each item below before opening your first real PR.

## 1. Project identity (`pyproject.toml`)

Replace every `REPLACE_ME` token:

- `name = "REPLACE_ME-project-name"` → kebab-case PyPI distribution name
- `authors = [{name = "REPLACE_ME Author", email = "replace-me@example.com"}]`
- `description = "REPLACE_ME — short project description"`
- `[tool.ruff.lint.isort] known-first-party = ["hello_world"]` →
  match your actual package directory under `src/`

## 2. Rename the package

```bash
git mv src/hello_world src/<your_package_name>
```

- Update any imports in `tests/` and elsewhere from `hello_world` to your
  package name.
- Update package-level metadata in `src/<your_package_name>/__init__.py`:
  `__author__`, `__email__`, and `__version__` are currently hardcoded
  with the template author's information and must be replaced.

## 3. Update README

- Replace `python-template` references with your project name
- Replace the example `hello_world` import/run snippets
- Update the badge URLs (replace `JacobPEvans/python-template` with
  `<your-org>/<your-repo>`)
- Fix the Codecov token in the coverage badge (or remove it until you wire
  up Codecov for the new repo)

## 4. CI workflows (`.github/workflows/`)

- `ci.yml` and `tests.yml` reference `JacobPEvans/python-template` in the
  Codecov `slug:` — replace with `<your-org>/<your-repo>`
- Confirm the Python `matrix` in `tests.yml` matches the versions you want
  to support; the single-version jobs in `ci.yml` use the latest released
  stable (`3.13`) — bump when you upgrade

## 5. Strip template scaffolding

Once everything is renamed and CI is green on your fork, delete this file:

```bash
git rm TEMPLATE.md
git commit -m "chore: remove template instantiation checklist"
```

## Why fork-and-edit instead of Cookiecutter?

The template doubles as a working repo for its own CI (linting, type checks,
security scans, coverage gating). Cookiecutter-style placeholders would
break that — the repo itself wouldn't be installable or testable. Fork
copies the working state; you edit it in place.
