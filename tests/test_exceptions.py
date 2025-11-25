"""Tests for exceptions module.

Author: JacobPEvans
"""

import pytest

from hello_world.exceptions import (
    BatchGreetingError,
    ConfigurationError,
    GreetingError,
    HelloWorldError,
    ValidationError,
)


class TestHelloWorldError:
    """Test cases for base HelloWorldError exception."""

    @pytest.mark.unit
    def test_basic_error(self) -> None:
        """Test basic error creation."""
        error = HelloWorldError("Test error message")
        assert str(error) == "Test error message"
        assert error.message == "Test error message"
        assert error.details is None

    @pytest.mark.unit
    def test_error_with_details(self) -> None:
        """Test error creation with details."""
        error = HelloWorldError("Test error", "Additional details")
        assert str(error) == "Test error - Details: Additional details"
        assert error.message == "Test error"
        assert error.details == "Additional details"

    @pytest.mark.unit
    def test_error_repr(self) -> None:
        """Test error __repr__ method."""
        error = HelloWorldError("Test", "Details")
        repr_str = repr(error)
        assert "HelloWorldError" in repr_str
        assert "Test" in repr_str
        assert "Details" in repr_str

    @pytest.mark.unit
    def test_error_is_exception(self) -> None:
        """Test that HelloWorldError is an Exception."""
        error = HelloWorldError("Test")
        assert isinstance(error, Exception)

    @pytest.mark.unit
    def test_error_can_be_raised(self) -> None:
        """Test that error can be raised and caught."""
        with pytest.raises(HelloWorldError) as exc_info:
            raise HelloWorldError("Raised error")
        assert str(exc_info.value) == "Raised error"


class TestValidationError:
    """Test cases for ValidationError exception."""

    @pytest.mark.unit
    def test_validation_error_creation(self) -> None:
        """Test ValidationError creation."""
        error = ValidationError(
            field="username",
            value="x",
            reason="too short",
        )
        assert error.field == "username"
        assert error.value == "x"
        assert error.reason == "too short"
        assert "username" in str(error)
        assert "too short" in str(error)

    @pytest.mark.unit
    def test_validation_error_with_details(self) -> None:
        """Test ValidationError with details."""
        error = ValidationError(
            field="email",
            value="invalid",
            reason="invalid format",
            details="Must contain @",
        )
        assert error.details == "Must contain @"
        assert "Details:" in str(error)

    @pytest.mark.unit
    def test_validation_error_inheritance(self) -> None:
        """Test that ValidationError inherits from HelloWorldError."""
        error = ValidationError("field", "value", "reason")
        assert isinstance(error, HelloWorldError)
        assert isinstance(error, Exception)

    @pytest.mark.unit
    def test_validation_error_with_fixture(
        self, sample_validation_error: dict[str, object]
    ) -> None:
        """Test ValidationError creation using fixture."""
        error = ValidationError(**sample_validation_error)  # type: ignore[arg-type]
        assert error.field == sample_validation_error["field"]
        assert error.value == sample_validation_error["value"]


class TestConfigurationError:
    """Test cases for ConfigurationError exception."""

    @pytest.mark.unit
    def test_configuration_error_creation(self) -> None:
        """Test ConfigurationError creation."""
        error = ConfigurationError(
            config_key="DATABASE_URL",
            expected="valid connection string",
        )
        assert error.config_key == "DATABASE_URL"
        assert error.expected == "valid connection string"
        assert "DATABASE_URL" in str(error)

    @pytest.mark.unit
    def test_configuration_error_with_details(self) -> None:
        """Test ConfigurationError with details."""
        error = ConfigurationError(
            config_key="API_KEY",
            expected="non-empty string",
            details="Check environment variables",
        )
        assert error.details == "Check environment variables"

    @pytest.mark.unit
    def test_configuration_error_inheritance(self) -> None:
        """Test that ConfigurationError inherits from HelloWorldError."""
        error = ConfigurationError("key", "expected")
        assert isinstance(error, HelloWorldError)

    @pytest.mark.unit
    def test_configuration_error_with_fixture(
        self, sample_configuration_error: dict[str, str]
    ) -> None:
        """Test ConfigurationError creation using fixture."""
        error = ConfigurationError(**sample_configuration_error)
        assert error.config_key == sample_configuration_error["config_key"]


class TestGreetingError:
    """Test cases for GreetingError exception."""

    @pytest.mark.unit
    def test_greeting_error_without_name(self) -> None:
        """Test GreetingError creation without name."""
        error = GreetingError(error_type="invalid_input")
        assert error.error_type == "invalid_input"
        assert error.name is None
        assert "invalid_input" in str(error)

    @pytest.mark.unit
    def test_greeting_error_with_name(self) -> None:
        """Test GreetingError creation with name."""
        error = GreetingError(error_type="validation_failed", name="BadName")
        assert error.name == "BadName"
        assert "BadName" in str(error)

    @pytest.mark.unit
    def test_greeting_error_with_details(self) -> None:
        """Test GreetingError with details."""
        error = GreetingError(
            error_type="length_exceeded",
            name="VeryLongName",
            details="Max length is 100",
        )
        assert error.details == "Max length is 100"

    @pytest.mark.unit
    def test_greeting_error_inheritance(self) -> None:
        """Test that GreetingError inherits from HelloWorldError."""
        error = GreetingError("error")
        assert isinstance(error, HelloWorldError)


class TestBatchGreetingError:
    """Test cases for BatchGreetingError exception."""

    @pytest.mark.unit
    def test_batch_error_creation(self) -> None:
        """Test BatchGreetingError creation."""
        error = BatchGreetingError(
            failed_names=["Bad1", "Bad2"],
            total_count=5,
            success_count=3,
        )
        assert error.failed_names == ["Bad1", "Bad2"]
        assert error.total_count == 5
        assert error.success_count == 3
        assert "2/5 failures" in str(error)

    @pytest.mark.unit
    def test_batch_error_truncates_names(self) -> None:
        """Test that BatchGreetingError truncates long lists of names."""
        many_names = [f"Name{i}" for i in range(10)]
        error = BatchGreetingError(
            failed_names=many_names,
            total_count=10,
            success_count=0,
        )
        # Should show ... for truncated names
        assert "..." in str(error)

    @pytest.mark.unit
    def test_batch_error_shows_all_short_list(self) -> None:
        """Test that short lists of names are shown completely."""
        error = BatchGreetingError(
            failed_names=["A", "B"],
            total_count=2,
            success_count=0,
        )
        # Should not have truncation
        error_str = str(error)
        assert "A" in error_str
        assert "B" in error_str

    @pytest.mark.unit
    def test_batch_error_inheritance(self) -> None:
        """Test that BatchGreetingError inherits from HelloWorldError."""
        error = BatchGreetingError([], 0, 0)
        assert isinstance(error, HelloWorldError)

    @pytest.mark.unit
    def test_batch_error_failed_names_is_copy(self) -> None:
        """Test that failed_names is a copy, not the original list."""
        original = ["Name1", "Name2"]
        error = BatchGreetingError(original, 2, 0)
        original.append("Name3")
        assert len(error.failed_names) == 2


class TestExceptionCatching:
    """Test cases for exception catching patterns."""

    @pytest.mark.unit
    def test_catch_all_package_errors(self) -> None:
        """Test catching all package errors with base class."""
        errors = [
            HelloWorldError("base"),
            ValidationError("f", "v", "r"),
            ConfigurationError("k", "e"),
            GreetingError("t"),
            BatchGreetingError([], 0, 0),
        ]
        for error in errors:
            with pytest.raises(HelloWorldError):
                raise error

    @pytest.mark.unit
    def test_specific_error_not_caught_by_sibling(self) -> None:
        """Test that specific errors aren't caught by sibling classes."""
        with pytest.raises(ValidationError):
            try:
                raise ValidationError("f", "v", "r")
            except ConfigurationError:
                pytest.fail("Should not catch ValidationError")
