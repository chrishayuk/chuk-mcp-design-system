"""Minimal theme preset - Clean monochrome palette."""

from chuk_design_system.themes.base import BaseTheme, ThemeColors, ThemeMotion

MINIMAL_THEME = BaseTheme(
    name="Minimal",
    description="Clean minimal theme with monochrome palette. Perfect for minimalist design and typography-focused content.",
    category="minimal",
    colors=ThemeColors(
        primary_hue="zinc",
        mode="light",
        gradient="linear-gradient(135deg, #212121 0%, #616161 100%)",
    ),
    motion=ThemeMotion(
        default_duration="slow",
        default_easing="ease",
        default_spring="stiff",
    ),
    tags=["minimal", "clean", "simple", "elegant"],
)
