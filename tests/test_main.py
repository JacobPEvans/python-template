"""Tests for main module."""

from hello_world.main import greet


def test_greet_default():
    """Test greet function with default parameter."""
    assert greet() == "Hello, World!"


def test_greet_custom():
    """Test greet function with custom name."""
    assert greet("Python") == "Hello, Python!"
