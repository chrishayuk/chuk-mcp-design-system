"""
Base theme structure and utilities.

Defines how themes combine tokens from different categories.
"""

from typing import Any
from pydantic import BaseModel, Field


class ThemeColors(BaseModel):
    """Color configuration for a theme."""

    primary_hue: str = Field(description="Primary color hue from palette")
    mode: str = Field(description="dark or light")
    gradient: str | None = Field(None, description="Optional gradient override")


class ThemeTypography(BaseModel):
    """Typography configuration for a theme."""

    medium: str = Field(default="web", description="Typography medium")
    primary_font: str = Field(default="display", description="Primary font family")
    body_font: str = Field(default="body", description="Body font family")


class ThemeSpacing(BaseModel):
    """Spacing configuration for a theme."""

    density: str = Field(default="normal", description="Spacing density")
    safe_area: str | None = Field(None, description="Platform-specific safe area")


class ThemeMotion(BaseModel):
    """Motion configuration for a theme."""

    default_duration: str = Field(default="normal")
    default_easing: str = Field(default="ease_out")
    default_spring: str = Field(default="smooth")


class BaseTheme(BaseModel):
    """
    Base theme configuration.

    Themes reference token values rather than defining new ones.
    """

    name: str
    description: str
    category: str
    colors: ThemeColors
    typography: ThemeTypography = Field(default_factory=ThemeTypography)
    spacing: ThemeSpacing = Field(default_factory=ThemeSpacing)
    motion: ThemeMotion = Field(default_factory=ThemeMotion)
    tags: list[str] = Field(default_factory=list)


def resolve_theme(theme: BaseTheme) -> dict[str, Any]:
    """
    Resolve a theme configuration into actual token values.

    Args:
        theme: Theme configuration

    Returns:
        Dictionary with resolved token values
    """
    from chuk_design_system.tokens import (
        ColorTokens,
        TypographyTokens,
        SpacingTokens,
        MotionTokens,
    )

    colors = ColorTokens()
    typography = TypographyTokens()
    spacing = SpacingTokens()
    motion = MotionTokens()

    # Resolve colors
    color_tokens = colors.get_all(theme.colors.primary_hue, theme.colors.mode)
    if theme.colors.gradient:
        color_tokens["gradient"] = theme.colors.gradient

    # Resolve typography
    typography_tokens = typography.get_all(theme.typography.medium)

    # Resolve spacing
    spacing_tokens = spacing.get_all()
    if theme.spacing.safe_area:
        spacing_tokens["activeSafeArea"] = spacing.safe_areas[theme.spacing.safe_area].model_dump()

    # Resolve motion
    motion_tokens = motion.get_all()
    motion_tokens["defaults"] = {
        "duration": theme.motion.default_duration,
        "easing": theme.motion.default_easing,
        "spring": theme.motion.default_spring,
    }

    return {
        "metadata": {
            "name": theme.name,
            "description": theme.description,
            "category": theme.category,
            "tags": theme.tags,
        },
        "colors": color_tokens,
        "typography": typography_tokens,
        "spacing": spacing_tokens,
        "motion": motion_tokens,
    }
