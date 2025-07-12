# Python Project Template

A minimal Python project template following best practices.

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `.\venv\Scripts\Activate.ps1` (Windows)
4. Install development dependencies: `pip install -e ".[dev]"`

## Running Tests

```bash
pytest
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

## License

This project is licensed under the MIT License - see the LICENSE file for details.
