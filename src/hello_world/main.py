"""
Main module for Hello World application.

This module provides a simple greeting functionality that demonstrates
Python best practices for packaging and documentation.

Author: JacobPEvans
Created: July 12, 2025
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


def greet(name: Optional[str] = None) -> str:
    """
    Generate a greeting message.

    Args:
        name: Name to greet. If None or empty, defaults to "World"

    Returns:
        str: A formatted greeting message

    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("Python")
        'Hello, Python!'
        >>> greet("")
        'Hello, World!'
    """
    if not name:
        logger.info("No name provided, defaulting to 'World'")
        name = "World"
    else:
        logger.info(f"Name provided: {name}")
    return f"Hello, {name}!"


def main() -> None:
    """
    Main entry point for the application.

    Prints a default greeting message to stdout.
    """
    print(greet())


if __name__ == "__main__":
    main()
