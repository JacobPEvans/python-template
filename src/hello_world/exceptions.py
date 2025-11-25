"""Custom exceptions for the Hello World package.

This module defines a hierarchy of exceptions for consistent error handling
throughout the application. All custom exceptions inherit from HelloWorldError.

Author: JacobPEvans
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


# Maximum number of failed names to display in error messages
_MAX_DISPLAY_NAMES = 5


class HelloWorldError(Exception):
    """Base exception for all Hello World package errors.

    All custom exceptions in this package inherit from this class,
    allowing users to catch all package-specific errors with a single
    except clause.

    Attributes:
        message: Human-readable description of the error.
        details: Optional additional details about the error.
    """

    def __init__(self, message: str, details: str | None = None) -> None:
        """Initialize the exception.

        Args:
            message: Human-readable description of the error.
            details: Optional additional details about the error.
        """
        self.message = message
        self.details = details
        super().__init__(self.message)

    def __str__(self) -> str:
        """Return string representation of the error."""
        if self.details:
            return f"{self.message} - Details: {self.details}"
        return self.message

    def __repr__(self) -> str:
        """Return detailed representation of the error."""
        return f"{self.__class__.__name__}(message={self.message!r}, details={self.details!r})"


class ValidationError(HelloWorldError):
    """Exception raised when input validation fails.

    This exception is raised when user-provided input does not meet
    the expected format, type, or constraints.

    Attributes:
        field: The name of the field that failed validation.
        value: The value that was rejected.
        reason: The reason for the validation failure.
    """

    def __init__(
        self,
        field: str,
        value: object,
        reason: str,
        *,
        details: str | None = None,
    ) -> None:
        """Initialize the validation error.

        Args:
            field: The name of the field that failed validation.
            value: The value that was rejected.
            reason: The reason for the validation failure.
            details: Optional additional details about the error.
        """
        self.field = field
        self.value = value
        self.reason = reason
        message = f"Validation failed for '{field}': {reason}"
        super().__init__(message, details)


class ConfigurationError(HelloWorldError):
    """Exception raised when configuration is invalid or missing.

    This exception is raised when the application cannot be configured
    properly due to missing or invalid configuration values.

    Attributes:
        config_key: The configuration key that caused the error.
        expected: Description of what was expected.
    """

    def __init__(
        self,
        config_key: str,
        expected: str,
        *,
        details: str | None = None,
    ) -> None:
        """Initialize the configuration error.

        Args:
            config_key: The configuration key that caused the error.
            expected: Description of what was expected.
            details: Optional additional details about the error.
        """
        self.config_key = config_key
        self.expected = expected
        message = f"Configuration error for '{config_key}': expected {expected}"
        super().__init__(message, details)


class GreetingError(HelloWorldError):
    """Exception raised when greeting generation fails.

    This exception is raised when the greeting function encounters
    an error that prevents it from generating a valid greeting.

    Attributes:
        name: The name that caused the error (if any).
        error_type: The type of error that occurred.
    """

    def __init__(
        self,
        error_type: str,
        name: str | None = None,
        *,
        details: str | None = None,
    ) -> None:
        """Initialize the greeting error.

        Args:
            error_type: The type of error that occurred.
            name: The name that caused the error (if any).
            details: Optional additional details about the error.
        """
        self.name = name
        self.error_type = error_type
        if name:
            message = f"Failed to generate greeting for '{name}': {error_type}"
        else:
            message = f"Failed to generate greeting: {error_type}"
        super().__init__(message, details)


class BatchGreetingError(HelloWorldError):
    """Exception raised when batch greeting operations fail.

    This exception is raised when processing multiple greetings
    and one or more fail.

    Attributes:
        failed_names: The names that failed to be greeted.
        total_count: Total number of names attempted.
        success_count: Number of successful greetings.
    """

    def __init__(
        self,
        failed_names: Sequence[str],
        total_count: int,
        success_count: int,
        *,
        details: str | None = None,
    ) -> None:
        """Initialize the batch greeting error.

        Args:
            failed_names: The names that failed to be greeted.
            total_count: Total number of names attempted.
            success_count: Number of successful greetings.
            details: Optional additional details about the error.
        """
        self.failed_names = list(failed_names)
        self.total_count = total_count
        self.success_count = success_count
        message = (
            f"Batch greeting failed: {len(failed_names)}/{total_count} failures. "
            f"Failed names: {', '.join(failed_names[:_MAX_DISPLAY_NAMES])}"
            f"{'...' if len(failed_names) > _MAX_DISPLAY_NAMES else ''}"
        )
        super().__init__(message, details)
