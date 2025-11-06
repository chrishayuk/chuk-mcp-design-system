"""
Color tokens - Universal color system.

Combines:
- Tailwind-style color palettes (50-950 scales) from chuk-mcp-pptx
- Theme-specific color schemes from chuk-mcp-remotion
- Semantic color roles (Canva-compatible)
"""

from typing import Any
from chuk_design_system.tokens.models import SemanticColors, SemanticColorGroup


# ============================================================================
# BASE COLOR PALETTE (Tailwind-inspired)
# ============================================================================

PALETTE: dict[str, dict[int, str]] = {
    # Neutrals
    "slate": {
        50: "#f8fafc",
        100: "#f1f5f9",
        200: "#e2e8f0",
        300: "#cbd5e1",
        400: "#94a3b8",
        500: "#64748b",
        600: "#475569",
        700: "#334155",
        800: "#1e293b",
        900: "#0f172a",
        950: "#020617",
    },
    "zinc": {
        50: "#fafafa",
        100: "#f4f4f5",
        200: "#e4e4e7",
        300: "#d4d4d8",
        400: "#a1a1aa",
        500: "#71717a",
        600: "#52525b",
        700: "#3f3f46",
        800: "#27272a",
        900: "#18181b",
        950: "#09090b",
    },
    # Primary colors
    "blue": {
        50: "#eff6ff",
        100: "#dbeafe",
        200: "#bfdbfe",
        300: "#93c5fd",
        400: "#60a5fa",
        500: "#3b82f6",
        600: "#2563eb",
        700: "#1d4ed8",
        800: "#1e40af",
        900: "#1e3a8a",
        950: "#172554",
    },
    "cyan": {
        50: "#ecfeff",
        100: "#cffafe",
        200: "#a5f3fc",
        300: "#67e8f9",
        400: "#22d3ee",
        500: "#06b6d4",
        600: "#0891b2",
        700: "#0e7490",
        800: "#155e75",
        900: "#164e63",
        950: "#083344",
    },
    "green": {
        50: "#f0fdf4",
        100: "#dcfce7",
        200: "#bbf7d0",
        300: "#86efac",
        400: "#4ade80",
        500: "#22c55e",
        600: "#16a34a",
        700: "#15803d",
        800: "#166534",
        900: "#14532d",
        950: "#052e16",
    },
    "purple": {
        50: "#faf5ff",
        100: "#f3e8ff",
        200: "#e9d5ff",
        300: "#d8b4fe",
        400: "#c084fc",
        500: "#a855f7",
        600: "#9333ea",
        700: "#7e22ce",
        800: "#6b21a8",
        900: "#581c87",
        950: "#3b0764",
    },
    "pink": {
        50: "#fdf2f8",
        100: "#fce7f3",
        200: "#fbcfe8",
        300: "#f9a8d4",
        400: "#f472b6",
        500: "#ec4899",
        600: "#db2777",
        700: "#be185d",
        800: "#9f1239",
        900: "#831843",
        950: "#500724",
    },
    "orange": {
        50: "#fff7ed",
        100: "#ffedd5",
        200: "#fed7aa",
        300: "#fdba74",
        400: "#fb923c",
        500: "#f97316",
        600: "#ea580c",
        700: "#c2410c",
        800: "#9a3412",
        900: "#7c2d12",
        950: "#431407",
    },
    "yellow": {
        50: "#fefce8",
        100: "#fef9c3",
        200: "#fef08a",
        300: "#fde047",
        400: "#facc15",
        500: "#eab308",
        600: "#ca8a04",
        700: "#a16207",
        800: "#854d0e",
        900: "#713f12",
        950: "#422006",
    },
    "red": {
        50: "#fef2f2",
        100: "#fee2e2",
        200: "#fecaca",
        300: "#fca5a5",
        400: "#f87171",
        500: "#ef4444",
        600: "#dc2626",
        700: "#b91c1c",
        800: "#991b1b",
        900: "#7f1d1d",
        950: "#450a0a",
    },
    "indigo": {
        50: "#eef2ff",
        100: "#e0e7ff",
        200: "#c7d2fe",
        300: "#a5b4fc",
        400: "#818cf8",
        500: "#6366f1",
        600: "#4f46e5",
        700: "#4338ca",
        800: "#3730a3",
        900: "#312e81",
        950: "#1e1b4b",
    },
    "violet": {
        50: "#f5f3ff",
        100: "#ede9fe",
        200: "#ddd6fe",
        300: "#c4b5fd",
        400: "#a78bfa",
        500: "#8b5cf6",
        600: "#7c3aed",
        700: "#6d28d9",
        800: "#5b21b6",
        900: "#4c1d95",
        950: "#2e1065",
    },
    "emerald": {
        50: "#ecfdf5",
        100: "#d1fae5",
        200: "#a7f3d0",
        300: "#6ee7b7",
        400: "#34d399",
        500: "#10b981",
        600: "#059669",
        700: "#047857",
        800: "#065f46",
        900: "#064e3b",
        950: "#022c22",
    },
    "amber": {
        50: "#fffbeb",
        100: "#fef3c7",
        200: "#fde68a",
        300: "#fcd34d",
        400: "#fbbf24",
        500: "#f59e0b",
        600: "#d97706",
        700: "#b45309",
        800: "#92400e",
        900: "#78350f",
        950: "#451a03",
    },
}


# ============================================================================
# GRADIENTS
# ============================================================================

GRADIENTS = {
    "sunset": "linear-gradient(135deg, #ff6b6b 0%, #f7b731 50%, #5f27cd 100%)",
    "ocean": "linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)",
    "forest": "linear-gradient(135deg, #00b09b 0%, #96c93d 50%, #ffe000 100%)",
    "flame": "linear-gradient(135deg, #ff416c 0%, #ff4b2b 50%, #ffc837 100%)",
    "aurora": "linear-gradient(135deg, #00c9ff 0%, #92fe9d 50%, #fc00ff 100%)",
    "cosmic": "linear-gradient(135deg, #7303c0 0%, #ec38bc 50%, #03001e 100%)",
    "tech": "linear-gradient(135deg, #0066FF 0%, #00D9FF 100%)",
    "finance": "linear-gradient(135deg, #00C853 0%, #FFD600 100%)",
    "education": "linear-gradient(135deg, #7C4DFF 0%, #FF6E40 100%)",
    "lifestyle": "linear-gradient(135deg, #FF6B9D 0%, #FFB74D 100%)",
    "gaming": "linear-gradient(135deg, #00E676 0%, #E040FB 100%)",
    "business": "linear-gradient(135deg, #1565C0 0%, #00ACC1 100%)",
}


# ============================================================================
# SEMANTIC TOKEN GENERATOR
# ============================================================================


def get_semantic_colors(primary_hue: str = "blue", mode: str = "dark") -> SemanticColors:
    """
    Generate semantic color tokens based on primary hue and mode.

    Canva-compatible semantic naming with action/typography/background roles.

    Args:
        primary_hue: Primary color from palette (e.g., "blue", "violet")
        mode: "dark" or "light"

    Returns:
        SemanticColors model with all semantic tokens
    """
    is_dark = mode == "dark"

    return SemanticColors(
        # Background tokens
        background=SemanticColorGroup(
            DEFAULT=PALETTE["zinc"][950] if is_dark else "#ffffff",
            foreground=PALETTE["zinc"][50] if is_dark else PALETTE["zinc"][900],
            hover=PALETTE["zinc"][900] if is_dark else PALETTE["zinc"][50],
            active=PALETTE["zinc"][800] if is_dark else PALETTE["zinc"][100],
        ),
        # Foreground tokens
        foreground=SemanticColorGroup(
            DEFAULT=PALETTE["zinc"][50] if is_dark else PALETTE["zinc"][900],
            foreground=PALETTE["zinc"][900] if is_dark else PALETTE["zinc"][50],
            hover=PALETTE["zinc"][200] if is_dark else PALETTE["zinc"][700],
            active=PALETTE["zinc"][100] if is_dark else PALETTE["zinc"][800],
        ),
        # Primary action colors
        primary=SemanticColorGroup(
            DEFAULT=PALETTE[primary_hue][500 if is_dark else 600],
            foreground="#ffffff",
            hover=PALETTE[primary_hue][400 if is_dark else 700],
            active=PALETTE[primary_hue][300 if is_dark else 800],
        ),
        # Secondary action colors
        secondary=SemanticColorGroup(
            DEFAULT=PALETTE["zinc"][800 if is_dark else 200],
            foreground=PALETTE["zinc"][50 if is_dark else 900],
            hover=PALETTE["zinc"][700 if is_dark else 300],
            active=PALETTE["zinc"][600 if is_dark else 400],
        ),
        # Accent colors
        accent=SemanticColorGroup(
            DEFAULT=PALETTE[primary_hue][400 if is_dark else 500],
            foreground=PALETTE["zinc"][950] if is_dark else "#ffffff",
            hover=PALETTE[primary_hue][300 if is_dark else 600],
            active=PALETTE[primary_hue][200 if is_dark else 700],
        ),
        # Muted colors
        muted=SemanticColorGroup(
            DEFAULT=PALETTE["zinc"][800 if is_dark else 100],
            foreground=PALETTE["zinc"][400 if is_dark else 600],
        ),
        # Card colors
        card=SemanticColorGroup(
            DEFAULT=PALETTE["zinc"][900 if is_dark else 50],
            foreground=PALETTE["zinc"][50 if is_dark else 900],
            hover=PALETTE["zinc"][800 if is_dark else 100],
        ),
        # Border colors
        border={
            "DEFAULT": PALETTE["zinc"][800 if is_dark else 200],
            "secondary": PALETTE["zinc"][700 if is_dark else 300],
        },
        # Status colors
        destructive=SemanticColorGroup(
            DEFAULT=PALETTE["red"][600 if is_dark else 500],
            foreground="#ffffff",
        ),
        success=SemanticColorGroup(
            DEFAULT=PALETTE["green"][600 if is_dark else 500],
            foreground="#ffffff",
        ),
        warning=SemanticColorGroup(
            DEFAULT=PALETTE["amber"][600 if is_dark else 500],
            foreground=PALETTE["zinc"][950],
        ),
        info=SemanticColorGroup(
            DEFAULT=PALETTE["blue"][600 if is_dark else 500],
            foreground="#ffffff",
        ),
        # Chart colors (for data visualization)
        chart=[
            PALETTE[primary_hue][500],
            PALETTE["cyan"][500],
            PALETTE["violet"][500],
            PALETTE["emerald"][500],
            PALETTE["orange"][500],
            PALETTE["pink"][500],
            PALETTE["yellow"][500],
            PALETTE["indigo"][500],
        ],
    )


# ============================================================================
# COLOR TOKENS CLASS
# ============================================================================


class ColorTokens:
    """Complete color token system."""

    def __init__(self) -> None:
        self.palette = PALETTE
        self.gradients = GRADIENTS

    def get_semantic(self, primary_hue: str = "blue", mode: str = "dark") -> SemanticColors:
        """Get semantic color tokens."""
        return get_semantic_colors(primary_hue, mode)

    def get_all(self, primary_hue: str = "blue", mode: str = "dark") -> dict[str, Any]:
        """Get all color tokens as dictionary."""
        return {
            "palette": self.palette,
            "semantic": self.get_semantic(primary_hue, mode).model_dump(),
            "gradients": self.gradients,
        }
