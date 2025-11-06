"""
Base Pydantic models for design tokens.

These models provide type safety and validation for all design tokens.
"""

from typing import Any, Literal
from pydantic import BaseModel, Field


# ============================================================================
# COLOR MODELS
# ============================================================================


class ColorScale(BaseModel):
    """A color scale from 50 (lightest) to 950 (darkest)."""

    scale_50: str = Field(..., alias="50")
    scale_100: str = Field(..., alias="100")
    scale_200: str = Field(..., alias="200")
    scale_300: str = Field(..., alias="300")
    scale_400: str = Field(..., alias="400")
    scale_500: str = Field(..., alias="500")
    scale_600: str = Field(..., alias="600")
    scale_700: str = Field(..., alias="700")
    scale_800: str = Field(..., alias="800")
    scale_900: str = Field(..., alias="900")
    scale_950: str = Field(..., alias="950")

    class Config:
        populate_by_name = True


class SemanticColorGroup(BaseModel):
    """A group of semantic colors (e.g., primary, secondary)."""

    DEFAULT: str
    foreground: str
    hover: str | None = None
    active: str | None = None


class SemanticColors(BaseModel):
    """Complete semantic color system."""

    # Backgrounds
    background: SemanticColorGroup
    foreground: SemanticColorGroup

    # Action colors
    primary: SemanticColorGroup
    secondary: SemanticColorGroup
    accent: SemanticColorGroup

    # UI elements
    muted: SemanticColorGroup
    card: SemanticColorGroup
    border: dict[str, str]

    # Status colors
    destructive: SemanticColorGroup
    success: SemanticColorGroup
    warning: SemanticColorGroup
    info: SemanticColorGroup

    # Chart colors
    chart: list[str]


# ============================================================================
# TYPOGRAPHY MODELS
# ============================================================================


class FontFamily(BaseModel):
    """Font family definition."""

    name: str
    fonts: list[str]
    description: str
    usage: str


class FontSizeScale(BaseModel):
    """Font size scale."""

    xs: str
    sm: str
    base: str
    lg: str
    xl: str
    xxl: str = Field(alias="2xl")
    xxxl: str = Field(alias="3xl")
    xxxxl: str = Field(alias="4xl")

    class Config:
        populate_by_name = True


class TextStyle(BaseModel):
    """Text style preset combining font properties."""

    name: str
    fontSize: str
    fontWeight: str
    lineHeight: str
    letterSpacing: str
    fontFamily: str


# ============================================================================
# SPACING MODELS
# ============================================================================


class SafeArea(BaseModel):
    """Safe area configuration for platform-specific layouts."""

    top: int
    bottom: int
    left: int
    right: int
    description: str
    aspect_ratio: str
    usage: str | None = None


class GridConfig(BaseModel):
    """Grid system configuration."""

    columns: int
    gap: str
    margin: str


# ============================================================================
# MOTION MODELS
# ============================================================================


class DurationConfig(BaseModel):
    """Duration configuration with multiple time representations."""

    ms: int
    frames_30fps: int
    frames_60fps: int
    seconds: float
    css: str
    description: str


class EasingConfig(BaseModel):
    """Easing curve configuration."""

    curve: list[float] = Field(..., description="Cubic bezier [x1, y1, x2, y2]")
    css: str
    description: str
    usage: str


class SpringConfig(BaseModel):
    """Spring animation configuration (Remotion-compatible)."""

    damping: float
    mass: float
    stiffness: float
    overshootClamping: bool
    description: str
    feel: str
    usage: str


class TransitionConfig(BaseModel):
    """Transition configuration."""

    properties: dict[str, Any]
    description: str
    usage: str
    default_duration: str
    default_easing: str


# ============================================================================
# THEME MODELS
# ============================================================================


class ThemeMetadata(BaseModel):
    """Theme metadata."""

    name: str
    description: str
    category: Literal["tech", "finance", "education", "lifestyle", "gaming", "business", "minimal"]
    tags: list[str] = Field(default_factory=list)


class Theme(BaseModel):
    """Complete theme combining all token categories."""

    metadata: ThemeMetadata
    colors: dict[str, Any]
    typography: dict[str, Any]
    spacing: dict[str, Any]
    motion: dict[str, Any] | None = None
