"""Main module for Hello World application.

This module provides a simple greeting functionality that demonstrates
Python best practices for packaging and documentation.

Author: JacobPEvans
Created: July 12, 2025
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

from hello_world.exceptions import BatchGreetingError, GreetingError
from hello_world.validators import validate_name

logger = logging.getLogger(__name__)


def greet(name: str | None = None, *, strict: bool = False) -> str:
    """Generate a greeting message.

    Args:
        name: Name to greet. If None or empty, defaults to "World".
        strict: If True, raises GreetingError for invalid names.
                If False, falls back to "World" for invalid names.

    Returns:
        A formatted greeting message.

    Raises:
        GreetingError: If strict=True and name validation fails.

    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("Python")
        'Hello, Python!'
        >>> greet("")
        'Hello, World!'
    """
    try:
        validated_name = validate_name(name)
    except Exception as e:
        if strict:
            raise GreetingError(
                error_type="validation_failed",
                name=name,
                details=str(e),
            ) from e
        logger.warning("Name validation failed, defaulting to 'World': %s", e)
        validated_name = None

    if not validated_name:
        logger.info("No name provided, defaulting to 'World'")
        validated_name = "World"
    else:
        logger.info("Greeting name: %s", validated_name)

    return f"Hello, {validated_name}!"


def greet_many(
    names: Iterable[str | None],
    *,
    strict: bool = False,
) -> list[str]:
    """Generate greetings for multiple names.

    Args:
        names: An iterable of names to greet.
        strict: If True, raises BatchGreetingError if any greetings fail.
                If False, uses "World" for failed names.

    Returns:
        A list of greeting messages.

    Raises:
        BatchGreetingError: If strict=True and any name fails validation.

    Examples:
        >>> greet_many(["Alice", "Bob"])
        ['Hello, Alice!', 'Hello, Bob!']
        >>> greet_many([None, "Charlie"])
        ['Hello, World!', 'Hello, Charlie!']
    """
    names_list = list(names)
    results: list[str] = []
    failed_names: list[str] = []

    for name in names_list:
        try:
            results.append(greet(name, strict=strict))
        except GreetingError:
            # Only raised when strict=True - track failures for batch error
            failed_names.append(str(name))

    if failed_names:
        raise BatchGreetingError(
            failed_names=failed_names,
            total_count=len(names_list),
            success_count=len(results),
        )

    return results


def create_greeting_template(
    greeting_word: str = "Hello",
    punctuation: str = "!",
) -> str:
    """Create a greeting template string.

    Args:
        greeting_word: The word to use for greeting (default: "Hello").
        punctuation: The punctuation to append (default: "!").

    Returns:
        A template string with a placeholder for the name.

    Examples:
        >>> create_greeting_template()
        'Hello, {name}!'
        >>> create_greeting_template("Hi", "?")
        'Hi, {name}?'
    """
    return f"{greeting_word}, {{name}}{punctuation}"


def format_greeting(template: str, name: str | None = None) -> str:
    """Format a greeting using a template.

    Args:
        template: A template string with a {name} placeholder.
        name: The name to insert. Defaults to "World" if None or empty.

    Returns:
        The formatted greeting string.

    Examples:
        >>> format_greeting("Hello, {name}!", "Python")
        'Hello, Python!'
        >>> format_greeting("Hi, {name}?", None)
        'Hi, World?'
    """
    validated_name = validate_name(name) or "World"
    return template.format(name=validated_name)


def main() -> None:
    """Execute the main entry point for the application.

    Prints a default greeting message to stdout.
    """
    print(greet())  # noqa: T201


if __name__ == "__main__":
    main()
