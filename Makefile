# Makefile for chuk-design-system

.PHONY: help install install-dev test test-cov test-watch lint format clean build publish example docs

# Default target
help:
	@echo "chuk-design-system Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install       - Install package in development mode"
	@echo "  install-dev   - Install package with dev dependencies"
	@echo "  test          - Run tests"
	@echo "  test-cov      - Run tests with coverage report"
	@echo "  test-watch    - Run tests in watch mode"
	@echo "  test-file     - Run specific test file (usage: make test-file FILE=test_colors.py)"
	@echo "  lint          - Run linters (ruff)"
	@echo "  format        - Format code (black + ruff)"
	@echo "  type-check    - Run mypy type checking"
	@echo "  clean         - Remove build artifacts and cache files"
	@echo "  build         - Build distribution packages"
	@echo "  publish       - Publish to PyPI (requires auth)"
	@echo "  example       - Run basic usage example"
	@echo "  docs          - Generate HTML documentation"
	@echo "  all           - Run format, lint, type-check, test-cov"

# Installation targets
install:
	uv pip install -e .

install-dev:
	uv pip install -e ".[dev]"

# Testing targets
test:
	source .venv/bin/activate && pytest tests/ -v

test-cov:
	source .venv/bin/activate && pytest tests/ --cov=src/chuk_design_system --cov-report=term-missing --cov-report=html -v

test-watch:
	source .venv/bin/activate && pytest-watch tests/ -v

test-file:
	source .venv/bin/activate && pytest tests/$(FILE) -v

test-quick:
	source .venv/bin/activate && pytest tests/ -v -x --tb=short

# Quality targets
lint:
	ruff check src/ tests/

format:
	black src/ tests/ examples/
	ruff check --fix src/ tests/

type-check:
	mypy src/

# Cleanup targets
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Build and publish
build: clean
	python -m build

publish: build
	python -m twine upload dist/*

# Examples and documentation
example:
	source .venv/bin/activate && python examples/basic_usage.py

docs:
	@echo "Documentation files:"
	@echo "  README.md - Main documentation"
	@echo "  USAGE.md  - Usage guide"
	@echo ""
	@echo "To view HTML coverage report:"
	@echo "  open htmlcov/index.html"

# CI/CD simulation
all: format lint type-check test-cov
	@echo ""
	@echo "✅ All checks passed!"

# Coverage by file
cov-report:
	source .venv/bin/activate && pytest tests/ --cov=src/chuk_design_system --cov-report=term | grep -E "(Name|src/chuk_design_system/(tokens|themes|exporters)/[^/]+\.py|TOTAL)"

# Show test stats
test-stats:
	@echo "Test Statistics:"
	@source .venv/bin/activate && pytest tests/ --collect-only -q | tail -1
	@echo ""
	@echo "Coverage by module:"
	@source .venv/bin/activate && pytest tests/ --cov=src/chuk_design_system --cov-report=term --quiet 2>/dev/null | grep -E "(Name|src/|TOTAL)" | head -20

# Development helpers
venv:
	uv venv
	@echo ""
	@echo "Virtual environment created. Activate with:"
	@echo "  source .venv/bin/activate"

setup: venv install-dev
	@echo ""
	@echo "✅ Development environment ready!"
	@echo "Run 'make test' to verify installation"

# Export examples
export-examples:
	@echo "Exporting all themes to all formats..."
	@mkdir -p exports/{canva,remotion,css,w3c}
	@python -c "from chuk_design_system.themes import THEMES, get_theme; \
		from chuk_design_system.exporters import *; \
		import json; \
		for name in THEMES.keys(): \
			theme = get_theme(name); \
			open(f'exports/canva/{name}.css', 'w').write(export_to_canva_css(theme)); \
			open(f'exports/remotion/{name}.ts', 'w').write(export_to_remotion_ts(theme)); \
			open(f'exports/css/{name}.css', 'w').write(export_to_css(theme)); \
			open(f'exports/w3c/{name}.json', 'w').write(export_to_w3c_json(theme))"
	@echo "✅ Exports created in exports/ directory"

# Benchmarking
benchmark:
	@echo "Running benchmarks..."
	@python -m timeit -n 1000 "from chuk_design_system.themes import get_theme; get_theme('tech')"

# Version management
version:
	@grep "^version" pyproject.toml | cut -d'"' -f2

bump-patch:
	@echo "Bumping patch version..."
	@python -c "import re; \
		content = open('pyproject.toml').read(); \
		new_content = re.sub(r'version = \"(\d+)\.(\d+)\.(\d+)\"', \
		lambda m: f'version = \"{m.group(1)}.{m.group(2)}.{int(m.group(3))+1}\"', content); \
		open('pyproject.toml', 'w').write(new_content)"
	@echo "New version: $$(make version)"

# Show project info
info:
	@echo "Project: chuk-design-system"
	@echo "Version: $$(make version)"
	@echo "Python: $$(python --version)"
	@echo ""
	@echo "Project structure:"
	@tree -L 2 src/ -I __pycache__ 2>/dev/null || find src/ -type d -not -path "*/\.*" | head -20

# Showcase targets
showcase-visual:
	@echo "Generating visual PNG showcases..."
	source .venv/bin/activate && python examples/showcase_visual.py
	@echo "✅ PNG showcases generated in output/ directory"
	@echo "Opening interactive HTML showcase..."
	open examples/showcase_interactive.html

showcase-html:
	@echo "Opening interactive HTML showcase..."
	open examples/showcase_interactive.html

showcase: showcase-visual
	@echo ""
	@echo "✅ Design system showcase complete!"
	@echo "   - PNG images: output/"
	@echo "   - Interactive HTML: examples/showcase_interactive.html"
