# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Calendar Versioning](https://calver.org/).

## [Unreleased]

### Added
- Initial project setup with modern Python packaging
- Comprehensive test suite with pytest
- Code quality tools (black, isort, flake8, mypy)
- Pre-commit hooks configuration
- Type hints throughout the codebase

### Changed
- ✅ Refactored GitHub Actions workflows for better separation of concerns
  - Split single `tests.yml` into dedicated `tests.yml` and `ci.yml` workflows
  - Removed `continue-on-error` from code quality checks to enforce standards
  - Added auto-fixing capabilities for black and isort in CI pipeline
  - Updated `ci.yml` to run on all branches for comprehensive code quality enforcement
  - All local tests and quality checks pass successfully
- Enhanced documentation with clearer setup instructions
  - Updated README.md with explicit virtual environment setup steps (.venv convention)
  - Added clear notes about pre-commit hook behavior and auto-fixing
  - Updated project structure to reflect new dual workflow setup
  - Clarified development vs production installation approaches

### Fixed
- N/A

## [2025.07.12]

### Added
- Initial release
- Basic hello world functionality
- Project template structure
- GNU General Public License v3
- README documentation

[Unreleased]: https://github.com/JacobPEvans/python-template/compare/v2025.07.12...HEAD
[2025.07.12]: https://github.com/JacobPEvans/python-template/releases/tag/v2025.07.12
