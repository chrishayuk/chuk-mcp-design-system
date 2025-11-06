"""Business theme preset - Professional navy/teal palette."""

from chuk_design_system.themes.base import BaseTheme, ThemeColors, ThemeMotion

BUSINESS_THEME = BaseTheme(
    name="Business",
    description="Professional business theme with navy/teal palette. Suitable for corporate, B2B, and professional services.",
    category="business",
    colors=ThemeColors(
        primary_hue="indigo",
        mode="dark",
        gradient="linear-gradient(135deg, #1565C0 0%, #00ACC1 100%)",
    ),
    motion=ThemeMotion(
        default_duration="normal",
        default_easing="ease",
        default_spring="stiff",
    ),
    tags=["professional", "business", "corporate", "reliable"],
)
