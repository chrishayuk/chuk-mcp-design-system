"""
PowerPoint (python-pptx) exporter.

Exports design tokens in formats compatible with python-pptx.
Optional dependency - only works if python-pptx is installed.
"""

from typing import Any


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore


def export_colors(theme: dict[str, Any]) -> dict[str, tuple[int, int, int]]:
    """
    Export colors as RGB tuples for python-pptx.

    Args:
        theme: Complete theme dictionary

    Returns:
        Dictionary mapping color names to RGB tuples
    """
    colors = {}

    if "colors" in theme and "semantic" in theme["colors"]:
        semantic = theme["colors"]["semantic"]

        for category, values in semantic.items():
            if isinstance(values, dict) and "DEFAULT" in values:
                hex_color = values["DEFAULT"]
                colors[category] = hex_to_rgb(hex_color)

                # Also export variants (skip None values)
                for variant in ["hover", "active", "foreground"]:
                    if variant in values and values[variant] is not None:
                        key = f"{category}_{variant}"
                        colors[key] = hex_to_rgb(values[variant])

    return colors


def export_colors_pptx(theme: dict[str, Any]) -> dict:
    """
    Export colors as python-pptx RGBColor objects.

    Requires python-pptx to be installed.

    Args:
        theme: Complete theme dictionary

    Returns:
        Dictionary with RGBColor objects
    """
    try:
        from pptx.util import RGBColor
    except ImportError:
        raise ImportError(
            "python-pptx is required for PPTX export. " "Install with: pip install python-pptx"
        )

    rgb_colors = export_colors(theme)
    return {name: RGBColor(*rgb) for name, rgb in rgb_colors.items()}


def export_font_sizes_pt(theme: dict[str, Any]) -> dict[str, float]:
    """
    Export font sizes in points for PowerPoint.

    Args:
        theme: Complete theme dictionary

    Returns:
        Dictionary mapping size names to point values
    """
    sizes = {}

    if "typography" in theme and "sizes" in theme["typography"]:
        # Check if we have PPTX-specific sizes
        size_values = theme["typography"]["sizes"]

        for key, value in size_values.items():
            # Convert to float, removing 'pt' if present
            if isinstance(value, str):
                if value.endswith("pt"):
                    sizes[key] = float(value[:-2])
                elif value.endswith("px"):
                    # Convert px to pt (1pt = 1.333px approximately)
                    sizes[key] = float(value[:-2]) * 0.75
                else:
                    sizes[key] = float(value)
            else:
                sizes[key] = float(value)

    return sizes


def export_spacing_emu(theme: dict[str, Any]) -> dict[str, int]:
    """
    Export spacing in EMUs (English Metric Units) for PowerPoint.

    1 inch = 914400 EMUs
    1 px ≈ 9525 EMUs (at 96 DPI)

    Args:
        theme: Complete theme dictionary

    Returns:
        Dictionary mapping spacing names to EMU values
    """
    spacing = {}

    if "spacing" in theme and "spacing" in theme["spacing"]:
        space_values = theme["spacing"]["spacing"]

        for key, value in space_values.items():
            # Convert px to EMU
            if isinstance(value, str) and value.endswith("px"):
                px_value = float(value[:-2])
                spacing[key] = int(px_value * 9525)

    return spacing


def create_pptx_theme_dict(theme: dict[str, Any]) -> dict[str, Any]:
    """
    Create a complete PPTX-compatible theme dictionary.

    Args:
        theme: Complete theme dictionary

    Returns:
        Dictionary with all PPTX-compatible token values
    """
    return {
        "colors_rgb": export_colors(theme),
        "font_sizes_pt": export_font_sizes_pt(theme),
        "spacing_emu": export_spacing_emu(theme),
        "metadata": theme.get("metadata", {}),
    }
