"""
Complete Design System Showcase

Interactive demonstration of the entire chuk-design-system.
Shows all features and capabilities in one comprehensive demo.
"""

import sys
from chuk_design_system.themes import list_themes, get_theme
from chuk_design_system.tokens import get_all_tokens


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def showcase_overview():
    """Show system overview."""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "   🎨 CHUK DESIGN SYSTEM - COMPLETE SHOWCASE   ".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")

    print_header("SYSTEM OVERVIEW")
    print("A universal design system with:")
    print("  ✅ Multi-format token export (Canva, Remotion, PPTX, CSS, W3C JSON)")
    print("  ✅ 7 pre-built themes")
    print("  ✅ Type-safe Pydantic models")
    print("  ✅ 90%+ test coverage")
    print("  ✅ MCP server for Claude integration")


def showcase_themes():
    """Show all available themes."""
    print_header("AVAILABLE THEMES")

    themes = list_themes()
    for i, theme in enumerate(themes, 1):
        print(f"{i}. {theme['name']} ({theme['key']})")
        print(f"   {theme['description']}")
        print(f"   Tags: {theme['tags']}\n")


def showcase_theme_details(theme_name="tech"):
    """Show detailed theme information."""
    print_header(f"THEME DETAILS: {theme_name.upper()}")

    theme = get_theme(theme_name)
    metadata = theme["metadata"]

    print(f"Name: {metadata['name']}")
    print(f"Description: {metadata['description']}")
    print(f"Category: {metadata['category']}")

    # Show key colors
    colors = theme["colors"]["semantic"]
    print("\nKey Colors:")
    print(f"  Primary:    {colors['primary']['DEFAULT']}")
    print(f"  Accent:     {colors['accent']['DEFAULT']}")
    print(f"  Background: {colors['background']['DEFAULT']}")
    print(f"  Foreground: {colors['foreground']['DEFAULT']}")

    # Show typography
    typography = theme["typography"]
    print("\nTypography:")
    print(f"  Base size: {typography['sizes']['base']}")
    print(f"  Scale: xs, sm, base, lg, xl, 2xl, 3xl, 4xl")

    # Show spacing
    spacing = theme["spacing"]
    print("\nSpacing (8px base unit):")
    print(f"  1u = {spacing['spacing']['1u']}")
    print(f"  2u = {spacing['spacing']['2u']}")

    # Show motion defaults
    motion = theme["motion"]
    if "defaults" in motion:
        defaults = motion["defaults"]
        print("\nMotion Defaults:")
        print(f"  Duration: {defaults['duration']}")
        print(f"  Easing: {defaults['easing']}")
        print(f"  Spring: {defaults['spring']}")


def showcase_token_categories():
    """Show token category structure."""
    print_header("TOKEN CATEGORIES")

    tokens = get_all_tokens()

    print("🎨 Colors:")
    print(f"   - {len(tokens['colors']['palette'])} color hues (50-950 scales)")
    print(f"   - Semantic tokens (primary, secondary, accent, etc.)")
    print(f"   - {len(tokens['colors']['gradients'])} gradient presets")

    print("\n📝 Typography:")
    print("   - 4 font families (display, body, mono, decorative)")
    print("   - 4 medium scales (web, pptx, video_1080p, video_4k)")
    print("   - 7 text style presets")

    print("\n📏 Spacing:")
    print("   - 8px base unit system (Canva-compatible)")
    print(f"   - {len(tokens['spacing']['safeAreas'])} platform safe areas")
    print("   - Grid systems (4, 8, 12 column)")

    print("\n⚡ Motion:")
    print(f"   - {len(tokens['motion']['durations'])} duration tokens")
    print(f"   - {len(tokens['motion']['easings'])} easing curves")
    print(f"   - {len(tokens['motion']['springs'])} spring configs")
    print("   - Enter/exit transition presets")


def showcase_export_formats():
    """Show export format capabilities."""
    print_header("EXPORT FORMATS")

    formats = [
        ("Canva CSS", "CSS variables for Canva app development", "--content-*"),
        ("Remotion TS", "TypeScript constants for Remotion videos", "export const"),
        ("Standard CSS", "Custom CSS properties", "--ds-*"),
        ("W3C JSON", "Design Tokens spec for interoperability", '{"$type": "color"}'),
        ("python-pptx", "RGBColor/Pt/EMU for PowerPoint", "RGBColor(r, g, b)"),
    ]

    for name, description, example in formats:
        print(f"📦 {name}")
        print(f"   {description}")
        print(f"   Example: {example}")
        print()


def showcase_use_cases():
    """Show practical use cases."""
    print_header("USE CASES")

    use_cases = [
        (
            "chuk-mcp-remotion",
            "Video Generation",
            "Export to Remotion TS → Generate videos with consistent branding",
        ),
        (
            "chuk-mcp-pptx",
            "Presentation Generation",
            "Export to python-pptx → Create branded PowerPoint decks",
        ),
        (
            "Canva Apps",
            "App Development",
            "Export to Canva CSS → Build apps matching Canva's UI",
        ),
        (
            "Web Projects",
            "Website Theming",
            "Export to CSS → Style websites with design system",
        ),
        (
            "LinkedIn Carousels",
            "Social Media",
            "Use tokens → Generate consistent LinkedIn content",
        ),
    ]

    for project, category, workflow in use_cases:
        print(f"• {project} ({category})")
        print(f"  {workflow}")
        print()


def show_quick_start():
    """Show quick start code examples."""
    print_header("QUICK START")

    print("Python API:")
    print(
        """
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters import export_to_canva_css

# Get a theme
theme = get_theme("tech")

# Export to Canva
css = export_to_canva_css(theme)
print(css)
"""
    )

    print("\nMakefile:")
    print(
        """
make test-cov      # Run tests with coverage
make example       # Run usage examples
make format        # Format code
make all          # Run all checks
"""
    )


def interactive_demo():
    """Run interactive demo if requested."""
    print_header("INTERACTIVE DEMO")
    print("Would you like to see specific showcases?")
    print()
    print("Available demos:")
    print("  1. Colors (python examples/showcase_colors.py)")
    print("  2. Typography (python examples/showcase_typography.py)")
    print("  3. Spacing (python examples/showcase_spacing.py)")
    print("  4. Motion (python examples/showcase_motion.py)")
    print()


def main():
    """Run complete showcase."""
    showcase_overview()
    showcase_themes()
    showcase_theme_details("tech")
    showcase_token_categories()
    showcase_export_formats()
    showcase_use_cases()
    show_quick_start()
    interactive_demo()

    print("=" * 70)
    print("✅ Design System Showcase Complete!")
    print("=" * 70)
    print("\nNext steps:")
    print("  • Run: make test-cov")
    print("  • View: README.md and USAGE.md")
    print("  • Try: Individual showcases (showcase_*.py)")
    print("  • Export: make export-examples")
    print()


if __name__ == "__main__":
    main()
