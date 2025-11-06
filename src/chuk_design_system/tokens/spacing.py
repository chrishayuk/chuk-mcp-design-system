"""
Spacing tokens - Universal spacing system.

Combines:
- 8px-based spacing scale (Canva-compatible: 1u = 8px)
- Layout dimensions (margins, padding, gaps)
- Border radius and widths
- Safe areas for different platforms (YouTube, TikTok, etc.)
- Grid and container configurations
"""

from typing import Any
from chuk_design_system.tokens.models import SafeArea, GridConfig


# ============================================================================
# SPACING SCALE (8px base unit)
# ============================================================================

# Using Canva-compatible naming: 1u = 8px
SPACING = {
    "0": "0px",
    "0.5u": "4px",  # 0.5 units
    "1u": "8px",  # 1 unit (base)
    "1.5u": "12px",  # 1.5 units
    "2u": "16px",  # 2 units
    "3u": "24px",  # 3 units
    "4u": "32px",  # 4 units
    "5u": "40px",  # 5 units
    "6u": "48px",  # 6 units
    "8u": "64px",  # 8 units
    "10u": "80px",  # 10 units
    "12u": "96px",  # 12 units
    "16u": "128px",  # 16 units
    "20u": "160px",  # 20 units
    "24u": "192px",  # 24 units
}

# Alternative t-shirt sizing (maps to units)
SPACING_TSHIRT = {
    "xs": SPACING["0.5u"],
    "sm": SPACING["1u"],
    "md": SPACING["2u"],
    "lg": SPACING["3u"],
    "xl": SPACING["4u"],
    "2xl": SPACING["6u"],
    "3xl": SPACING["8u"],
    "4xl": SPACING["12u"],
}


# ============================================================================
# LAYOUT DIMENSIONS
# ============================================================================

MARGINS = {
    "page": SPACING["4u"],
    "section": SPACING["6u"],
    "container": SPACING["2u"],
}

PADDING = {
    "tight": SPACING["1u"],
    "normal": SPACING["2u"],
    "relaxed": SPACING["3u"],
    "loose": SPACING["4u"],
}

GAPS = {
    "tight": SPACING["1u"],
    "normal": SPACING["2u"],
    "relaxed": SPACING["3u"],
    "loose": SPACING["4u"],
}


# ============================================================================
# BORDER RADIUS
# ============================================================================

RADIUS = {
    "none": "0",
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "16px",
    "2xl": "24px",
    "full": "9999px",
}


# ============================================================================
# BORDER WIDTH
# ============================================================================

BORDER_WIDTH = {
    "none": "0",
    "thin": "1px",
    "medium": "2px",
    "thick": "4px",
}


# ============================================================================
# SAFE AREAS (Platform-specific)
# ============================================================================

SAFE_AREAS = {
    "youtube_shorts": SafeArea(
        top=100,
        bottom=180,
        left=40,
        right=40,
        description="YouTube Shorts safe area avoiding UI overlays",
        aspect_ratio="9:16",
        usage="Vertical video for YouTube Shorts",
    ),
    "tiktok": SafeArea(
        top=120,
        bottom=200,
        left=40,
        right=40,
        description="TikTok safe area avoiding UI elements",
        aspect_ratio="9:16",
        usage="Vertical video for TikTok",
    ),
    "instagram_story": SafeArea(
        top=100,
        bottom=220,
        left=40,
        right=40,
        description="Instagram Stories safe area",
        aspect_ratio="9:16",
        usage="Vertical video for Instagram Stories",
    ),
    "instagram_reel": SafeArea(
        top=100,
        bottom=200,
        left=40,
        right=40,
        description="Instagram Reels safe area",
        aspect_ratio="9:16",
        usage="Vertical video for Instagram Reels",
    ),
    "youtube_landscape": SafeArea(
        top=60,
        bottom=60,
        left=80,
        right=80,
        description="YouTube landscape video safe area",
        aspect_ratio="16:9",
        usage="Horizontal video for YouTube",
    ),
    "presentation": SafeArea(
        top=40,
        bottom=40,
        left=60,
        right=60,
        description="PowerPoint/Keynote presentation safe area",
        aspect_ratio="16:9",
        usage="Presentation slides",
    ),
    "none": SafeArea(
        top=0,
        bottom=0,
        left=0,
        right=0,
        description="No safe area restrictions",
        aspect_ratio="any",
        usage="Full bleed content",
    ),
}


# ============================================================================
# GRID SYSTEMS
# ============================================================================

GRID = {
    "12_column": GridConfig(
        columns=12,
        gap=SPACING["2u"],
        margin=SPACING["4u"],
    ),
    "8_column": GridConfig(
        columns=8,
        gap=SPACING["2u"],
        margin=SPACING["3u"],
    ),
    "4_column": GridConfig(
        columns=4,
        gap=SPACING["2u"],
        margin=SPACING["2u"],
    ),
}


# ============================================================================
# CONTAINER WIDTHS
# ============================================================================

CONTAINERS = {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px",
    "full": "100%",
}


# ============================================================================
# ASPECT RATIOS
# ============================================================================

ASPECT_RATIOS = {
    "square": "1:1",
    "video": "16:9",
    "portrait": "9:16",
    "ultrawide": "21:9",
    "cinema": "2.39:1",
    "presentation": "4:3",
}


# ============================================================================
# Z-INDEX LAYERS
# ============================================================================

Z_INDEX = {
    "base": 0,
    "dropdown": 1000,
    "sticky": 1100,
    "overlay": 1200,
    "modal": 1300,
    "popover": 1400,
    "tooltip": 1500,
}


# ============================================================================
# SPACING TOKENS CLASS
# ============================================================================


class SpacingTokens:
    """Complete spacing token system."""

    def __init__(self) -> None:
        self.spacing = SPACING
        self.spacing_tshirt = SPACING_TSHIRT
        self.margins = MARGINS
        self.padding = PADDING
        self.gaps = GAPS
        self.radius = RADIUS
        self.border_width = BORDER_WIDTH
        self.safe_areas = SAFE_AREAS
        self.grid = GRID
        self.containers = CONTAINERS
        self.aspect_ratios = ASPECT_RATIOS
        self.z_index = Z_INDEX

    def get_safe_area(self, platform: str) -> SafeArea:
        """Get safe area configuration for platform."""
        if platform not in self.safe_areas:
            raise ValueError(f"Unknown platform: {platform}")
        return self.safe_areas[platform]

    def get_grid(self, columns: int = 12) -> GridConfig:
        """Get grid configuration."""
        key = f"{columns}_column"
        if key not in self.grid:
            raise ValueError(f"Unknown grid: {key}")
        return self.grid[key]

    def get_all(self) -> dict[str, Any]:
        """Get all spacing tokens as dictionary."""
        return {
            "spacing": self.spacing,
            "spacingTshirt": self.spacing_tshirt,
            "margins": self.margins,
            "padding": self.padding,
            "gaps": self.gaps,
            "radius": self.radius,
            "borderWidth": self.border_width,
            "safeAreas": {k: v.model_dump() for k, v in self.safe_areas.items()},
            "grid": {k: v.model_dump() for k, v in self.grid.items()},
            "containers": self.containers,
            "aspectRatios": self.aspect_ratios,
            "zIndex": self.z_index,
        }
