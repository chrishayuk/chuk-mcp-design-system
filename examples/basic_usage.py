"""
Basic usage examples for chuk-design-system.

Demonstrates how to use themes, tokens, and exporters.
"""

from chuk_design_system.themes import list_themes, get_theme
from chuk_design_system.tokens import get_all_tokens, ColorTokens, TypographyTokens
from chuk_design_system.exporters import (
    export_to_canva_css,
    export_to_css,
    export_to_remotion_ts,
    export_to_w3c_json,
)


def example_list_themes():
    """List all available themes."""
    print("=== Available Themes ===\n")
    themes = list_themes()
    for theme in themes:
        print(f"{theme['name']} ({theme['key']})")
        print(f"  {theme['description']}")
        print(f"  Tags: {theme['tags']}")
        print()


def example_get_theme():
    """Get a complete theme with all tokens."""
    print("=== Tech Theme ===\n")
    theme = get_theme("tech")
    print(f"Name: {theme['metadata']['name']}")
    print(f"Description: {theme['metadata']['description']}")
    print(f"\nPrimary Color: {theme['colors']['semantic']['primary']['DEFAULT']}")
    print(f"Background: {theme['colors']['semantic']['background']['DEFAULT']}")
    print()


def example_tokens_only():
    """Access tokens directly without a theme."""
    print("=== Direct Token Access ===\n")

    # Get color tokens
    colors = ColorTokens()
    print(f"Blue 500: {colors.palette['blue'][500]}")
    print(f"Green 600: {colors.palette['green'][600]}")

    # Get semantic colors
    semantic = colors.get_semantic("purple", "dark")
    print(f"Purple primary: {semantic.primary.DEFAULT}")

    print()

    # Get typography tokens
    typography = TypographyTokens()
    print(f"Font sizes (web): {typography.sizes['web'].base}")
    print(f"Font sizes (video 1080p): {typography.sizes['video_1080p'].base}")
    print()


def example_export_canva():
    """Export theme to Canva CSS variables."""
    print("=== Export to Canva CSS ===\n")
    theme = get_theme("tech")
    css = export_to_canva_css(theme)
    print(css[:500] + "...")  # Print first 500 chars
    print()


def example_export_remotion():
    """Export theme to Remotion TypeScript."""
    print("=== Export to Remotion TypeScript ===\n")
    theme = get_theme("finance")
    ts = export_to_remotion_ts(theme)
    print(ts[:500] + "...")  # Print first 500 chars
    print()


def example_export_standard_css():
    """Export theme to standard CSS."""
    print("=== Export to Standard CSS ===\n")
    theme = get_theme("education")
    css = export_to_css(theme, prefix="edu")
    print(css[:500] + "...")  # Print first 500 chars
    print()


def example_export_w3c_json():
    """Export theme to W3C Design Tokens JSON."""
    print("=== Export to W3C JSON ===\n")
    theme = get_theme("minimal")
    json_output = export_to_w3c_json(theme)
    print(json_output[:500] + "...")  # Print first 500 chars
    print()


def example_multi_format_export():
    """Export the same theme to multiple formats."""
    print("=== Multi-Format Export (Gaming Theme) ===\n")
    theme = get_theme("gaming")

    formats = {
        "Canva CSS": export_to_canva_css(theme),
        "Remotion TS": export_to_remotion_ts(theme),
        "Standard CSS": export_to_css(theme),
        "W3C JSON": export_to_w3c_json(theme),
    }

    for format_name, output in formats.items():
        print(f"{format_name}: {len(output)} characters")

    print()


if __name__ == "__main__":
    example_list_themes()
    example_get_theme()
    example_tokens_only()
    example_export_canva()
    example_export_remotion()
    example_export_standard_css()
    example_export_w3c_json()
    example_multi_format_export()

    print("✅ All examples completed successfully!")
