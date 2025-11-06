"""Finance theme preset - Professional green/gold palette."""

from chuk_design_system.themes.base import BaseTheme, ThemeColors, ThemeMotion

FINANCE_THEME = BaseTheme(
    name="Finance",
    description="Professional finance theme with green/gold palette. Ideal for financial services, banking, and investment content.",
    category="finance",
    colors=ThemeColors(
        primary_hue="green",
        mode="dark",
        gradient="linear-gradient(135deg, #00C853 0%, #FFD600 100%)",
    ),
    motion=ThemeMotion(
        default_duration="normal",
        default_easing="ease",
        default_spring="smooth",
    ),
    tags=["professional", "finance", "business", "trustworthy"],
)
