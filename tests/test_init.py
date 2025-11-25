"""Tests for package initialization.

Author: JacobPEvans
Created: July 13, 2025
"""

import importlib
from pathlib import Path
from unittest.mock import patch

import pytest

import hello_world
from hello_world import (
    BatchGreetingError,
    ConfigurationError,
    GreetingError,
    HelloWorldError,
    ValidationError,
    create_greeting_template,
    format_greeting,
    greet,
    greet_many,
    validate_name,
    validate_names_batch,
    validate_positive_int,
)


class TestPackageInit:
    """Test cases for package initialization."""

    @pytest.mark.unit
    def test_logging_config_missing_file(self) -> None:
        """Test package initialization when logging.conf doesn't exist."""
        with patch.object(Path, "exists", return_value=False):
            importlib.reload(hello_world)

        # Verify the module still works despite missing config
        assert hello_world.greet() == "Hello, World!"

    @pytest.mark.unit
    def test_logging_config_present(self) -> None:
        """Test package initialization when logging.conf exists."""
        # Reload to ensure logging is configured
        importlib.reload(hello_world)
        assert hello_world.greet() == "Hello, World!"


class TestPackageMetadata:
    """Test cases for package metadata."""

    @pytest.mark.unit
    def test_version(self) -> None:
        """Test package version is defined."""
        assert hello_world.__version__ == "0.1.0"

    @pytest.mark.unit
    def test_author(self) -> None:
        """Test package author is defined."""
        assert hello_world.__author__ == "JacobPEvans"

    @pytest.mark.unit
    def test_email(self) -> None:
        """Test package email is defined."""
        assert "@" in hello_world.__email__


class TestPackageExports:
    """Test cases for package exports."""

    @pytest.mark.unit
    def test_greet_exported(self) -> None:
        """Test greet function is exported."""
        assert greet is not None
        assert callable(greet)
        assert greet() == "Hello, World!"

    @pytest.mark.unit
    def test_greet_many_exported(self) -> None:
        """Test greet_many function is exported."""
        assert greet_many is not None
        assert callable(greet_many)
        assert greet_many(["A"]) == ["Hello, A!"]

    @pytest.mark.unit
    def test_create_greeting_template_exported(self) -> None:
        """Test create_greeting_template is exported."""
        assert create_greeting_template is not None
        assert callable(create_greeting_template)

    @pytest.mark.unit
    def test_format_greeting_exported(self) -> None:
        """Test format_greeting is exported."""
        assert format_greeting is not None
        assert callable(format_greeting)

    @pytest.mark.unit
    def test_validators_exported(self) -> None:
        """Test validator functions are exported."""
        assert validate_name is not None
        assert validate_names_batch is not None
        assert validate_positive_int is not None

    @pytest.mark.unit
    def test_exceptions_exported(self) -> None:
        """Test exception classes are exported."""
        assert HelloWorldError is not None
        assert ValidationError is not None
        assert ConfigurationError is not None
        assert GreetingError is not None
        assert BatchGreetingError is not None

    @pytest.mark.unit
    def test_all_exports(self) -> None:
        """Test __all__ contains expected exports."""
        expected_exports = {
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
            "BatchGreetingError",
            "ConfigurationError",
            "GreetingError",
            "HelloWorldError",
            "ValidationError",
        }
        assert set(hello_world.__all__) == expected_exports


class TestPackageUsage:
    """Test cases for typical package usage patterns."""

    @pytest.mark.unit
    def test_import_star(self) -> None:
        """Test that importing * gives expected symbols."""
        # This tests that __all__ is properly defined
        module_dict: dict[str, object] = {}
        exec("from hello_world import *", module_dict)  # noqa: S102

        assert "greet" in module_dict
        assert "ValidationError" in module_dict

    @pytest.mark.unit
    def test_typical_usage(self) -> None:
        """Test a typical usage pattern of the package."""
        # Import and use
        from hello_world import greet, validate_name

        name = validate_name("  User  ")
        result = greet(name)
        assert result == "Hello, User!"

    @pytest.mark.unit
    def test_exception_handling_pattern(self) -> None:
        """Test typical exception handling pattern."""
        from hello_world import HelloWorldError, greet

        try:
            # This won't raise, but shows the pattern
            greet("Test")
        except HelloWorldError:
            pytest.fail("Should not raise")

    @pytest.mark.unit
    def test_batch_operations(self) -> None:
        """Test batch operations work as expected."""
        from hello_world import greet_many

        names = ["Alice", "Bob", None, ""]
        results = greet_many(names)
        assert len(results) == 4
        assert results[0] == "Hello, Alice!"
        assert results[2] == "Hello, World!"
