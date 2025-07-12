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
- Updated documentation with better examples and usage instructions
- ✅ Refactored GitHub Actions workflows for better separation of concerns
  - Split single `tests.yml` into dedicated `tests.yml` and `ci.yml` workflows
  - Removed `continue-on-error` from code quality checks to enforce standards
  - Added auto-fixing capabilities for black and isort in CI pipeline
  - All local tests and quality checks pass successfully

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
