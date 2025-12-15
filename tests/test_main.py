"""Tests for main module.

Author: JacobPEvans
Created: July 12, 2025
"""

from unittest.mock import MagicMock

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from hello_world.exceptions import BatchGreetingError, GreetingError
from hello_world.main import (
    create_greeting_template,
    format_greeting,
    greet,
    greet_many,
    main,
)


class TestGreetFunction:
    """Test cases for the greet function."""

    @pytest.mark.unit
    def test_greet_default(self) -> None:
        """Test greet function with default parameter (None)."""
        assert greet() == "Hello, World!"

    @pytest.mark.unit
    def test_greet_custom(self) -> None:
        """Test greet function with custom name."""
        assert greet("Python") == "Hello, Python!"

    @pytest.mark.unit
    def test_greet_empty_string(self) -> None:
        """Test greet function with empty string should default to World."""
        assert greet("") == "Hello, World!"

    @pytest.mark.unit
    def test_greet_none_explicit(self) -> None:
        """Test greet function with explicit None parameter."""
        assert greet(None) == "Hello, World!"

    @pytest.mark.unit
    def test_greet_whitespace_only(self) -> None:
        """Test greet function with whitespace-only string."""
        assert greet("   ") == "Hello, World!"

    @pytest.mark.unit
    def test_greet_strips_whitespace(self) -> None:
        """Test that greet function strips leading/trailing whitespace."""
        assert greet("  Alice  ") == "Hello, Alice!"

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Alice", "Hello, Alice!"),
            ("Bob", "Hello, Bob!"),
            ("123", "Hello, 123!"),
            ("Test User", "Hello, Test User!"),
            ("Dr. Smith", "Hello, Dr. Smith!"),
            ("Mary-Jane", "Hello, Mary-Jane!"),
            ("O'Connor", "Hello, O'Connor!"),
        ],
    )
    def test_greet_parametrized(self, name: str, expected: str) -> None:
        """Test greet function with various inputs using parametrization."""
        assert greet(name) == expected

    @pytest.mark.unit
    def test_greet_with_valid_names_fixture(self, valid_names: list[str]) -> None:
        """Test greet function with valid names from fixture."""
        for name in valid_names:
            result = greet(name)
            assert result.startswith("Hello, ")
            assert result.endswith("!")

    @pytest.mark.unit
    def test_greet_strict_mode_valid(self) -> None:
        """Test greet function in strict mode with valid input."""
        assert greet("Alice", strict=True) == "Hello, Alice!"

    @pytest.mark.unit
    def test_greet_strict_mode_invalid_raises(self) -> None:
        """Test greet function in strict mode raises for invalid input."""
        # A very long name should fail validation in strict mode
        long_name = "A" * 101
        with pytest.raises(GreetingError) as exc_info:
            greet(long_name, strict=True)
        assert "validation_failed" in str(exc_info.value)

    @pytest.mark.unit
    def test_greet_non_strict_mode_fallback(self) -> None:
        """Test greet function in non-strict mode falls back gracefully."""
        long_name = "A" * 101
        # Should not raise, should fallback to World
        result = greet(long_name, strict=False)
        assert result == "Hello, World!"

    @pytest.mark.unit
    def test_greet_logs_info(self, mock_logger: MagicMock) -> None:
        """Test that greet function logs appropriately."""
        greet("TestUser")
        mock_logger.info.assert_called()
        # Check that TestUser was logged
        call_args_str = str(mock_logger.info.call_args_list)
        assert "TestUser" in call_args_str

    @pytest.mark.unit
    def test_greet_logs_default(self, mock_logger: MagicMock) -> None:
        """Test that greet function logs when using default."""
        greet(None)
        mock_logger.info.assert_called()
        # Check that defaulting to World was logged
        call_args_str = str(mock_logger.info.call_args_list)
        assert "World" in call_args_str

    @given(st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=("L", "N", "Zs"))))
    @settings(max_examples=50)
    def test_greet_hypothesis_valid_text(self, name: str) -> None:
        """Property-based test for greet with valid text."""
        if name.strip():
            result = greet(name)
            assert result.startswith("Hello, ")
            assert result.endswith("!")


class TestGreetManyFunction:
    """Test cases for the greet_many function."""

    @pytest.mark.unit
    def test_greet_many_simple(self) -> None:
        """Test greet_many with simple list."""
        result = greet_many(["Alice", "Bob"])
        assert result == ["Hello, Alice!", "Hello, Bob!"]

    @pytest.mark.unit
    def test_greet_many_with_none(self) -> None:
        """Test greet_many with None values."""
        result = greet_many([None, "Charlie"])
        assert result == ["Hello, World!", "Hello, Charlie!"]

    @pytest.mark.unit
    def test_greet_many_empty_list(self) -> None:
        """Test greet_many with empty list."""
        result = greet_many([])
        assert result == []

    @pytest.mark.unit
    def test_greet_many_all_none(self) -> None:
        """Test greet_many with all None values."""
        result = greet_many([None, None, None])
        assert result == ["Hello, World!", "Hello, World!", "Hello, World!"]

    @pytest.mark.unit
    def test_greet_many_generator(self) -> None:
        """Test greet_many with generator input."""
        names = (name for name in ["Alice", "Bob"])
        result = greet_many(names)
        assert result == ["Hello, Alice!", "Hello, Bob!"]

    @pytest.mark.unit
    def test_greet_many_strict_raises_batch_error(self) -> None:
        """Test greet_many strict mode raises BatchGreetingError."""
        names = ["Alice", "A" * 101, "Bob"]  # One invalid name
        with pytest.raises(BatchGreetingError) as exc_info:
            greet_many(names, strict=True)
        assert exc_info.value.total_count == 3
        assert len(exc_info.value.failed_names) == 1

    @pytest.mark.unit
    def test_greet_many_non_strict_with_invalid(self) -> None:
        """Test greet_many non-strict mode handles invalid names gracefully."""
        names = ["Alice", "A" * 101, "Bob"]  # One invalid name in the middle
        result = greet_many(names, strict=False)
        # Should have 3 results - invalid name falls back to World
        assert len(result) == 3
        assert result[0] == "Hello, Alice!"
        assert result[1] == "Hello, World!"  # Fallback for invalid
        assert result[2] == "Hello, Bob!"


class TestCreateGreetingTemplate:
    """Test cases for create_greeting_template function."""

    @pytest.mark.unit
    def test_default_template(self) -> None:
        """Test default template creation."""
        template = create_greeting_template()
        assert template == "Hello, {name}!"

    @pytest.mark.unit
    def test_custom_greeting_word(self) -> None:
        """Test custom greeting word."""
        template = create_greeting_template("Hi")
        assert template == "Hi, {name}!"

    @pytest.mark.unit
    def test_custom_punctuation(self) -> None:
        """Test custom punctuation."""
        template = create_greeting_template(punctuation="?")
        assert template == "Hello, {name}?"

    @pytest.mark.unit
    def test_fully_custom(self) -> None:
        """Test fully customized template."""
        template = create_greeting_template("Greetings", "...")
        assert template == "Greetings, {name}..."


class TestFormatGreeting:
    """Test cases for format_greeting function."""

    @pytest.mark.unit
    def test_format_with_name(self) -> None:
        """Test formatting with a name."""
        template = "Hello, {name}!"
        result = format_greeting(template, "Alice")
        assert result == "Hello, Alice!"

    @pytest.mark.unit
    def test_format_with_none(self) -> None:
        """Test formatting with None defaults to World."""
        template = "Hi, {name}?"
        result = format_greeting(template, None)
        assert result == "Hi, World?"

    @pytest.mark.unit
    def test_format_with_empty_string(self) -> None:
        """Test formatting with empty string defaults to World."""
        template = "Hey, {name}."
        result = format_greeting(template, "")
        assert result == "Hey, World."

    @pytest.mark.unit
    def test_format_with_invalid_name_falls_back_to_world(self) -> None:
        """Test formatting with invalid name falls back to World."""
        template = "Hello, {name}!"
        # Name with invalid characters should fall back to World
        result = format_greeting(template, "Test<script>")
        assert result == "Hello, World!"


class TestMainFunction:
    """Test cases for the main function."""

    @pytest.mark.unit
    def test_main_prints_greeting(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test that main function prints the default greeting."""
        main()
        captured = capsys.readouterr()
        assert captured.out == "Hello, World!\n"

    @pytest.mark.unit
    def test_main_no_exceptions(self) -> None:
        """Test that main function doesn't raise exceptions."""
        # Should not raise
        main()
