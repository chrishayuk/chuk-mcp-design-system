"""
Design tokens package.

Exports all token categories and provides unified access to the token system.
"""

from chuk_design_system.tokens.colors import ColorTokens, PALETTE, GRADIENTS
from chuk_design_system.tokens.typography import (
    TypographyTokens,
    FONT_FAMILIES,
    FONT_SIZES,
    FONT_WEIGHTS,
    TEXT_STYLES,
)
from chuk_design_system.tokens.spacing import (
    SpacingTokens,
    SPACING,
    SAFE_AREAS,
    GRID,
    CONTAINERS,
)
from chuk_design_system.tokens.motion import (
    MotionTokens,
    DURATIONS,
    EASINGS,
    SPRINGS,
)

__all__ = [
    # Token classes
    "ColorTokens",
    "TypographyTokens",
    "SpacingTokens",
    "MotionTokens",
    # Color exports
    "PALETTE",
    "GRADIENTS",
    # Typography exports
    "FONT_FAMILIES",
    "FONT_SIZES",
    "FONT_WEIGHTS",
    "TEXT_STYLES",
    # Spacing exports
    "SPACING",
    "SAFE_AREAS",
    "GRID",
    "CONTAINERS",
    # Motion exports
    "DURATIONS",
    "EASINGS",
    "SPRINGS",
    # Utility functions
    "get_all_tokens",
]


def get_all_tokens(primary_hue: str = "blue", mode: str = "dark", medium: str = "web") -> dict:
    """
    Get all design tokens as a single dictionary.

    Args:
        primary_hue: Primary color hue for semantic colors
        mode: Color mode (dark/light)
        medium: Typography medium (web, pptx, video_1080p, video_4k)

    Returns:
        Dictionary containing all token categories
    """
    colors = ColorTokens()
    typography = TypographyTokens()
    spacing = SpacingTokens()
    motion = MotionTokens()

    return {
        "colors": colors.get_all(primary_hue, mode),
        "typography": typography.get_all(medium),
        "spacing": spacing.get_all(),
        "motion": motion.get_all(),
    }
