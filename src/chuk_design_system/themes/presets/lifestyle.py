"""Lifestyle theme preset - Warm pink/coral palette."""

from chuk_design_system.themes.base import BaseTheme, ThemeColors, ThemeMotion

LIFESTYLE_THEME = BaseTheme(
    name="Lifestyle",
    description="Warm lifestyle theme with pink/coral palette. Perfect for lifestyle, wellness, and personal brands.",
    category="lifestyle",
    colors=ThemeColors(
        primary_hue="pink",
        mode="light",
        gradient="linear-gradient(135deg, #FF6B9D 0%, #FFB74D 100%)",
    ),
    motion=ThemeMotion(
        default_duration="slower",
        default_easing="smooth",
        default_spring="gentle",
    ),
    tags=["warm", "lifestyle", "personal", "welcoming"],
)
