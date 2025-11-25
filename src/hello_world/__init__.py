"""Hello World package.

A simple Python package template demonstrating best practices.

Author: JacobPEvans
Created: July 12, 2025
"""

from __future__ import annotations

import logging.config
from pathlib import Path

from hello_world.exceptions import (
    BatchGreetingError,
    ConfigurationError,
    GreetingError,
    HelloWorldError,
    ValidationError,
)
from hello_world.main import (
    create_greeting_template,
    format_greeting,
    greet,
    greet_many,
)
from hello_world.validators import (
    validate_name,
    validate_names_batch,
    validate_positive_int,
)


# Construct the full path to the logging configuration file
_config_path = Path(__file__).parent / "logging.conf"

# Configure the logging using the file
if _config_path.exists():
    logging.config.fileConfig(_config_path)

__version__ = "0.1.0"
__author__ = "JacobPEvans"
__email__ = "20714140+JacobPEvans@users.noreply.github.com"

__all__ = [
    "BatchGreetingError",
    "ConfigurationError",
    "GreetingError",
    "HelloWorldError",
    "ValidationError",
    "__author__",
    "__email__",
    "__version__",
    "create_greeting_template",
    "format_greeting",
    "greet",
    "greet_many",
    "validate_name",
    "validate_names_batch",
    "validate_positive_int",
]
