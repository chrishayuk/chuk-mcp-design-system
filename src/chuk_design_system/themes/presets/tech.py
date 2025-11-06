"""Tech theme preset - Modern blue/cyan palette."""

from chuk_design_system.themes.base import BaseTheme, ThemeColors, ThemeMotion

TECH_THEME = BaseTheme(
    name="Tech",
    description="Modern tech aesthetic with blue/cyan palette. Perfect for technology, SaaS, and digital content.",
    category="tech",
    colors=ThemeColors(
        primary_hue="blue",
        mode="dark",
        gradient="linear-gradient(135deg, #0066FF 0%, #00D9FF 100%)",
    ),
    motion=ThemeMotion(
        default_duration="fast",
        default_easing="smooth",
        default_spring="snappy",
    ),
    tags=["modern", "technology", "professional", "clean"],
)
