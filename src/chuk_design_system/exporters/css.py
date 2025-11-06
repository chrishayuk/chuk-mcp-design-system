"""
Standard CSS variables exporter.

Exports design tokens as standard CSS custom properties.
"""

from typing import Any


def export_to_css(theme: dict[str, Any], prefix: str = "ds") -> str:
    """
    Export theme to standard CSS variables.

    Args:
        theme: Complete theme dictionary from get_theme()
        prefix: CSS variable prefix (default: "ds" for design-system)

    Returns:
        CSS string with custom properties
    """
    lines = [
        "/**",
        f" * {theme['metadata']['name']} Theme",
        f" * {theme['metadata']['description']}",
        " */",
        "",
        ":root {",
    ]

    # Color variables
    if "colors" in theme and "semantic" in theme["colors"]:
        lines.append("  /* Colors */")
        semantic = theme["colors"]["semantic"]

        for category, values in semantic.items():
            if isinstance(values, dict):
                for key, value in values.items():
                    var_name = (
                        f"{prefix}-color-{category}-{key}"
                        if key != "DEFAULT"
                        else f"{prefix}-color-{category}"
                    )
                    lines.append(f"  --{var_name}: {value};")
            elif isinstance(values, list):
                # Handle chart colors
                for i, color in enumerate(values):
                    lines.append(f"  --{prefix}-color-{category}-{i + 1}: {color};")

        lines.append("")

    # Spacing variables
    if "spacing" in theme and "spacing" in theme["spacing"]:
        lines.append("  /* Spacing */")
        spacing = theme["spacing"]["spacing"]

        for key, value in spacing.items():
            # Normalize key (remove 'u', replace dots)
            normalized_key = key.replace("u", "").replace(".", "-")
            lines.append(f"  --{prefix}-space-{normalized_key}: {value};")

        lines.append("")

    # Typography variables
    if "typography" in theme:
        lines.append("  /* Typography */")

        if "sizes" in theme["typography"]:
            sizes = theme["typography"]["sizes"]
            for key, value in sizes.items():
                lines.append(f"  --{prefix}-font-size-{key}: {value};")

        if "weights" in theme["typography"]:
            weights = theme["typography"]["weights"]
            for key, value in weights.items():
                lines.append(f"  --{prefix}-font-weight-{key}: {value};")

        if "lineHeights" in theme["typography"]:
            line_heights = theme["typography"]["lineHeights"]
            for key, value in line_heights.items():
                lines.append(f"  --{prefix}-line-height-{key}: {value};")

        lines.append("")

    # Border radius
    if "spacing" in theme and "radius" in theme["spacing"]:
        lines.append("  /* Border Radius */")
        radius = theme["spacing"]["radius"]

        for key, value in radius.items():
            lines.append(f"  --{prefix}-radius-{key}: {value};")

        lines.append("")

    # Motion variables
    if "motion" in theme and "durations" in theme["motion"]:
        lines.append("  /* Durations */")
        durations = theme["motion"]["durations"]

        for key, value in durations.items():
            if "css" in value:
                lines.append(f"  --{prefix}-duration-{key}: {value['css']};")

        lines.append("")

    if "motion" in theme and "easings" in theme["motion"]:
        lines.append("  /* Easings */")
        easings = theme["motion"]["easings"]

        for key, value in easings.items():
            if "css" in value:
                lines.append(f"  --{prefix}-easing-{key}: {value['css']};")

        lines.append("")

    lines.append("}")
    return "\n".join(lines)


def export_utility_classes(theme: dict[str, Any], prefix: str = "ds") -> str:
    """
    Export utility CSS classes based on tokens.

    Args:
        theme: Complete theme dictionary
        prefix: Class prefix

    Returns:
        CSS string with utility classes
    """
    lines = []

    # Spacing utilities
    if "spacing" in theme and "spacing" in theme["spacing"]:
        lines.append("/* Spacing Utilities */")
        spacing = theme["spacing"]["spacing"]

        for key, value in spacing.items():
            normalized_key = key.replace("u", "").replace(".", "-")
            # Margin utilities
            lines.append(f".{prefix}-m-{normalized_key} {{ margin: {value}; }}")
            lines.append(f".{prefix}-mt-{normalized_key} {{ margin-top: {value}; }}")
            lines.append(f".{prefix}-mb-{normalized_key} {{ margin-bottom: {value}; }}")
            lines.append(f".{prefix}-ml-{normalized_key} {{ margin-left: {value}; }}")
            lines.append(f".{prefix}-mr-{normalized_key} {{ margin-right: {value}; }}")

            # Padding utilities
            lines.append(f".{prefix}-p-{normalized_key} {{ padding: {value}; }}")
            lines.append(f".{prefix}-pt-{normalized_key} {{ padding-top: {value}; }}")
            lines.append(f".{prefix}-pb-{normalized_key} {{ padding-bottom: {value}; }}")
            lines.append(f".{prefix}-pl-{normalized_key} {{ padding-left: {value}; }}")
            lines.append(f".{prefix}-pr-{normalized_key} {{ padding-right: {value}; }}")

        lines.append("")

    return "\n".join(lines)
