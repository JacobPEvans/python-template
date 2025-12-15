# Contributing to Python Template

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Please:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-template.git
   cd python-template
   ```
3. Add the upstream repository as a remote:
   ```bash
   git remote add upstream https://github.com/JacobPEvans/python-template.git
   ```

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Git
- Make (optional, but recommended)

### Installation

**Important:** Always use a virtual environment to isolate project dependencies from your system Python.

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install development dependencies (inside the activated virtual environment):
   ```bash
   # Using make (recommended)
   make install-dev

   # Or manually
   pip install -e ".[dev]"
   pre-commit install
   ```

3. Verify your setup:
   ```bash
   make check  # Or: pytest && ruff check src/ tests/
   ```

**Note:** All `make` and `pytest` commands should be run within the activated virtual environment.

## Code Style

This project enforces strict code quality standards using multiple tools:

### Formatting

- **Ruff**: Fast all-in-one linter and formatter (handles formatting and import sorting)

### Linting

- **Ruff**: Comprehensive linting (pyflakes, pycodestyle, pylint rules, isort, and many more)
- **mypy**: Static type checking (strict mode)
- **bandit**: Security linting

### Documentation

- All public functions, classes, and modules must have docstrings
- Use Google-style docstrings
- Include type hints for all function parameters and return values

### Example

```python
def greet(name: str | None = None) -> str:
    """Generate a greeting message.

    Args:
        name: The name to greet. Defaults to "World" if None.

    Returns:
        A formatted greeting string.

    Raises:
        ValidationError: If the name contains invalid characters.

    Examples:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet()
        'Hello, World!'
    """
    ...
```

### Running Code Quality Checks

```bash
# Format code
make format

# Run all linters
make lint

# Run type checker
make type-check

# Run security checks
make security

# Run all checks at once
make all
```

## Testing

### Test Requirements

- **100% code coverage is required** - All pull requests must maintain 100% coverage
- Tests must pass on Python 3.11 or higher
- Use pytest for all tests

### Writing Tests

1. Place tests in the `tests/` directory
2. Name test files with `test_` prefix
3. Use descriptive test names that explain what is being tested
4. Use fixtures from `conftest.py` when appropriate
5. Mark tests appropriately (`@pytest.mark.unit`, `@pytest.mark.integration`)

### Running Tests

```bash
# Run all tests
make test

# Run with coverage (required before PR)
make test-cov

# Run tests in parallel (faster)
make test-fast

# Run only unit tests
make test-unit

# Run specific test file
pytest tests/test_main.py -v
```

### Property-Based Testing

We use Hypothesis for property-based testing. When appropriate, add hypothesis tests:

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1, max_size=50))
def test_function_with_hypothesis(value: str) -> None:
    """Property-based test for function."""
    result = some_function(value)
    assert some_property(result)
```

## Submitting Changes

### Branch Naming

Use descriptive branch names:

- `feature/add-new-validation`
- `fix/handle-empty-input`
- `docs/update-readme`
- `refactor/simplify-greet-function`

### Commit Messages

Follow conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(validators): add email validation function

fix(greet): handle None input correctly

docs(readme): update installation instructions

test(main): add hypothesis tests for greet function
```

### Before Submitting

1. Ensure all tests pass with 100% coverage:
   ```bash
   make test-cov
   ```

2. Run all quality checks:
   ```bash
   make all
   ```

3. Update documentation if needed

4. Add yourself to contributors (if applicable)

## Pull Request Process

1. **Create a descriptive PR title** following the commit message format

2. **Fill out the PR template** with:
   - Description of changes
   - Related issue numbers
   - Testing performed
   - Checklist completion

3. **Ensure CI passes** - All GitHub Actions checks must pass

4. **Request review** from maintainers

5. **Address feedback** - Make requested changes and push updates

6. **Merge** - Once approved and CI passes, a maintainer will merge your PR

### PR Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex logic
- [ ] Documentation updated (if applicable)
- [ ] Tests added/updated with 100% coverage
- [ ] All CI checks passing
- [ ] No merge conflicts with main branch

## Questions?

If you have questions, feel free to:

1. Open an issue for discussion
2. Check existing issues and PRs for similar topics
3. Review the project documentation

Thank you for contributing! 🎉
