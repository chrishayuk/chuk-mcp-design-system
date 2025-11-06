"""
Spacing System Showcase

Demonstrates all spacing features:
- 8px unit system (Canva-compatible)
- Safe areas for platforms
- Grid systems
- Aspect ratios
"""

from chuk_design_system.tokens import SpacingTokens, SPACING, SAFE_AREAS, GRID


def showcase_spacing_scale():
    """Showcase 8px-based spacing scale."""
    print("=" * 60)
    print("SPACING SCALE (8px base unit)")
    print("=" * 60)
    print("\nCanva-compatible: 1u = 8px\n")

    spacing = SpacingTokens()

    # Show unit-based spacing
    print("Unit-based (recommended):")
    for unit in ["0.5u", "1u", "2u", "3u", "4u", "6u", "8u"]:
        print(f"  {unit:4s} = {spacing.spacing[unit]}")

    # Show t-shirt sizing
    print("\nT-shirt sizing:")
    for size in ["xs", "sm", "md", "lg", "xl", "2xl"]:
        print(f"  {size:3s} = {spacing.spacing_tshirt[size]}")


def showcase_safe_areas():
    """Showcase platform-specific safe areas."""
    print("\n" + "=" * 60)
    print("PLATFORM SAFE AREAS")
    print("=" * 60)

    spacing = SpacingTokens()

    platforms = [
        "youtube_shorts",
        "tiktok",
        "instagram_story",
        "youtube_landscape",
        "presentation",
    ]

    print("\nAvoid UI overlays with safe areas:\n")

    for platform in platforms:
        safe_area = spacing.get_safe_area(platform)
        print(f"{platform.replace('_', ' ').title()}:")
        print(f"  Aspect: {safe_area.aspect_ratio}")
        print(
            f"  Padding: T:{safe_area.top}px R:{safe_area.right}px B:{safe_area.bottom}px L:{safe_area.left}px"
        )
        print(f"  Usage: {safe_area.usage}")
        print()


def showcase_grid_systems():
    """Showcase grid configurations."""
    print("=" * 60)
    print("GRID SYSTEMS")
    print("=" * 60)

    spacing = SpacingTokens()

    print("\nResponsive grid configurations:\n")

    for columns in [12, 8, 4]:
        grid = spacing.get_grid(columns)
        print(f"{columns}-Column Grid:")
        print(f"  Columns: {grid.columns}")
        print(f"  Gap: {grid.gap}")
        print(f"  Margin: {grid.margin}")
        print()


def showcase_layout_tokens():
    """Showcase layout-related tokens."""
    print("=" * 60)
    print("LAYOUT TOKENS")
    print("=" * 60)

    spacing = SpacingTokens()

    # Border radius
    print("\nBorder Radius:")
    for name in ["none", "sm", "md", "lg", "xl", "full"]:
        print(f"  {name:4s}: {spacing.radius[name]}")

    # Container widths
    print("\nContainer Widths:")
    for name in ["sm", "md", "lg", "xl", "2xl", "full"]:
        print(f"  {name:3s}: {spacing.containers[name]}")

    # Aspect ratios
    print("\nAspect Ratios:")
    for name, ratio in spacing.aspect_ratios.items():
        print(f"  {name:12s}: {ratio}")


def showcase_z_index():
    """Showcase z-index layering system."""
    print("\n" + "=" * 60)
    print("Z-INDEX LAYERS")
    print("=" * 60)
    print("\nStacking order for UI elements:\n")

    spacing = SpacingTokens()

    for name, value in spacing.z_index.items():
        print(f"  {name:12s}: {value}")


def main():
    """Run all spacing showcases."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "   📏 CHUK DESIGN SYSTEM - SPACING SHOWCASE   ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    showcase_spacing_scale()
    showcase_safe_areas()
    showcase_grid_systems()
    showcase_layout_tokens()
    showcase_z_index()

    print("=" * 60)
    print("✅ Spacing showcase complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  - Try: python examples/showcase_colors.py")
    print("  - Try: python examples/showcase_typography.py")
    print("  - Try: python examples/showcase_motion.py")
    print()


if __name__ == "__main__":
    main()
