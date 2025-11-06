"""
W3C Design Tokens JSON exporter.

Exports design tokens following the W3C Design Tokens Community Group specification.
https://design-tokens.github.io/community-group/format/
"""

import json
from typing import Any


def export_to_w3c_json(theme: dict[str, Any], pretty: bool = True) -> str:
    """
    Export theme to W3C Design Tokens JSON format.

    Args:
        theme: Complete theme dictionary
        pretty: Pretty-print JSON (default: True)

    Returns:
        JSON string following W3C Design Tokens spec
    """
    tokens: dict[str, Any] = {}

    # Color tokens
    if "colors" in theme and "semantic" in theme["colors"]:
        tokens["color"] = {}
        semantic = theme["colors"]["semantic"]

        for category, values in semantic.items():
            if isinstance(values, dict):
                if "DEFAULT" in values:
                    tokens["color"][category] = {
                        "$type": "color",
                        "$value": values["DEFAULT"],
                        "$description": f"{category.capitalize()} color",
                    }

                # Add variants as separate tokens
                for variant, value in values.items():
                    if variant != "DEFAULT":
                        key = f"{category}-{variant}"
                        tokens["color"][key] = {
                            "$type": "color",
                            "$value": value,
                            "$description": f"{category.capitalize()} {variant} color",
                        }

    # Dimension tokens (spacing)
    if "spacing" in theme and "spacing" in theme["spacing"]:
        tokens["dimension"] = {}
        spacing = theme["spacing"]["spacing"]

        for key, value in spacing.items():
            tokens["dimension"][f"space-{key}"] = {
                "$type": "dimension",
                "$value": value,
            }

    # Typography tokens
    if "typography" in theme:
        # Font sizes
        if "sizes" in theme["typography"]:
            if "fontSize" not in tokens:
                tokens["fontSize"] = {}

            sizes = theme["typography"]["sizes"]
            for key, value in sizes.items():
                tokens["fontSize"][key] = {
                    "$type": "dimension",
                    "$value": value,
                }

        # Font weights
        if "weights" in theme["typography"]:
            tokens["fontWeight"] = {}
            weights = theme["typography"]["weights"]

            for key, value in weights.items():
                tokens["fontWeight"][key] = {
                    "$type": "number",
                    "$value": value,
                }

    # Duration tokens
    if "motion" in theme and "durations" in theme["motion"]:
        tokens["duration"] = {}
        durations = theme["motion"]["durations"]

        for key, value in durations.items():
            if "css" in value:
                tokens["duration"][key] = {
                    "$type": "duration",
                    "$value": value["css"],
                    "$description": value.get("description", ""),
                }

    # Cubic bezier tokens (easings)
    if "motion" in theme and "easings" in theme["motion"]:
        tokens["cubicBezier"] = {}
        easings = theme["motion"]["easings"]

        for key, value in easings.items():
            if "curve" in value:
                tokens["cubicBezier"][key] = {
                    "$type": "cubicBezier",
                    "$value": value["curve"],
                    "$description": value.get("description", ""),
                }

    indent = 2 if pretty else None
    return json.dumps(tokens, indent=indent)


def export_tokens_minimal(theme: dict[str, Any]) -> str:
    """
    Export minimal token set (colors and spacing only).

    Args:
        theme: Complete theme dictionary

    Returns:
        Minimal JSON string
    """
    tokens: dict[str, Any] = {"color": {}, "dimension": {}}

    # Only export primary semantic colors
    if "colors" in theme and "semantic" in theme["colors"]:
        semantic = theme["colors"]["semantic"]
        for category in ["primary", "secondary", "background", "foreground"]:
            if category in semantic and "DEFAULT" in semantic[category]:
                tokens["color"][category] = {
                    "$type": "color",
                    "$value": semantic[category]["DEFAULT"],
                }

    # Only export main spacing values
    if "spacing" in theme and "spacingTshirt" in theme["spacing"]:
        spacing = theme["spacing"]["spacingTshirt"]
        for key, value in spacing.items():
            tokens["dimension"][f"space-{key}"] = {"$type": "dimension", "$value": value}

    return json.dumps(tokens, indent=2)
