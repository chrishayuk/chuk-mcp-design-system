"""Gaming theme preset - High-energy neon palette."""

from chuk_design_system.themes.base import BaseTheme, ThemeColors, ThemeMotion

GAMING_THEME = BaseTheme(
    name="Gaming",
    description="High-energy gaming theme with neon accents. Ideal for gaming content, esports, and entertainment.",
    category="gaming",
    colors=ThemeColors(
        primary_hue="green",
        mode="dark",
        gradient="linear-gradient(135deg, #00E676 0%, #E040FB 100%)",
    ),
    motion=ThemeMotion(
        default_duration="faster",
        default_easing="snappy",
        default_spring="bouncy",
    ),
    tags=["energetic", "gaming", "neon", "bold"],
)
