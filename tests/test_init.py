"""
Tests for package initialization.

Author: JacobPEvans
Created: July 13, 2025
"""

from unittest.mock import patch


class TestPackageInit:
    """Test cases for package initialization."""

    def test_logging_config_missing_file(self) -> None:
        """Test package initialization when logging.conf doesn't exist."""
        with patch("os.path.exists", return_value=False):
            # Re-import the module to trigger the initialization code
            import importlib

            import hello_world

            importlib.reload(hello_world)

        # Verify the module still works despite missing config
        assert hello_world.greet() == "Hello, World!"
