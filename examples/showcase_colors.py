"""
Color System Showcase

Demonstrates all color features:
- Color palettes
- Semantic colors
- Gradients
- Theme-specific colors
"""

from chuk_design_system.tokens import ColorTokens, PALETTE, GRADIENTS
from chuk_design_system.themes import get_theme, list_themes


def showcase_palettes():
    """Showcase all color palettes."""
    print("=" * 60)
    print("COLOR PALETTES")
    print("=" * 60)
    print("\nTailwind-inspired color scales (50-950)\n")

    colors = ColorTokens()

    # Show a few key colors with visual blocks
    showcase_hues = ["blue", "green", "purple", "pink", "zinc"]

    for hue in showcase_hues:
        print(f"\n{hue.upper()}:")
        scale = colors.palette[hue]
        for weight in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]:
            # Create color block using ANSI escape codes
            hex_color = scale[weight]
            r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
            # Use background color with RGB
            color_block = f"\033[48;2;{r};{g};{b}m    \033[0m"
            print(f"  {weight:3d}: {color_block}  {hex_color}")


def showcase_semantic_colors():
    """Showcase semantic color system."""
    print("\n" + "=" * 60)
    print("SEMANTIC COLORS (Canva-compatible)")
    print("=" * 60)

    colors = ColorTokens()

    def show_color(label, hex_color):
        """Show a color with visual block."""
        r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
        color_block = f"\033[48;2;{r};{g};{b}m      \033[0m"
        print(f"  {label:12s} {color_block}  {hex_color}")

    # Show dark mode
    print("\nDARK MODE (Blue primary):")
    semantic_dark = colors.get_semantic("blue", "dark")
    show_color("Primary:", semantic_dark.primary.DEFAULT)
    show_color("Accent:", semantic_dark.accent.DEFAULT)
    show_color("Background:", semantic_dark.background.DEFAULT)
    show_color("Foreground:", semantic_dark.foreground.DEFAULT)
    show_color("Success:", semantic_dark.success.DEFAULT)
    show_color("Warning:", semantic_dark.warning.DEFAULT)
    show_color("Error:", semantic_dark.destructive.DEFAULT)

    # Show light mode
    print("\nLIGHT MODE (Purple primary):")
    semantic_light = colors.get_semantic("purple", "light")
    show_color("Primary:", semantic_light.primary.DEFAULT)
    show_color("Accent:", semantic_light.accent.DEFAULT)
    show_color("Background:", semantic_light.background.DEFAULT)
    show_color("Foreground:", semantic_light.foreground.DEFAULT)


def showcase_gradients():
    """Showcase gradient definitions."""
    print("\n" + "=" * 60)
    print("GRADIENTS")
    print("=" * 60)
    print("\nPre-defined gradient options:\n")

    import re

    def extract_gradient_colors(gradient_str):
        """Extract hex colors from gradient string."""
        return re.findall(r'#[0-9a-fA-F]{6}', gradient_str)

    def show_gradient_bar(colors, width=40):
        """Show a gradient bar by interpolating between colors."""
        result = "  "
        steps = width

        # For simplicity, show first and last color transitioning
        if len(colors) >= 2:
            start_color = colors[0]
            end_color = colors[-1]

            # Parse hex colors
            r1, g1, b1 = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:7], 16)
            r2, g2, b2 = int(end_color[1:3], 16), int(end_color[3:5], 16), int(end_color[5:7], 16)

            for i in range(steps):
                t = i / (steps - 1)
                r = int(r1 + (r2 - r1) * t)
                g = int(g1 + (g2 - g1) * t)
                b = int(b1 + (b2 - b1) * t)
                result += f"\033[48;2;{r};{g};{b}m \033[0m"

        return result

    for name, gradient in list(GRADIENTS.items())[:6]:
        colors = extract_gradient_colors(gradient)
        print(f"{name.capitalize()}:")
        print(show_gradient_bar(colors))
        print(f"  Colors: {' → '.join(colors[:3])}")
        print()


def showcase_theme_colors():
    """Showcase theme-specific color schemes."""
    print("\n" + "=" * 60)
    print("THEME COLOR SCHEMES")
    print("=" * 60)

    def show_color_inline(hex_color):
        """Show a color block inline."""
        r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
        return f"\033[48;2;{r};{g};{b}m    \033[0m"

    themes_to_show = ["tech", "finance", "education", "lifestyle"]

    for theme_name in themes_to_show:
        theme = get_theme(theme_name)
        colors = theme["colors"]["semantic"]

        print(f"\n{theme['metadata']['name'].upper()} Theme:")
        print(f"  Primary:    {show_color_inline(colors['primary']['DEFAULT'])}  {colors['primary']['DEFAULT']}")
        print(f"  Accent:     {show_color_inline(colors['accent']['DEFAULT'])}  {colors['accent']['DEFAULT']}")
        print(f"  Background: {show_color_inline(colors['background']['DEFAULT'])}  {colors['background']['DEFAULT']}")
        print(f"  {theme['metadata']['description'][:60]}...")


def showcase_chart_colors():
    """Showcase chart color palettes."""
    print("\n" + "=" * 60)
    print("CHART COLORS (Data Visualization)")
    print("=" * 60)

    colors = ColorTokens()
    semantic = colors.get_semantic("blue", "dark")

    def show_color_inline(hex_color):
        """Show a color block inline."""
        r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
        return f"\033[48;2;{r};{g};{b}m      \033[0m"

    print("\nChart color sequence:")
    for i, color in enumerate(semantic.chart, 1):
        print(f"  Color {i}: {show_color_inline(color)}  {color}")

    # Show all colors in a row
    print("\n  Full palette: ", end="")
    for color in semantic.chart:
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        print(f"\033[48;2;{r};{g};{b}m    \033[0m", end="")
    print()


def main():
    """Run all color showcases."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "   🎨 CHUK DESIGN SYSTEM - COLOR SHOWCASE   ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")

    showcase_palettes()
    showcase_semantic_colors()
    showcase_gradients()
    showcase_theme_colors()
    showcase_chart_colors()

    print("\n" + "=" * 60)
    print("✅ Color showcase complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  - Try: python examples/showcase_typography.py")
    print("  - Try: python examples/showcase_spacing.py")
    print("  - Try: python examples/showcase_motion.py")
    print("  - Try: python examples/design_system_showcase.py (complete)")
    print()


if __name__ == "__main__":
    main()
