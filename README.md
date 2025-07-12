# Python Project Template

A minimal Python project template following modern best practices and industry standards.

**Author:** JacobPEvans
**Created:** July 12, 2025
**License:** GNU General Public License v3 or later (GPLv3+)
**Python Version:** 3.11+

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Git

### Installation

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd python-template
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux/macOS
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # Development installation (includes dev dependencies)
   pip install -e ".[dev]"

   # Or just production dependencies
   pip install -e .
   ```

4. **Set up pre-commit hooks**
   ```bash
   # Install pre-commit
   pip install pre-commit

   # Install the git hook scripts
   pre-commit install

   # (Optional) Run on all files to test setup
   pre-commit run --all-files
   ```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src/hello_world --cov-report=html

# Run tests in verbose mode
pytest -v

# Run specific test file
pytest tests/test_main.py -v
```

## 🛠️ Development Tools

### Pre-commit Hooks Setup

Pre-commit hooks automatically run code formatting, linting, and type checking before each commit to ensure code quality.
```bash
# Install pre-commit
pip install pre-commit

# Install the git hook scripts
pre-commit install

# Test the setup
pre-commit run --all-files
```

> **Note**: Once installed, pre-commit will automatically run on every `git commit`. If any checks fail, the commit will be blocked until issues are fixed. Code formatting tools like Black and isort will auto-fix many issues.

## Features

- ✅ Modern Python packaging with `pyproject.toml`
- ✅ Automated testing with pytest
- ✅ GitHub Actions CI/CD pipeline
- ✅ Code coverage reporting
- ✅ Type hints support
- ✅ Pre-configured `.gitignore`

## Project Structure

```
python-template/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions CI/CD
├── src/
│   └── hello_world/
│       ├── __init__.py        # Package initialization
│       └── main.py            # Main application code
├── tests/
│   ├── __init__.py            # Test package initialization
│   └── test_main.py           # Unit tests
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
├── pyproject.toml             # Modern Python packaging
└── requirements-dev.txt       # Development dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python-template
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Usage

Run the hello world application:

```bash
python -m hello_world.main
```

Or import and use in your code:

```python
from hello_world import greet

print(greet("Python"))  # Output: Hello, Python!
```

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Running Tests with Coverage

```bash
pytest tests/ -v --cov=src/hello_world --cov-report=html
```

### Installing in Development Mode

```bash
pip install -e .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
