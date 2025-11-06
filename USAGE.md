# Usage Guide

## Installation

```bash
# Using uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

## Quick Start

### 1. Using Themes

```python
from chuk_design_system.themes import list_themes, get_theme

# List all available themes
themes = list_themes()
for theme in themes:
    print(f"{theme['name']}: {theme['description']}")

# Get a complete theme
tech_theme = get_theme("tech")
print(tech_theme["colors"]["semantic"]["primary"]["DEFAULT"])  # #3b82f6
```

### 2. Using Tokens Directly

```python
from chuk_design_system.tokens import ColorTokens, TypographyTokens, SpacingTokens

# Color tokens
colors = ColorTokens()
print(colors.palette["blue"][500])  # #3b82f6
semantic = colors.get_semantic("purple", "dark")
print(semantic.primary.DEFAULT)  # #a855f7

# Typography tokens
typography = TypographyTokens()
print(typography.sizes["web"].base)  # 16px
print(typography.sizes["video_1080p"].base)  # 40px

# Spacing tokens (Canva-compatible: 1u = 8px)
spacing = SpacingTokens()
print(spacing.spacing["2u"])  # 16px
print(spacing.spacing_tshirt["md"])  # 16px
```

### 3. Exporting to Different Formats

```python
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters import (
    export_to_canva_css,
    export_to_css,
    export_to_remotion_ts,
    export_to_w3c_json,
)

theme = get_theme("tech")

# Export for Canva app
canva_css = export_to_canva_css(theme)
with open("tech-theme-canva.css", "w") as f:
    f.write(canva_css)

# Export for Remotion video project
remotion_ts = export_to_remotion_ts(theme)
with open("tech-theme.ts", "w") as f:
    f.write(remotion_ts)

# Export standard CSS
css = export_to_css(theme, prefix="tech")
with open("tech-theme.css", "w") as f:
    f.write(css)

# Export W3C Design Tokens JSON
w3c_json = export_to_w3c_json(theme)
with open("tech-theme.json", "w") as f:
    f.write(w3c_json)
```

### 4. Using with python-pptx

```python
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters.pptx import export_colors_pptx, export_font_sizes_pt
from pptx import Presentation
from pptx.util import Pt

theme = get_theme("finance")

# Get colors as RGBColor objects
colors = export_colors_pptx(theme)

# Get font sizes in points
font_sizes = export_font_sizes_pt(theme)

# Use in presentation
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Add shape with theme colors
shape = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(1), Inches(1), Inches(3), Inches(2)
)
shape.fill.solid()
shape.fill.fore_color.rgb = colors["primary"]

# Add text with theme typography
text_frame = shape.text_frame
p = text_frame.paragraphs[0]
p.text = "Finance Theme"
p.font.size = Pt(font_sizes["xl"])
```

### 5. MCP Server Usage

Start the MCP server:

```bash
python -m chuk_design_system.server
```

Claude can then use these tools:

- `list_themes()` - List all available themes
- `get_theme(name)` - Get complete theme with all tokens
- `get_theme_metadata(name)` - Get theme metadata only
- `get_tokens(category, primary_hue, mode, medium)` - Get specific token category
- `export_theme(theme_name, format, css_prefix)` - Export theme to format

## Use Cases

### For chuk-mcp-remotion

```python
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters import export_to_remotion_ts

# Export theme for Remotion project
theme = get_theme("tech")
ts_code = export_to_remotion_ts(theme)

# Save to Remotion project
with open("remotion-project/src/theme.ts", "w") as f:
    f.write(ts_code)

# Access spring configs
springs = theme["motion"]["springs"]
smooth_spring = springs["smooth"]
# Use in Remotion: spring({damping: 22, mass: 1, stiffness: 150})
```

### For chuk-mcp-pptx

```python
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters.pptx import create_pptx_theme_dict

theme = get_theme("business")
pptx_theme = create_pptx_theme_dict(theme)

# Use colors_rgb, font_sizes_pt, spacing_emu in your PPTX generation
colors = pptx_theme["colors_rgb"]
# colors["primary"] = (21, 101, 192)
```

### For Canva Apps

```python
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters import export_to_canva_css

theme = get_theme("lifestyle")
canva_css = export_to_canva_css(theme)

# Save to Canva app
with open("canva-app/styles/theme.css", "w") as f:
    f.write(canva_css)

# Use in Canva app components:
# background-color: var(--content-color-primary);
# padding: var(--content-space-2);
# font-size: var(--content-typography-title-large);
```

## Token Reference

### Colors
- **Palette**: 50-950 scales for 13+ color hues (Tailwind-inspired)
- **Semantic**: Primary, secondary, accent, background, foreground, status colors
- **Gradients**: Pre-defined gradients for each theme

### Typography
- **Font Families**: Display, body, mono, decorative
- **Font Sizes**: Multiple scales for web, pptx, video_1080p, video_4k
- **Weights**: Thin (100) to black (900)
- **Text Styles**: Pre-defined combinations (hero_title, title, heading, etc.)

### Spacing
- **Scale**: 8px-based unit system (Canva-compatible: 1u = 8px)
- **T-shirt sizes**: xs, sm, md, lg, xl, 2xl, 3xl, 4xl
- **Safe Areas**: Platform-specific (YouTube, TikTok, Instagram, etc.)
- **Grid**: 12-column, 8-column, 4-column configurations

### Motion
- **Durations**: instant to slowest (with frame conversions for 30fps/60fps)
- **Easings**: Cubic bezier curves (linear, ease, smooth, bouncy, etc.)
- **Springs**: Remotion-compatible spring configs
- **Transitions**: Pre-defined enter/exit animations

## Available Themes

| Theme | Description | Primary Hue | Best For |
|-------|-------------|-------------|----------|
| **Tech** | Modern blue/cyan | Blue | Technology, SaaS, digital content |
| **Finance** | Professional green/gold | Green | Financial services, banking, investment |
| **Education** | Friendly purple/orange | Purple | Tutorials, courses, learning |
| **Lifestyle** | Warm pink/coral | Pink | Lifestyle, wellness, personal brands |
| **Gaming** | High-energy neon | Green | Gaming, esports, entertainment |
| **Business** | Professional navy/teal | Indigo | Corporate, B2B, professional services |
| **Minimal** | Clean monochrome | Zinc | Minimalist design, typography focus |

## Export Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| **Canva CSS** | --content-* variables | Canva app development |
| **Remotion TS** | TypeScript constants | Remotion video projects |
| **Standard CSS** | Custom CSS variables | Web projects |
| **W3C JSON** | Design Tokens spec | Tool interoperability |
| **python-pptx** | RGBColor, Pt values | PowerPoint generation |

## Advanced Usage

### Custom Theme Configuration

```python
from chuk_design_system.themes.base import BaseTheme, ThemeColors, resolve_theme

# Create custom theme
custom_theme = BaseTheme(
    name="MyBrand",
    description="Custom brand theme",
    category="tech",
    colors=ThemeColors(
        primary_hue="violet",
        mode="dark",
        gradient="linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)"
    ),
    tags=["custom", "brand"]
)

# Resolve to get all tokens
resolved = resolve_theme(custom_theme)
```

### Filtering Tokens

```python
from chuk_design_system.tokens import get_all_tokens

# Get only what you need
tokens = get_all_tokens(primary_hue="blue", mode="dark", medium="video_1080p")

# Extract specific categories
colors_only = tokens["colors"]
typography_only = tokens["typography"]
```

## Next Steps

- Check `examples/basic_usage.py` for more examples
- Run tests with `pytest tests/`
- Integrate with chuk-mcp-remotion or chuk-mcp-pptx projects
- Build your own Canva app using the exported CSS variables
