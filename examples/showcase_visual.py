"""
Visual Design System Showcase

Generates PNG images showing colors, gradients, typography, and more.
This provides a proper visual representation that terminal output cannot.
"""

from PIL import Image, ImageDraw, ImageFont
import sys
from pathlib import Path

from chuk_design_system.tokens import ColorTokens, TypographyTokens, GRADIENTS, PALETTE
from chuk_design_system.themes import get_theme


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def create_color_palette_image(output_path="output/color_palettes.png"):
    """Generate color palette showcase image."""
    # Image dimensions
    width, height = 1200, 800
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    colors = ColorTokens()
    hues = ["blue", "green", "purple", "pink", "orange", "zinc"]
    weights = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]

    # Title
    draw.text((20, 20), "Color Palettes", fill=(0, 0, 0), font=None)

    # Draw color swatches
    swatch_width = 80
    swatch_height = 50
    start_y = 60

    for i, hue in enumerate(hues):
        # Draw hue label
        draw.text((20, start_y + i * (swatch_height + 5)), hue.capitalize(), fill=(0, 0, 0))

        scale = colors.palette[hue]
        for j, weight in enumerate(weights):
            x = 100 + j * (swatch_width + 2)
            y = start_y + i * (swatch_height + 5)

            color = hex_to_rgb(scale[weight])
            draw.rectangle([x, y, x + swatch_width, y + swatch_height], fill=color)

            # Add weight label
            text_color = (255, 255, 255) if weight >= 500 else (0, 0, 0)
            draw.text((x + 5, y + 5), str(weight), fill=text_color)

    img.save(output_path)
    print(f"✅ Saved color palette to {output_path}")
    return output_path


def create_gradient_image(output_path="output/gradients.png"):
    """Generate gradient showcase image."""
    width, height = 1200, 600
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((20, 20), "Gradients", fill=(0, 0, 0), font=None)

    # Extract colors from gradient strings
    import re

    def extract_colors(gradient_str):
        return re.findall(r"#[0-9a-fA-F]{6}", gradient_str)

    def draw_gradient(draw, x, y, w, h, colors):
        """Draw a horizontal gradient."""
        if len(colors) < 2:
            return

        start_rgb = hex_to_rgb(colors[0])
        end_rgb = hex_to_rgb(colors[-1])

        for i in range(w):
            t = i / (w - 1)
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t)

            draw.line([(x + i, y), (x + i, y + h)], fill=(r, g, b))

    # Draw each gradient
    gradient_height = 80
    start_y = 60

    for i, (name, gradient_str) in enumerate(list(GRADIENTS.items())[:6]):
        y = start_y + i * (gradient_height + 10)

        # Draw gradient name
        draw.text((20, y + 30), name.capitalize(), fill=(0, 0, 0))

        # Draw gradient
        colors = extract_colors(gradient_str)
        draw_gradient(draw, 150, y, 1000, gradient_height, colors)

        # Draw color labels
        for j, color in enumerate(colors[:3]):
            label_x = 150 + j * 200
            draw.text((label_x, y + gradient_height + 5), color, fill=(0, 0, 0))

    img.save(output_path)
    print(f"✅ Saved gradients to {output_path}")
    return output_path


def create_semantic_colors_image(output_path="output/semantic_colors.png"):
    """Generate semantic colors showcase image."""
    width, height = 1000, 600
    img = Image.new("RGB", (width, height), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)

    colors = ColorTokens()

    # Title
    draw.text((20, 20), "Semantic Colors", fill=(0, 0, 0), font=None)

    # Dark mode section
    draw.text((20, 60), "Dark Mode (Blue Primary)", fill=(0, 0, 0))
    semantic_dark = colors.get_semantic("blue", "dark")

    roles = [
        ("Primary", semantic_dark.primary.DEFAULT),
        ("Accent", semantic_dark.accent.DEFAULT),
        ("Background", semantic_dark.background.DEFAULT),
        ("Foreground", semantic_dark.foreground.DEFAULT),
        ("Success", semantic_dark.success.DEFAULT),
        ("Warning", semantic_dark.warning.DEFAULT),
        ("Error", semantic_dark.destructive.DEFAULT),
    ]

    swatch_size = 120
    for i, (role, hex_color) in enumerate(roles):
        x = 20 + (i % 4) * (swatch_size + 20)
        y = 100 + (i // 4) * (swatch_size + 40)

        rgb = hex_to_rgb(hex_color)
        draw.rectangle([x, y, x + swatch_size, y + swatch_size], fill=rgb, outline=(0, 0, 0))

        # Label
        draw.text((x, y + swatch_size + 5), role, fill=(0, 0, 0))
        draw.text((x, y + swatch_size + 20), hex_color, fill=(100, 100, 100))

    # Light mode section
    draw.text((20, 340), "Light Mode (Purple Primary)", fill=(0, 0, 0))
    semantic_light = colors.get_semantic("purple", "light")

    roles_light = [
        ("Primary", semantic_light.primary.DEFAULT),
        ("Accent", semantic_light.accent.DEFAULT),
        ("Background", semantic_light.background.DEFAULT),
        ("Foreground", semantic_light.foreground.DEFAULT),
    ]

    for i, (role, hex_color) in enumerate(roles_light):
        x = 20 + i * (swatch_size + 20)
        y = 380

        rgb = hex_to_rgb(hex_color)
        draw.rectangle([x, y, x + swatch_size, y + swatch_size], fill=rgb, outline=(0, 0, 0))

        # Label
        draw.text((x, y + swatch_size + 5), role, fill=(0, 0, 0))
        draw.text((x, y + swatch_size + 20), hex_color, fill=(100, 100, 100))

    img.save(output_path)
    print(f"✅ Saved semantic colors to {output_path}")
    return output_path


def create_theme_comparison_image(output_path="output/theme_comparison.png"):
    """Generate theme comparison showcase image."""
    width, height = 1400, 800
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((20, 20), "Theme Comparison", fill=(0, 0, 0), font=None)

    themes = ["tech", "finance", "education", "lifestyle", "gaming", "business"]

    card_width = 220
    card_height = 300
    margin = 20

    for i, theme_name in enumerate(themes):
        theme = get_theme(theme_name)
        colors = theme["colors"]["semantic"]

        # Calculate position
        col = i % 3
        row = i // 3
        x = margin + col * (card_width + margin)
        y = 80 + row * (card_height + margin)

        # Draw theme card background
        bg_color = hex_to_rgb(colors["background"]["DEFAULT"])
        draw.rectangle([x, y, x + card_width, y + card_height], fill=bg_color, outline=(200, 200, 200))

        # Theme name
        fg_color = hex_to_rgb(colors["foreground"]["DEFAULT"])
        draw.text((x + 10, y + 10), theme["metadata"]["name"], fill=fg_color)

        # Color swatches
        swatch_height = 40
        color_roles = [
            ("Primary", colors["primary"]["DEFAULT"]),
            ("Accent", colors["accent"]["DEFAULT"]),
            ("Success", colors["success"]["DEFAULT"]),
            ("Warning", colors["warning"]["DEFAULT"]),
        ]

        for j, (role, hex_color) in enumerate(color_roles):
            swatch_y = y + 50 + j * (swatch_height + 10)
            rgb = hex_to_rgb(hex_color)
            draw.rectangle([x + 10, swatch_y, x + card_width - 10, swatch_y + swatch_height], fill=rgb)

            # Role label
            text_color = (255, 255, 255) if sum(rgb) < 400 else (0, 0, 0)
            draw.text((x + 15, swatch_y + 10), role, fill=text_color)

    img.save(output_path)
    print(f"✅ Saved theme comparison to {output_path}")
    return output_path


def create_typography_image(output_path="output/typography.png"):
    """Generate typography showcase image."""
    width, height = 1400, 1000
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    typography = TypographyTokens()

    # Title
    draw.text((20, 20), "Typography System", fill=(0, 0, 0), font=None)

    # Try to use system fonts for better rendering
    try:
        # Try different font sizes for demonstration
        from PIL import ImageFont

        # System fonts that are commonly available
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/SFNSDisplay.ttf",
            "/Library/Fonts/Arial.ttf",
        ]

        fonts = {}
        for size in [12, 14, 16, 20, 24, 30, 36, 48]:
            for font_path in font_paths:
                try:
                    fonts[size] = ImageFont.truetype(font_path, size)
                    break
                except:
                    continue
            if size not in fonts:
                fonts[size] = None
    except:
        fonts = {size: None for size in [12, 14, 16, 20, 24, 30, 36, 48]}

    # Text style presets showcase
    y_offset = 80
    sample_text = "The quick brown fox jumps over the lazy dog"

    styles = [
        ("hero_title", "Hero Title", 48),
        ("title", "Title", 36),
        ("heading", "Heading", 24),
        ("body", "Body Text", 16),
        ("caption", "Caption", 14),
    ]

    for style_name, label, size in styles:
        style = typography.get_text_style(style_name, "web")

        # Draw style label
        draw.text((20, y_offset), f"{label} ({style['fontSize']}, weight {style['fontWeight']})",
                  fill=(100, 100, 100), font=fonts.get(12))

        # Draw sample text with appropriate font
        font = fonts.get(size)
        draw.text((20, y_offset + 25), sample_text[:40], fill=(0, 0, 0), font=font)

        y_offset += 100

    # Font size comparison across mediums
    draw.text((20, 600), "Multi-Medium Font Scales", fill=(0, 0, 0), font=fonts.get(16))

    mediums = ["web", "pptx", "video_1080p", "video_4k"]
    medium_labels = ["Web (16px)", "PPTX (18pt)", "Video 1080p (40px)", "Video 4K (80px)"]

    y_offset = 640
    for i, (medium, label) in enumerate(zip(mediums, medium_labels)):
        sizes = typography.sizes[medium]
        x_offset = 20 + (i * 320)

        draw.text((x_offset, y_offset), label, fill=(100, 100, 100), font=fonts.get(12))
        draw.text((x_offset, y_offset + 25), f"Base: {sizes.base}", fill=(0, 0, 0), font=fonts.get(14))
        draw.text((x_offset, y_offset + 50), f"Large: {sizes.lg}", fill=(0, 0, 0), font=fonts.get(14))
        draw.text((x_offset, y_offset + 75), f"XL: {sizes.xl}", fill=(0, 0, 0), font=fonts.get(14))

    # Font weights demonstration
    draw.text((20, 800), "Font Weights", fill=(0, 0, 0), font=fonts.get(16))

    weights_demo = [
        ("Light (300)", 300),
        ("Regular (400)", 400),
        ("Medium (500)", 500),
        ("Semibold (600)", 600),
        ("Bold (700)", 700),
        ("Black (900)", 900),
    ]

    y_offset = 840
    for i, (label, weight) in enumerate(weights_demo):
        x_offset = 20 + (i % 3) * 400
        y = y_offset + (i // 3) * 40

        draw.text((x_offset, y), f"{label}: Aa Bb 123", fill=(0, 0, 0), font=fonts.get(16))

    img.save(output_path)
    print(f"✅ Saved typography to {output_path}")
    return output_path


def create_motion_image(output_path="output/motion.png"):
    """Generate motion/animation showcase image."""
    width, height = 1400, 1000
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    from chuk_design_system.tokens import MotionTokens, DURATIONS, EASINGS, SPRINGS

    motion = MotionTokens()

    # Title
    draw.text((20, 20), "Motion & Animation System", fill=(0, 0, 0), font=None)

    # Durations with frame visualization
    draw.text((20, 60), "Durations (Video-optimized)", fill=(0, 0, 0), font=None)

    durations_to_show = [
        ("instant", DURATIONS["instant"]),
        ("fast", DURATIONS["fast"]),
        ("normal", DURATIONS["normal"]),
        ("slow", DURATIONS["slow"]),
        ("slowest", DURATIONS["slowest"]),
    ]

    y_offset = 90
    for name, duration in durations_to_show:
        # Draw duration info
        draw.text((20, y_offset), f"{name.capitalize()}: {duration.ms}ms", fill=(0, 0, 0))
        draw.text((200, y_offset), f"30fps: {duration.frames_30fps}f", fill=(100, 100, 100))
        draw.text((320, y_offset), f"60fps: {duration.frames_60fps}f", fill=(100, 100, 100))

        # Draw timeline bar
        bar_width = min(duration.frames_30fps * 10, 400)
        draw.rectangle([450, y_offset, 450 + bar_width, y_offset + 20],
                      fill=(59, 130, 246), outline=(0, 0, 0))

        y_offset += 35

    # Easing curves visualization
    draw.text((20, 300), "Easing Curves", fill=(0, 0, 0), font=None)

    easings_to_show = [
        ("linear", EASINGS["linear"]),
        ("ease_out", EASINGS["ease_out"]),
        ("ease_in_out", EASINGS["ease_in_out"]),
        ("smooth", EASINGS["smooth"]),
        ("snappy", EASINGS["snappy"]),
        ("bouncy", EASINGS["bouncy"]),
    ]

    def draw_easing_curve(draw, x, y, width, height, curve_points):
        """Draw an easing curve visualization."""
        # Draw box
        draw.rectangle([x, y, x + width, y + height], outline=(200, 200, 200))

        # Draw curve
        steps = 50
        points = []
        for i in range(steps):
            t = i / (steps - 1)
            # Approximate bezier curve
            if curve_points == [0.0, 0.0, 1.0, 1.0]:  # linear
                eased = t
            elif curve_points == [0.0, 0.0, 0.58, 1.0]:  # ease_out
                eased = 1 - (1 - t) ** 2
            elif curve_points == [0.42, 0.0, 0.58, 1.0]:  # ease_in_out
                eased = t ** 2 if t < 0.5 else 1 - (1 - t) ** 2
            elif curve_points == [0.4, 0.0, 0.2, 1.0]:  # smooth
                eased = 1 - (1 - t) ** 1.8
            elif curve_points == [0.4, 0.0, 0.6, 1.0]:  # snappy
                eased = 1 - (1 - t) ** 1.5
            else:  # bouncy
                eased = min(1.2, 1 - (1 - t) ** 2 * (1 + 0.2 * (1 - t)))

            px = x + t * width
            py = y + height - eased * height
            points.append((px, py))

        # Draw the curve line
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=(59, 130, 246), width=2)

    curve_y = 330
    for i, (name, easing) in enumerate(easings_to_show):
        col = i % 3
        row = i // 3

        x = 20 + col * 450
        y = curve_y + row * 180

        # Label
        draw.text((x, y), name.replace("_", " ").title(), fill=(0, 0, 0))
        draw.text((x, y + 15), f"{easing.curve}", fill=(100, 100, 100))

        # Draw curve
        draw_easing_curve(draw, x, y + 40, 120, 100, easing.curve)

    # Spring configurations
    draw.text((20, 700), "Spring Configurations (Remotion-compatible)", fill=(0, 0, 0), font=None)

    springs_to_show = [
        ("gentle", SPRINGS["gentle"]),
        ("smooth", SPRINGS["smooth"]),
        ("bouncy", SPRINGS["bouncy"]),
        ("snappy", SPRINGS["snappy"]),
        ("stiff", SPRINGS["stiff"]),
    ]

    y_offset = 730
    for name, spring in springs_to_show:
        config = motion.get_spring_config(name)

        draw.text((20, y_offset), f"{name.capitalize()}:", fill=(0, 0, 0))
        draw.text((120, y_offset),
                 f"damping={config['damping']}, stiffness={config['stiffness']}, mass={config['mass']}",
                 fill=(100, 100, 100))

        # Draw spring feel indicator
        stiffness_bar = int(config['stiffness'] / 2)
        draw.rectangle([600, y_offset, 600 + stiffness_bar, y_offset + 15],
                      fill=(139, 92, 246))

        y_offset += 30

    img.save(output_path)
    print(f"✅ Saved motion to {output_path}")
    return output_path


def create_spacing_image(output_path="output/spacing.png"):
    """Generate spacing system showcase image."""
    width, height = 1200, 800
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    from chuk_design_system.tokens import SpacingTokens, SPACING

    spacing = SpacingTokens()

    # Title
    draw.text((20, 20), "Spacing System (8px base unit)", fill=(0, 0, 0), font=None)

    # Spacing scale visualization
    draw.text((20, 60), "Spacing Scale", fill=(0, 0, 0), font=None)

    units = ["0.5u", "1u", "2u", "3u", "4u", "6u", "8u"]

    y_offset = 90
    for unit in units:
        value = SPACING[unit]
        px_value = int(value.replace("px", ""))

        # Draw label
        draw.text((20, y_offset), f"{unit} ({value})", fill=(0, 0, 0))

        # Draw spacing visualization
        draw.rectangle([150, y_offset, 150 + px_value, y_offset + 20],
                      fill=(59, 130, 246), outline=(0, 0, 0))

        y_offset += 40

    # Safe areas visualization
    draw.text((20, 400), "Platform Safe Areas", fill=(0, 0, 0), font=None)

    platforms = ["youtube_shorts", "tiktok", "instagram_story"]

    x_offset = 20
    for platform in platforms:
        safe_area = spacing.get_safe_area(platform)

        # Draw platform card
        card_width = 180
        card_height = 320

        draw.text((x_offset, 430), platform.replace("_", " ").title(), fill=(0, 0, 0))

        # Draw outer box (viewport)
        draw.rectangle([x_offset, 460, x_offset + card_width, 460 + card_height],
                      fill=(240, 240, 240), outline=(0, 0, 0))

        # Draw safe area (inset)
        safe_x1 = x_offset + safe_area.left // 4
        safe_y1 = 460 + safe_area.top // 4
        safe_x2 = x_offset + card_width - safe_area.right // 4
        safe_y2 = 460 + card_height - safe_area.bottom // 4

        draw.rectangle([safe_x1, safe_y1, safe_x2, safe_y2],
                      fill=(144, 238, 144), outline=(34, 197, 94), width=2)

        # Labels
        draw.text((x_offset + 5, 470), f"T:{safe_area.top}", fill=(100, 100, 100))
        draw.text((x_offset + 5, 760), f"B:{safe_area.bottom}", fill=(100, 100, 100))

        x_offset += card_width + 40

    # Grid systems
    draw.text((700, 400), "Grid Systems", fill=(0, 0, 0), font=None)

    for i, columns in enumerate([12, 8, 4]):
        grid = spacing.get_grid(columns)
        y = 430 + i * 100

        draw.text((700, y), f"{columns}-Column Grid", fill=(0, 0, 0))
        draw.text((700, y + 20), f"Gap: {grid.gap}, Margin: {grid.margin}", fill=(100, 100, 100))

        # Draw simplified grid
        grid_width = 400
        col_width = (grid_width - (columns - 1) * 4) // columns

        for col in range(columns):
            x = 700 + col * (col_width + 4)
            draw.rectangle([x, y + 45, x + col_width, y + 65],
                          fill=(200, 200, 255), outline=(100, 100, 200))

    img.save(output_path)
    print(f"✅ Saved spacing to {output_path}")
    return output_path


def main():
    """Generate all visual showcases."""
    print("\n" + "=" * 60)
    print("🎨 GENERATING VISUAL DESIGN SYSTEM SHOWCASE")
    print("=" * 60 + "\n")

    # Create output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Generate images
    files = []
    files.append(create_color_palette_image())
    files.append(create_gradient_image())
    files.append(create_semantic_colors_image())
    files.append(create_theme_comparison_image())
    files.append(create_typography_image())
    files.append(create_motion_image())
    files.append(create_spacing_image())

    print("\n" + "=" * 60)
    print("✅ Visual showcase complete!")
    print("=" * 60)
    print("\nGenerated files:")
    for file in files:
        print(f"  - {file}")
    print("\nOpen these PNG files to see the design system visually!")
    print()


if __name__ == "__main__":
    main()
