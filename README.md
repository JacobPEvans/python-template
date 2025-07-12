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

### Code Formatting & Linting
```bash
# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Lint with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/
```

### Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

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
└── requirements.txt           # Dependencies
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
   pip install -r requirements.txt
   ```

## Usage

Run the hello world application:

```bash
python -m src.hello_world.main
```

Or import and use in your code:

```python
from src.hello_world import hello_world

print(hello_world("Python"))  # Output: Hello, Python!
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
