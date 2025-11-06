# Makefile Quick Reference

## Common Commands

### Testing
```bash
make test           # Run all tests
make test-cov       # Run tests with coverage report
make test-quick     # Run tests with early exit on failure
make test-file FILE=test_colors.py  # Run specific test file
make cov-report     # Show coverage by file
make test-stats     # Show test statistics
```

### Development
```bash
make install        # Install package in development mode
make install-dev    # Install with dev dependencies
make example        # Run basic usage examples
make clean          # Clean build artifacts
```

### Code Quality
```bash
make format         # Format code with black + ruff
make lint           # Run linters
make type-check     # Run mypy type checking
make all            # Run format, lint, type-check, test-cov
```

### Build & Publish
```bash
make build          # Build distribution packages
make publish        # Publish to PyPI
make version        # Show current version
make bump-patch     # Bump patch version (0.1.0 → 0.1.1)
```

### Utilities
```bash
make help           # Show all available targets
make info           # Show project information
make export-examples  # Export all themes to all formats
make docs           # Show documentation info
```

## Test Coverage Goals

- **Overall**: 88% (203 tests)
- **Core Modules**: 90%+ coverage
  - Tokens: 100%
  - Themes: 95%+
  - Exporters: 100% (except optional dependencies)

## Quick Start

```bash
# Set up development environment
make setup

# Run tests with coverage
make test-cov

# Run example
make example

# Format and check code
make format
make lint

# Run all checks (CI simulation)
make all
```

## Coverage Report

After running `make test-cov`, view the HTML report:
```bash
open htmlcov/index.html
```

## Export Examples

Generate all theme exports:
```bash
make export-examples
```

This creates:
```
exports/
├── canva/      # CSS variables for Canva apps
├── remotion/   # TypeScript for Remotion
├── css/        # Standard CSS
└── w3c/        # W3C Design Tokens JSON
```

## Tips

- Use `make test-quick` during development for fast feedback
- Run `make all` before committing to ensure code quality
- Use `make test-file FILE=...` to test specific modules
- Check `make help` for complete list of targets
