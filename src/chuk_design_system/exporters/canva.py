"""
Canva CSS variables exporter.

Exports design tokens as Canva-compatible CSS variables for use in Canva apps.
"""

from typing import Any


def export_to_canva_css(theme: dict[str, Any]) -> str:
    """
    Export theme to Canva-compatible CSS variables.

    Args:
        theme: Complete theme dictionary from get_theme()

    Returns:
        CSS string with --content-* variables
    """
    lines = [":root {"]

    # Color variables
    if "colors" in theme and "semantic" in theme["colors"]:
        semantic = theme["colors"]["semantic"]

        # Action colors
        if "primary" in semantic:
            lines.append(f"  --content-color-primary: {semantic['primary']['DEFAULT']};")
            lines.append(
                f"  --content-color-primary-foreground: {semantic['primary']['foreground']};"
            )

        if "secondary" in semantic:
            lines.append(f"  --content-color-secondary: {semantic['secondary']['DEFAULT']};")

        if "accent" in semantic:
            lines.append(f"  --content-color-tertiary: {semantic['accent']['DEFAULT']};")

        # Background colors
        if "background" in semantic:
            lines.append(f"  --content-color-bg: {semantic['background']['DEFAULT']};")

        # Typography colors
        if "foreground" in semantic:
            lines.append(
                f"  --content-color-typography-primary: {semantic['foreground']['DEFAULT']};"
            )
            if "hover" in semantic["foreground"]:
                lines.append(
                    f"  --content-color-typography-secondary: {semantic['foreground']['hover']};"
                )

        # Status colors
        if "success" in semantic:
            lines.append(f"  --content-color-success: {semantic['success']['DEFAULT']};")
        if "warning" in semantic:
            lines.append(f"  --content-color-warning: {semantic['warning']['DEFAULT']};")
        if "destructive" in semantic:
            lines.append(f"  --content-color-error: {semantic['destructive']['DEFAULT']};")

    # Spacing variables (convert to Canva's unit system)
    if "spacing" in theme and "spacing" in theme["spacing"]:
        spacing = theme["spacing"]["spacing"]
        lines.append("")
        lines.append("  /* Spacing (unit system: 1u = 8px) */")
        for key, value in spacing.items():
            css_key = key.replace("u", "")  # "1u" -> "1"
            lines.append(f"  --content-space-{css_key}: {value};")

    # Typography variables
    if "typography" in theme and "sizes" in theme["typography"]:
        sizes = theme["typography"]["sizes"]
        lines.append("")
        lines.append("  /* Typography */")

        # Map our semantic sizes to Canva naming
        size_map = {
            "xs": "small",
            "sm": "small",
            "base": "medium",
            "lg": "medium",
            "xl": "large",
            "2xl": "large",
            "3xl": "large",
            "4xl": "large",
        }

        for key, value in sizes.items():
            if key in size_map:
                canva_size = size_map[key]
                lines.append(f"  --content-typography-{canva_size}-{key}: {value};")

    # Font weights
    if "typography" in theme and "weights" in theme["typography"]:
        weights = theme["typography"]["weights"]
        lines.append("")
        lines.append("  /* Font weights */")
        for key, value in weights.items():
            lines.append(f"  --content-typography-weight-{key}: {value};")

    lines.append("}")
    return "\n".join(lines)


def export_colors_only(theme: dict[str, Any]) -> str:
    """Export only color tokens to Canva CSS."""
    lines = [":root {"]

    if "colors" in theme and "semantic" in theme["colors"]:
        semantic = theme["colors"]["semantic"]

        for category, values in semantic.items():
            if isinstance(values, dict) and "DEFAULT" in values:
                lines.append(f"  --content-color-{category}: {values['DEFAULT']};")

    lines.append("}")
    return "\n".join(lines)
