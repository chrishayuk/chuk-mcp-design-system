"""Education theme preset - Friendly purple/orange palette."""

from chuk_design_system.themes.base import BaseTheme, ThemeColors, ThemeMotion

EDUCATION_THEME = BaseTheme(
    name="Education",
    description="Friendly education theme with purple/orange palette. Great for tutorials, courses, and learning content.",
    category="education",
    colors=ThemeColors(
        primary_hue="purple",
        mode="dark",
        gradient="linear-gradient(135deg, #7C4DFF 0%, #FF6E40 100%)",
    ),
    motion=ThemeMotion(
        default_duration="normal",
        default_easing="ease_out",
        default_spring="bouncy",
    ),
    tags=["friendly", "education", "learning", "approachable"],
)
