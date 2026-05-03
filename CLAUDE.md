# python-template

A Python project template demonstrating modern best practices: ruff linting,
mypy type checking, bandit security scanning, and pytest with coverage.

## Key Commands

```bash
make install      # install the package in editable mode
make install-dev  # install the package in editable mode with dev dependencies
make lint         # ruff check
make format       # ruff format (auto-fix)
make test         # pytest
make security     # bandit + pip-audit
make all          # format + lint + type-check + security + test-cov
```

## Structure

```text
src/hello_world/    # main package
  main.py           # greet() and greet_many() entry points
  validators.py     # validate_name() input guard
  exceptions.py     # GreetingError, ValidationError, BatchGreetingError
tests/              # pytest suite (mirrors src/)
```

## Development Conventions

- **Linting**: `ruff check --fix` (replaces flake8/isort/pylint)
- **Formatting**: `ruff format`
- **Types**: `mypy src/` (strict mode via pyproject.toml)
- **Security**: `bandit -r src/` + `pip-audit`
- **Tests**: `pytest --cov=src/hello_world` — 100% coverage expected
- **Pre-commit**: hooks run ruff, mypy, bandit, trailing-whitespace on every commit

## CI Workflows

- `ci.yml` — Code Quality (ruff + mypy + bandit + pip-audit + docstring check)
- `tests.yml` — Tests across Python 3.11/3.12/3.13 with Codecov upload
