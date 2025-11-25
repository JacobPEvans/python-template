"""Tests for validators module.

Author: JacobPEvans
"""

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from hello_world.exceptions import ValidationError
from hello_world.validators import (
    ALLOWED_NAME_PATTERN,
    MAX_NAME_LENGTH,
    MIN_NAME_LENGTH,
    validate_name,
    validate_names_batch,
    validate_positive_int,
    validated,
)


class TestValidateName:
    """Test cases for validate_name function."""

    @pytest.mark.unit
    def test_valid_simple_name(self) -> None:
        """Test validation of a simple valid name."""
        assert validate_name("Alice") == "Alice"

    @pytest.mark.unit
    def test_valid_name_with_space(self) -> None:
        """Test validation of name with spaces."""
        assert validate_name("John Doe") == "John Doe"

    @pytest.mark.unit
    def test_valid_name_with_hyphen(self) -> None:
        """Test validation of name with hyphen."""
        assert validate_name("Mary-Jane") == "Mary-Jane"

    @pytest.mark.unit
    def test_valid_name_with_apostrophe(self) -> None:
        """Test validation of name with apostrophe."""
        assert validate_name("O'Connor") == "O'Connor"

    @pytest.mark.unit
    def test_valid_name_with_period(self) -> None:
        """Test validation of name with period."""
        assert validate_name("Dr. Smith") == "Dr. Smith"

    @pytest.mark.unit
    def test_none_returns_none(self) -> None:
        """Test that None input returns None."""
        assert validate_name(None) is None

    @pytest.mark.unit
    def test_empty_string_returns_none(self) -> None:
        """Test that empty string returns None."""
        assert validate_name("") is None

    @pytest.mark.unit
    def test_whitespace_only_returns_none(self) -> None:
        """Test that whitespace-only string returns None."""
        assert validate_name("   ") is None

    @pytest.mark.unit
    def test_strips_whitespace(self) -> None:
        """Test that whitespace is stripped."""
        assert validate_name("  Alice  ") == "Alice"

    @pytest.mark.unit
    def test_max_length_valid(self) -> None:
        """Test that name at max length is valid."""
        name = "A" * MAX_NAME_LENGTH
        assert validate_name(name) == name

    @pytest.mark.unit
    def test_exceeds_max_length_raises(self) -> None:
        """Test that name exceeding max length raises ValidationError."""
        name = "A" * (MAX_NAME_LENGTH + 1)
        with pytest.raises(ValidationError) as exc_info:
            validate_name(name)
        assert exc_info.value.field == "name"
        assert "100 characters" in exc_info.value.reason

    @pytest.mark.unit
    def test_invalid_characters_raises(self) -> None:
        """Test that invalid characters raise ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            validate_name("Name<script>")
        assert "invalid characters" in exc_info.value.reason

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "invalid_name",
        [
            "Name;DROP",
            "Hello\x00World",
            "Test@email",
            "Name#hashtag",
            "Test$dollar",
        ],
    )
    def test_various_invalid_characters(self, invalid_name: str) -> None:
        """Test various invalid characters raise ValidationError."""
        with pytest.raises(ValidationError):
            validate_name(invalid_name)

    @pytest.mark.unit
    def test_unicode_names_valid(self) -> None:
        """Test that unicode names are valid."""
        assert validate_name("日本語") == "日本語"
        assert validate_name("Привет") == "Привет"
        assert validate_name("مرحبا") == "مرحبا"

    @pytest.mark.unit
    def test_numbers_valid(self) -> None:
        """Test that names with numbers are valid."""
        assert validate_name("User123") == "User123"

    @given(st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=("L", "N"))))
    @settings(max_examples=50)
    def test_hypothesis_alphanumeric(self, name: str) -> None:
        """Property-based test for alphanumeric names."""
        # Should not raise for alphanumeric text
        result = validate_name(name)
        if name.strip():
            assert result == name.strip()


class TestValidateNamesBatch:
    """Test cases for validate_names_batch function."""

    @pytest.mark.unit
    def test_valid_batch(self) -> None:
        """Test validation of valid name batch."""
        names = ["Alice", "Bob", "Charlie"]
        result = validate_names_batch(names)
        assert result == ["Alice", "Bob", "Charlie"]

    @pytest.mark.unit
    def test_batch_with_none(self) -> None:
        """Test batch with None values."""
        names = ["Alice", None, "Charlie"]
        result = validate_names_batch(names)
        assert result == ["Alice", None, "Charlie"]

    @pytest.mark.unit
    def test_batch_with_empty_strings(self) -> None:
        """Test batch with empty strings."""
        names = ["Alice", "", "Charlie"]
        result = validate_names_batch(names)
        assert result == ["Alice", None, "Charlie"]

    @pytest.mark.unit
    def test_empty_batch(self) -> None:
        """Test empty batch."""
        result = validate_names_batch([])
        assert result == []

    @pytest.mark.unit
    def test_batch_tuple_input(self) -> None:
        """Test batch with tuple input."""
        names = ("Alice", "Bob")
        result = validate_names_batch(names)
        assert result == ["Alice", "Bob"]

    @pytest.mark.unit
    def test_batch_invalid_type_raises(self) -> None:
        """Test that invalid type raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            validate_names_batch("not a list")  # type: ignore[arg-type]
        assert exc_info.value.field == "names"
        assert "list or tuple" in exc_info.value.reason

    @pytest.mark.unit
    def test_batch_with_invalid_name_raises(self) -> None:
        """Test batch with invalid name raises ValidationError."""
        names = ["Alice", "A" * 101, "Charlie"]
        with pytest.raises(ValidationError) as exc_info:
            validate_names_batch(names)
        assert exc_info.value.field == "names"
        assert "Index 1" in str(exc_info.value.details)


class TestValidatePositiveInt:
    """Test cases for validate_positive_int function."""

    @pytest.mark.unit
    def test_valid_positive_int(self) -> None:
        """Test validation of valid positive integer."""
        assert validate_positive_int(5) == 5
        assert validate_positive_int(1) == 1
        assert validate_positive_int(1000000) == 1000000

    @pytest.mark.unit
    def test_zero_raises(self) -> None:
        """Test that zero raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            validate_positive_int(0)
        assert "positive integer" in exc_info.value.reason

    @pytest.mark.unit
    def test_negative_raises(self) -> None:
        """Test that negative integers raise ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            validate_positive_int(-1)
        assert "positive integer" in exc_info.value.reason

    @pytest.mark.unit
    def test_float_raises(self) -> None:
        """Test that floats raise ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            validate_positive_int(1.5)  # type: ignore[arg-type]
        assert "integer" in exc_info.value.reason

    @pytest.mark.unit
    def test_bool_raises(self) -> None:
        """Test that booleans raise ValidationError."""
        with pytest.raises(ValidationError):
            validate_positive_int(True)  # type: ignore[arg-type]

    @pytest.mark.unit
    def test_custom_field_name(self) -> None:
        """Test custom field name in error."""
        with pytest.raises(ValidationError) as exc_info:
            validate_positive_int(-1, "count")
        assert exc_info.value.field == "count"

    @given(st.integers(min_value=1, max_value=10000))
    @settings(max_examples=50)
    def test_hypothesis_positive_integers(self, value: int) -> None:
        """Property-based test for positive integers."""
        assert validate_positive_int(value) == value


class TestValidatedDecorator:
    """Test cases for validated decorator."""

    @pytest.mark.unit
    def test_decorator_validates_kwarg(self) -> None:
        """Test that decorator validates keyword argument."""

        @validated(validate_name, "name")
        def greet(name: str | None = None) -> str:
            return f"Hello, {name or 'World'}!"

        assert greet(name="Alice") == "Hello, Alice!"

    @pytest.mark.unit
    def test_decorator_strips_whitespace(self) -> None:
        """Test that decorator strips whitespace via validator."""

        @validated(validate_name, "name")
        def greet(name: str | None = None) -> str:
            return f"Hello, {name or 'World'}!"

        assert greet(name="  Alice  ") == "Hello, Alice!"

    @pytest.mark.unit
    def test_decorator_none_handling(self) -> None:
        """Test that decorator handles None properly."""

        @validated(validate_name, "name")
        def greet(name: str | None = None) -> str:
            return f"Hello, {name or 'World'}!"

        assert greet(name=None) == "Hello, World!"

    @pytest.mark.unit
    def test_decorator_preserves_function_metadata(self) -> None:
        """Test that decorator preserves function metadata."""

        @validated(validate_name, "name")
        def my_function(name: str | None = None) -> str:
            """My docstring."""
            return str(name)

        assert my_function.__name__ == "my_function"
        assert my_function.__doc__ == "My docstring."

    @pytest.mark.unit
    def test_decorator_with_positional_args(self) -> None:
        """Test that decorator works with positional arguments (arg not in kwargs)."""

        @validated(validate_name, "name")
        def greet(name: str | None = None) -> str:
            return f"Hello, {name or 'World'}!"

        # Call with positional argument - won't be validated since not in kwargs
        result = greet("Alice")
        assert result == "Hello, Alice!"


class TestConstants:
    """Test cases for module constants."""

    @pytest.mark.unit
    def test_max_name_length(self) -> None:
        """Test MAX_NAME_LENGTH constant."""
        assert MAX_NAME_LENGTH == 100

    @pytest.mark.unit
    def test_min_name_length(self) -> None:
        """Test MIN_NAME_LENGTH constant."""
        assert MIN_NAME_LENGTH == 1

    @pytest.mark.unit
    def test_allowed_pattern_matches_valid(self) -> None:
        """Test ALLOWED_NAME_PATTERN matches valid names."""
        assert ALLOWED_NAME_PATTERN.match("Alice")
        assert ALLOWED_NAME_PATTERN.match("John Doe")
        assert ALLOWED_NAME_PATTERN.match("O'Connor")
        assert ALLOWED_NAME_PATTERN.match("Mary-Jane")

    @pytest.mark.unit
    def test_allowed_pattern_rejects_invalid(self) -> None:
        """Test ALLOWED_NAME_PATTERN rejects invalid names."""
        assert not ALLOWED_NAME_PATTERN.match("Test<script>")
        assert not ALLOWED_NAME_PATTERN.match("Name@email")
