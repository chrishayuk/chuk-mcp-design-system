"""
Typography tokens - Universal typography system.

Combines:
- Font family definitions
- Multi-resolution font scales (web, presentation, video)
- Text style presets
- Font weights, line heights, letter spacing
"""

from typing import Any
from chuk_design_system.tokens.models import FontFamily, FontSizeScale, TextStyle


# ============================================================================
# FONT FAMILIES
# ============================================================================

FONT_FAMILIES = {
    "display": FontFamily(
        name="Display",
        fonts=["Inter", "SF Pro Display", "system-ui", "sans-serif"],
        description="Large headings and titles",
        usage="Headlines, hero text, main titles",
    ),
    "body": FontFamily(
        name="Body",
        fonts=["Inter", "SF Pro Text", "system-ui", "sans-serif"],
        description="Body text and paragraphs",
        usage="Paragraphs, descriptions, captions",
    ),
    "mono": FontFamily(
        name="Monospace",
        fonts=["JetBrains Mono", "Fira Code", "Monaco", "Consolas", "monospace"],
        description="Code and technical content",
        usage="Code blocks, technical text, data",
    ),
    "decorative": FontFamily(
        name="Decorative",
        fonts=["Poppins", "Montserrat", "Raleway", "sans-serif"],
        description="Special emphasis and style",
        usage="Stylized text, special callouts, branding",
    ),
}


# ============================================================================
# FONT SIZES
# ============================================================================

# Web/Presentation font sizes (px)
FONT_SIZES_WEB = FontSizeScale(
    xs="12px",
    sm="14px",
    base="16px",
    lg="18px",
    xl="20px",
    xxl="24px",
    xxxl="30px",
    xxxxl="36px",
)

# PowerPoint font sizes (pt)
FONT_SIZES_PPTX = FontSizeScale(
    xs="14pt",
    sm="16pt",
    base="18pt",
    lg="24pt",
    xl="32pt",
    xxl="40pt",
    xxxl="48pt",
    xxxxl="60pt",
)

# Video font sizes - 1080p (larger for readability)
FONT_SIZES_VIDEO_1080P = FontSizeScale(
    xs="24px",
    sm="32px",
    base="40px",
    lg="48px",
    xl="64px",
    xxl="80px",
    xxxl="96px",
    xxxxl="120px",
)

# Video font sizes - 4K
FONT_SIZES_VIDEO_4K = FontSizeScale(
    xs="48px",
    sm="64px",
    base="80px",
    lg="96px",
    xl="128px",
    xxl="160px",
    xxxl="192px",
    xxxxl="240px",
)

# Unified font sizes dictionary
FONT_SIZES = {
    "web": FONT_SIZES_WEB,
    "pptx": FONT_SIZES_PPTX,
    "video_1080p": FONT_SIZES_VIDEO_1080P,
    "video_4k": FONT_SIZES_VIDEO_4K,
}


# ============================================================================
# FONT WEIGHTS
# ============================================================================

FONT_WEIGHTS = {
    "thin": 100,
    "extralight": 200,
    "light": 300,
    "regular": 400,
    "medium": 500,
    "semibold": 600,
    "bold": 700,
    "extrabold": 800,
    "black": 900,
}


# ============================================================================
# LINE HEIGHTS
# ============================================================================

LINE_HEIGHTS = {
    "none": 1.0,
    "tight": 1.1,
    "snug": 1.25,
    "normal": 1.5,
    "relaxed": 1.75,
    "loose": 2.0,
}


# ============================================================================
# LETTER SPACING
# ============================================================================

LETTER_SPACING = {
    "tighter": "-0.05em",
    "tight": "-0.025em",
    "normal": "0",
    "wide": "0.025em",
    "wider": "0.05em",
    "widest": "0.1em",
}


# ============================================================================
# TEXT STYLE PRESETS
# ============================================================================

# These use semantic size names that can be resolved per-medium
TEXT_STYLES = {
    "hero_title": TextStyle(
        name="Hero Title",
        fontSize="4xl",
        fontWeight="black",
        lineHeight="tight",
        letterSpacing="tight",
        fontFamily="display",
    ),
    "title": TextStyle(
        name="Title",
        fontSize="3xl",
        fontWeight="bold",
        lineHeight="tight",
        letterSpacing="tight",
        fontFamily="display",
    ),
    "heading": TextStyle(
        name="Heading",
        fontSize="2xl",
        fontWeight="semibold",
        lineHeight="snug",
        letterSpacing="normal",
        fontFamily="display",
    ),
    "subheading": TextStyle(
        name="Subheading",
        fontSize="xl",
        fontWeight="medium",
        lineHeight="snug",
        letterSpacing="normal",
        fontFamily="display",
    ),
    "body": TextStyle(
        name="Body",
        fontSize="base",
        fontWeight="regular",
        lineHeight="normal",
        letterSpacing="normal",
        fontFamily="body",
    ),
    "caption": TextStyle(
        name="Caption",
        fontSize="sm",
        fontWeight="medium",
        lineHeight="relaxed",
        letterSpacing="wide",
        fontFamily="body",
    ),
    "small": TextStyle(
        name="Small",
        fontSize="xs",
        fontWeight="regular",
        lineHeight="relaxed",
        letterSpacing="normal",
        fontFamily="body",
    ),
}


# ============================================================================
# TYPOGRAPHY SCALE (Canva-compatible naming)
# ============================================================================

# Maps semantic roles to size tokens
TYPOGRAPHY_SCALE = {
    "title_large": "4xl",
    "title_medium": "3xl",
    "title_small": "2xl",
    "body_large": "lg",
    "body_medium": "base",
    "body_small": "sm",
}


# ============================================================================
# TYPOGRAPHY TOKENS CLASS
# ============================================================================


class TypographyTokens:
    """Complete typography token system."""

    def __init__(self) -> None:
        self.families = FONT_FAMILIES
        self.sizes = FONT_SIZES
        self.weights = FONT_WEIGHTS
        self.line_heights = LINE_HEIGHTS
        self.letter_spacing = LETTER_SPACING
        self.text_styles = TEXT_STYLES
        self.scale = TYPOGRAPHY_SCALE

    def get_text_style(self, style_name: str, medium: str = "web") -> dict[str, Any]:
        """
        Get a text style with resolved font sizes for specific medium.

        Args:
            style_name: Name of text style (e.g., "hero_title")
            medium: Target medium (web, pptx, video_1080p, video_4k)

        Returns:
            Dictionary with resolved font properties
        """
        if style_name not in TEXT_STYLES:
            raise ValueError(f"Unknown text style: {style_name}")

        style = TEXT_STYLES[style_name]
        sizes = self.sizes[medium]

        # Map semantic size name to actual size
        size_map = {
            "xs": sizes.xs,
            "sm": sizes.sm,
            "base": sizes.base,
            "lg": sizes.lg,
            "xl": sizes.xl,
            "2xl": sizes.xxl,
            "3xl": sizes.xxxl,
            "4xl": sizes.xxxxl,
        }

        return {
            "name": style.name,
            "fontSize": size_map.get(style.fontSize, sizes.base),
            "fontWeight": self.weights.get(style.fontWeight, 400),
            "lineHeight": self.line_heights.get(style.lineHeight, 1.5),
            "letterSpacing": self.letter_spacing.get(style.letterSpacing, "0"),
            "fontFamily": ", ".join(self.families[style.fontFamily].fonts),
        }

    def get_all(self, medium: str = "web") -> dict[str, Any]:
        """Get all typography tokens as dictionary."""
        return {
            "families": {k: v.model_dump() for k, v in self.families.items()},
            "sizes": self.sizes[medium].model_dump(),
            "weights": self.weights,
            "lineHeights": self.line_heights,
            "letterSpacing": self.letter_spacing,
            "textStyles": {k: v.model_dump() for k, v in self.text_styles.items()},
            "scale": self.scale,
        }
