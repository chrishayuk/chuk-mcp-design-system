"""
Themes package - Pre-built design themes.

Themes combine tokens from different categories into cohesive design systems.
"""

from typing import Any
from chuk_design_system.themes.base import BaseTheme, resolve_theme
from chuk_design_system.themes.presets import (
    TECH_THEME,
    FINANCE_THEME,
    EDUCATION_THEME,
    LIFESTYLE_THEME,
    GAMING_THEME,
    BUSINESS_THEME,
    MINIMAL_THEME,
)

# Theme registry
THEMES = {
    "tech": TECH_THEME,
    "finance": FINANCE_THEME,
    "education": EDUCATION_THEME,
    "lifestyle": LIFESTYLE_THEME,
    "gaming": GAMING_THEME,
    "business": BUSINESS_THEME,
    "minimal": MINIMAL_THEME,
}


def list_themes() -> list[dict[str, str]]:
    """
    List all available themes with metadata.

    Returns:
        List of theme metadata dictionaries
    """
    return [
        {
            "name": theme.name,
            "key": key,
            "description": theme.description,
            "category": theme.category,
            "tags": ", ".join(theme.tags),
        }
        for key, theme in THEMES.items()
    ]


def get_theme(name: str) -> dict[str, Any]:
    """
    Get a complete theme with resolved tokens.

    Args:
        name: Theme name (e.g., "tech", "finance")

    Returns:
        Dictionary with complete theme including all resolved tokens

    Raises:
        ValueError: If theme name is not found
    """
    name_lower = name.lower()
    if name_lower not in THEMES:
        available = ", ".join(THEMES.keys())
        raise ValueError(f"Theme '{name}' not found. Available themes: {available}")

    theme = THEMES[name_lower]
    return resolve_theme(theme)


def get_theme_metadata(name: str) -> dict[str, str]:
    """
    Get theme metadata without resolving tokens.

    Args:
        name: Theme name

    Returns:
        Theme metadata dictionary
    """
    name_lower = name.lower()
    if name_lower not in THEMES:
        raise ValueError(f"Theme '{name}' not found")

    theme = THEMES[name_lower]
    return {
        "name": theme.name,
        "description": theme.description,
        "category": theme.category,
        "tags": ", ".join(theme.tags),
    }


__all__ = [
    "BaseTheme",
    "resolve_theme",
    "THEMES",
    "list_themes",
    "get_theme",
    "get_theme_metadata",
]
