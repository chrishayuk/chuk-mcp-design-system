"""
Typography System Showcase

Demonstrates all typography features:
- Font families
- Font sizes for different mediums
- Text style presets
- Font weights and line heights
"""

from chuk_design_system.tokens import (
    TypographyTokens,
    FONT_FAMILIES,
    FONT_WEIGHTS,
    TEXT_STYLES,
)


def showcase_font_families():
    """Showcase font family definitions."""
    print("=" * 60)
    print("FONT FAMILIES")
    print("=" * 60)
    print()

    for name, family in FONT_FAMILIES.items():
        print(f"{family.name}:")
        print(f"  Stack: {', '.join(family.fonts[:3])}")
        print(f"  Usage: {family.usage}")
        print()


def showcase_font_sizes():
    """Showcase font sizes across mediums."""
    print("=" * 60)
    print("FONT SIZES (Multi-Medium Support)")
    print("=" * 60)

    typography = TypographyTokens()

    mediums = ["web", "pptx", "video_1080p", "video_4k"]

    print("\nComparison of 'base' size across mediums:")
    for medium in mediums:
        sizes = typography.sizes[medium]
        print(f"  {medium:12s}: {sizes.base}")

    print("\nWeb scale (xs → 4xl):")
    web_sizes = typography.sizes["web"]
    for size in ["xs", "sm", "base", "lg", "xl", "xxl", "xxxl", "xxxxl"]:
        value = getattr(web_sizes, size)
        print(f"  {size:4s}: {value}")


def showcase_font_weights():
    """Showcase font weight scale."""
    print("\n" + "=" * 60)
    print("FONT WEIGHTS")
    print("=" * 60)
    print()

    for name, weight in FONT_WEIGHTS.items():
        print(f"  {name:12s}: {weight}")


def showcase_text_styles():
    """Showcase text style presets."""
    print("\n" + "=" * 60)
    print("TEXT STYLE PRESETS")
    print("=" * 60)

    typography = TypographyTokens()

    # Show styles for web with visual samples
    print("\nWeb typography presets:\n")

    samples = {
        "hero_title": "The Quick Brown Fox",
        "title": "The Quick Brown Fox Jumps",
        "heading": "The Quick Brown Fox Jumps Over",
        "body": "The quick brown fox jumps over the lazy dog",
        "caption": "The quick brown fox jumps over the lazy dog - sample caption text"
    }

    # Map weights to ANSI bold codes
    def get_weight_code(weight):
        return "\033[1m" if int(weight) >= 700 else ""

    for style_name in ["hero_title", "title", "heading", "body", "caption"]:
        style = typography.get_text_style(style_name, "web")
        weight_code = get_weight_code(style['fontWeight'])
        reset = "\033[0m"

        print(f"{style['name']}:")
        print(f"  Size: {style['fontSize']}, Weight: {style['fontWeight']}")
        print(f"  Sample: {weight_code}{samples[style_name]}{reset}")
        print()


def showcase_responsive_typography():
    """Showcase responsive typography across mediums."""
    print("=" * 60)
    print("RESPONSIVE TYPOGRAPHY")
    print("=" * 60)

    typography = TypographyTokens()

    print("\n'Hero Title' style across mediums:\n")

    for medium in ["web", "pptx", "video_1080p", "video_4k"]:
        style = typography.get_text_style("hero_title", medium)
        print(f"{medium:12s}: {style['fontSize']} @ {style['fontWeight']} weight")


def main():
    """Run all typography showcases."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "   📝 CHUK DESIGN SYSTEM - TYPOGRAPHY SHOWCASE   ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    showcase_font_families()
    showcase_font_sizes()
    showcase_font_weights()
    showcase_text_styles()
    showcase_responsive_typography()

    print("=" * 60)
    print("✅ Typography showcase complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  - Try: python examples/showcase_colors.py")
    print("  - Try: python examples/showcase_spacing.py")
    print("  - Try: python examples/showcase_motion.py")
    print()


if __name__ == "__main__":
    main()
