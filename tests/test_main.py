"""
Tests for main module.

Author: JacobPEvans
Created: July 12, 2025
"""

import pytest

from hello_world.main import greet


class TestGreetFunction:
    """Test cases for the greet function."""

    def test_greet_default(self) -> None:
        """Test greet function with default parameter (None)."""
        assert greet() == "Hello, World!"

    def test_greet_custom(self) -> None:
        """Test greet function with custom name."""
        assert greet("Python") == "Hello, Python!"

    def test_greet_empty_string(self) -> None:
        """Test greet function with empty string should default to World."""
        assert greet("") == "Hello, World!"

    def test_greet_none_explicit(self) -> None:
        """Test greet function with explicit None parameter."""
        assert greet(None) == "Hello, World!"

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Alice", "Hello, Alice!"),
            ("Bob", "Hello, Bob!"),
            ("123", "Hello, 123!"),
            ("Test User", "Hello, Test User!"),
        ],
    )
    def test_greet_parametrized(self, name: str, expected: str) -> None:
        """Test greet function with various inputs using parametrization."""
        assert greet(name) == expected
