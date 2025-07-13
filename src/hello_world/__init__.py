"""
Hello World package.

A simple Python package template demonstrating best practices.

Author: JacobPEvans
Created: July 12, 2025
"""

import logging.config
import os

from .main import greet

# Construct the full path to the logging configuration file
config_path = os.path.join(os.path.dirname(__file__), "logging.conf")

# Configure the logging using the file
if os.path.exists(config_path):
    logging.config.fileConfig(config_path)

__version__ = "0.1.0"
__author__ = "JacobPEvans"
__email__ = "20714140+JacobPEvans@users.noreply.github.com"

__all__ = ["greet"]
