# Makefile for Python project development tasks
# Usage: make <target>

.PHONY: help install install-dev clean lint format test test-cov test-fast security type-check all pre-commit docs build

# Default target
.DEFAULT_GOAL := help

# Project settings
PYTHON := python3
PIP := $(PYTHON) -m pip
PYTEST := $(PYTHON) -m pytest
SRC_DIR := src
TEST_DIR := tests

# Colors for terminal output
BLUE := \033[34m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
RESET := \033[0m

help: ## Show this help message
	@echo "$(BLUE)Available targets:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(RESET) %s\n", $$1, $$2}'

# =============================================================================
# Installation
# =============================================================================

install: ## Install package in production mode
	$(PIP) install -e .

install-dev: ## Install package with development dependencies
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"
	pre-commit install

# =============================================================================
# Code Quality
# =============================================================================

lint: ## Run all linters (ruff, flake8, mypy)
	@echo "$(BLUE)Running Ruff...$(RESET)"
	ruff check $(SRC_DIR) $(TEST_DIR)
	@echo "$(BLUE)Running flake8...$(RESET)"
	flake8 $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)All linting passed!$(RESET)"

lint-fix: ## Run linters with auto-fix enabled
	@echo "$(BLUE)Running Ruff with auto-fix...$(RESET)"
	ruff check --fix $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)Auto-fix complete!$(RESET)"

format: ## Format code with Ruff and Black
	@echo "$(BLUE)Formatting and sorting imports with Ruff...$(RESET)"
	ruff check --fix $(SRC_DIR) $(TEST_DIR)
	ruff format $(SRC_DIR) $(TEST_DIR)
	@echo "$(BLUE)Formatting with Black...$(RESET)"
	black $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)Formatting complete!$(RESET)"

format-check: ## Check code formatting without making changes
	@echo "$(BLUE)Checking Ruff format...$(RESET)"
	ruff format --check $(SRC_DIR) $(TEST_DIR)
	@echo "$(BLUE)Checking Black formatting...$(RESET)"
	black --check $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)Format check passed!$(RESET)"

type-check: ## Run mypy type checker
	@echo "$(BLUE)Running mypy...$(RESET)"
	mypy $(SRC_DIR)
	@echo "$(GREEN)Type checking passed!$(RESET)"

security: ## Run security checks (bandit, pip-audit)
	@echo "$(BLUE)Running Bandit security scan...$(RESET)"
	bandit -r $(SRC_DIR) -c pyproject.toml
	@echo "$(BLUE)Running pip-audit...$(RESET)"
	pip-audit
	@echo "$(GREEN)Security checks passed!$(RESET)"

# =============================================================================
# Testing
# =============================================================================

test: ## Run all tests
	@echo "$(BLUE)Running tests...$(RESET)"
	$(PYTEST) $(TEST_DIR) -v

test-cov: ## Run tests with coverage report
	@echo "$(BLUE)Running tests with coverage...$(RESET)"
	$(PYTEST) --cov --cov-branch --cov-report=term-missing --cov-report=html --cov-fail-under=100

test-fast: ## Run tests in parallel (faster)
	@echo "$(BLUE)Running tests in parallel...$(RESET)"
	$(PYTEST) $(TEST_DIR) -n auto -v

test-unit: ## Run only unit tests
	@echo "$(BLUE)Running unit tests...$(RESET)"
	$(PYTEST) $(TEST_DIR) -v -m unit

test-integration: ## Run only integration tests
	@echo "$(BLUE)Running integration tests...$(RESET)"
	$(PYTEST) $(TEST_DIR) -v -m integration

test-watch: ## Run tests in watch mode (requires pytest-watch)
	@echo "$(BLUE)Running tests in watch mode...$(RESET)"
	ptw -- -v

# =============================================================================
# Pre-commit
# =============================================================================

pre-commit: ## Run pre-commit hooks on all files
	@echo "$(BLUE)Running pre-commit hooks...$(RESET)"
	pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	@echo "$(BLUE)Updating pre-commit hooks...$(RESET)"
	pre-commit autoupdate

# =============================================================================
# Build & Documentation
# =============================================================================

build: clean ## Build distribution packages
	@echo "$(BLUE)Building distribution packages...$(RESET)"
	$(PYTHON) -m build
	@echo "$(GREEN)Build complete!$(RESET)"

docs: ## Generate documentation (placeholder)
	@echo "$(YELLOW)Documentation generation not yet configured$(RESET)"

# =============================================================================
# Cleanup
# =============================================================================

clean: ## Remove build artifacts and cache files
	@echo "$(BLUE)Cleaning up...$(RESET)"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "$(GREEN)Cleanup complete!$(RESET)"

# =============================================================================
# Combined Targets
# =============================================================================

all: format lint type-check security test-cov ## Run all quality checks and tests

ci: format-check lint type-check security test-cov ## Run CI pipeline locally

check: lint type-check test ## Quick check (lint, type-check, test)
