"""Input validation utilities for the Hello World package.

This module provides validation functions and decorators for ensuring
data integrity throughout the application.

Author: JacobPEvans
"""

from __future__ import annotations

import functools
import inspect
import re
from typing import TYPE_CHECKING, ParamSpec, TypeVar


if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

from hello_world.exceptions import ValidationError


# Type variables for generic decorators
P = ParamSpec("P")
R = TypeVar("R")

# Constants for validation
MAX_NAME_LENGTH = 100
MIN_NAME_LENGTH = 1
ALLOWED_NAME_PATTERN = re.compile(r"^[\w\s\-'.]+$", re.UNICODE)


def validate_name(name: str | None) -> str | None:
    """Validate a name for greeting.

    Args:
        name: The name to validate. Can be None or empty.

    Returns:
        The validated name, or None if the name was None/empty.

    Raises:
        ValidationError: If the name fails validation checks.

    Examples:
        >>> validate_name("Alice")
        'Alice'
        >>> validate_name("")
        >>> validate_name(None)
        >>> validate_name("  ")
    """
    if name is None:
        return None

    # Strip whitespace
    name = name.strip()

    if not name:
        return None

    # Check length constraints
    if len(name) > MAX_NAME_LENGTH:
        msg = f"must be at most {MAX_NAME_LENGTH} characters"
        raise ValidationError(field="name", value=name, reason=msg)

    # Check for valid characters (alphanumeric, spaces, hyphens, apostrophes, periods)
    if not ALLOWED_NAME_PATTERN.match(name):
        msg = "contains invalid characters (only letters, numbers, spaces, hyphens, apostrophes, and periods allowed)"
        raise ValidationError(field="name", value=name, reason=msg)

    return name


def validate_names_batch(names: Sequence[str | None]) -> list[str | None]:
    """Validate a batch of names.

    Args:
        names: A sequence of names to validate.

    Returns:
        A list of validated names.

    Raises:
        ValidationError: If the input is not a valid sequence.
        ValidationError: If any name fails validation (includes index in details).

    Examples:
        >>> validate_names_batch(["Alice", "Bob", None])
        ['Alice', 'Bob', None]
    """
    if not isinstance(names, list | tuple):
        msg = "must be a list or tuple"
        raise ValidationError(field="names", value=type(names).__name__, reason=msg)

    validated: list[str | None] = []
    errors: list[str] = []

    for i, name in enumerate(names):
        try:
            validated.append(validate_name(name))
        except ValidationError as e:
            errors.append(f"Index {i}: {e.reason}")

    if errors:
        msg = f"batch validation failed for {len(errors)} item(s)"
        raise ValidationError(
            field="names",
            value=f"batch of {len(names)} names",
            reason=msg,
            details="; ".join(errors),
        )

    return validated


def validate_positive_int(value: int, field_name: str = "value") -> int:
    """Validate that a value is a positive integer.

    Args:
        value: The value to validate.
        field_name: The name of the field being validated (for error messages).

    Returns:
        The validated positive integer.

    Raises:
        ValidationError: If the value is not a positive integer.

    Examples:
        >>> validate_positive_int(5)
        5
        >>> validate_positive_int(0)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValidationError: Validation failed for 'value': must be a positive integer
    """
    if not isinstance(value, int) or isinstance(value, bool):
        msg = "must be an integer"
        raise ValidationError(field=field_name, value=value, reason=msg)

    if value <= 0:
        msg = "must be a positive integer"
        raise ValidationError(field=field_name, value=value, reason=msg)

    return value


def validated(
    validator: Callable[[str | None], str | None],
    arg_name: str = "name",
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator factory for validating function arguments.

    Creates a decorator that validates a specific argument using
    the provided validator function before calling the wrapped function.

    This decorator handles both positional and keyword arguments by using
    inspect.signature to bind arguments to their parameter names.

    Args:
        validator: The validation function to apply.
        arg_name: The name of the argument to validate.

    Returns:
        A decorator that validates the specified argument.

    Example:
        >>> @validated(validate_name, "name")
        ... def say_hello(name: str | None = None) -> str:
        ...     return f"Hello, {name or 'World'}!"
        >>> say_hello("Alice")
        'Hello, Alice!'
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        sig = inspect.signature(func)

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Bind positional and keyword arguments to parameter names
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate the specified argument if present
            if arg_name in bound_args.arguments:
                validated_value = validator(bound_args.arguments[arg_name])
                bound_args.arguments[arg_name] = validated_value

            # Call the original function with potentially modified arguments
            return func(*bound_args.args, **bound_args.kwargs)

        return wrapper

    return decorator
