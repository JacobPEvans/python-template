# python-template

A Python project template demonstrating modern best practices: ruff linting, mypy type checking, bandit security scanning, and pytest with coverage.

## Key Commands

```bash
make install      # install runtime dependencies
make install-dev  # install all dev dependencies
make lint         # ruff check + mypy
make format       # ruff format (auto-fix)
make test         # pytest with coverage
make security     # bandit + safety
make all          # lint + type-check + test + security
```

## Structure

```
src/hello_world/    # main package
  main.py           # greet() and batch_greet() entry points
  validators.py     # validate_name() input guard
  exceptions.py     # GreetingError, ValidationError, BatchGreetingError
tests/              # pytest suite (mirrors src/)
```

## Development Conventions

- **Linting**: `ruff check --fix` (replaces flake8/isort/pylint)
- **Formatting**: `ruff format`
- **Types**: `mypy src/` (strict mode via pyproject.toml)
- **Security**: `bandit -r src/` + `safety check`
- **Tests**: `pytest --cov=src/hello_world` — 100% coverage expected
- **Pre-commit**: hooks run ruff, mypy, bandit, trailing-whitespace on every commit

## CI Workflows

- `ci.yml` — Code Quality (ruff + mypy)
- `tests.yml` — Tests across Python 3.11/3.12/3.13 with Codecov upload
