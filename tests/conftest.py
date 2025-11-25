"""Pytest configuration and shared fixtures.

This module contains fixtures and configuration that are automatically
available to all tests in the tests directory.

Author: JacobPEvans
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator


# Configure logging for tests
logging.getLogger("hello_world").setLevel(logging.DEBUG)


# =============================================================================
# Fixtures for greet function testing
# =============================================================================


@pytest.fixture
def valid_names() -> list[str]:
    """Provide a list of valid names for testing."""
    return [
        "Alice",
        "Bob",
        "Charlie",
        "Dr. Smith",
        "Mary-Jane",
        "O'Connor",
        "Test User 123",
        "名前",  # Japanese
        "Имя",  # Russian
    ]


@pytest.fixture
def invalid_names() -> list[str]:
    """Provide a list of invalid names for testing."""
    return [
        "A" * 101,  # Too long
        "Name<script>",  # Invalid characters
        "Name;DROP TABLE",  # SQL injection attempt
        "Hello\x00World",  # Null byte
    ]


@pytest.fixture
def edge_case_names() -> list[str | None]:
    """Provide edge case names for testing."""
    return [
        None,
        "",
        "   ",  # Only whitespace
        " Alice ",  # Leading/trailing whitespace
        "A",  # Single character
        "A" * 100,  # Max length
    ]


# =============================================================================
# Fixtures for mocking
# =============================================================================


@pytest.fixture
def mock_logger() -> Generator[MagicMock, None, None]:
    """Provide a mock logger for testing logging behavior."""
    import hello_world.main

    original_logger = hello_world.main.logger
    mock = MagicMock(spec=logging.Logger)
    hello_world.main.logger = mock
    yield mock
    hello_world.main.logger = original_logger


@pytest.fixture
def captured_logs(caplog: pytest.LogCaptureFixture) -> pytest.LogCaptureFixture:
    """Provide log capturing with DEBUG level enabled."""
    caplog.set_level(logging.DEBUG, logger="hello_world.main")
    caplog.set_level(logging.DEBUG, logger="hello_world")
    return caplog


# =============================================================================
# Fixtures for exception testing
# =============================================================================


@pytest.fixture
def sample_validation_error() -> dict[str, object]:
    """Provide sample data for creating a ValidationError."""
    return {
        "field": "test_field",
        "value": "test_value",
        "reason": "test_reason",
        "details": "test_details",
    }


@pytest.fixture
def sample_configuration_error() -> dict[str, str]:
    """Provide sample data for creating a ConfigurationError."""
    return {
        "config_key": "test_key",
        "expected": "test_expected",
        "details": "test_details",
    }


# =============================================================================
# Markers and hooks
# =============================================================================


def pytest_configure(config: pytest.Config) -> None:
    """Configure custom pytest markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow running")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")


# =============================================================================
# Autouse fixtures
# =============================================================================


@pytest.fixture(autouse=True)
def _ensure_logging_propagates() -> Generator[None, None, None]:
    """Ensure logging propagates for test capture."""
    logger = logging.getLogger("hello_world.main")
    original_propagate = logger.propagate
    logger.propagate = True
    yield
    logger.propagate = original_propagate
