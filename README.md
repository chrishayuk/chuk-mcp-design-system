# 🎨 Chuk Design System

A universal design token system with multi-format export capabilities. Define your design system once, export to Canva CSS, Remotion TypeScript, python-pptx, standard CSS, and W3C Design Tokens JSON.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Test Coverage](https://img.shields.io/badge/coverage-89%25-brightgreen.svg)](https://github.com/chrishayuk/chuk-mcp-design-system)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 🎨 **Universal Design Tokens**: Colors, typography, spacing, and motion
- 📦 **Multi-Format Export**: Canva, Remotion, PPTX, CSS, W3C JSON
- 🎭 **7 Pre-Built Themes**: Tech, Finance, Education, Lifestyle, Gaming, Business, Minimal
- 🔒 **Type-Safe**: Pydantic models with full validation
- ✅ **Well-Tested**: 89% test coverage with 200+ tests
- 🚀 **MCP Server**: Claude integration ready
- 📱 **Platform-Aware**: Safe areas for YouTube, TikTok, Instagram
- 🎬 **Video-Optimized**: Frame-perfect durations and Remotion springs

## 🚀 Quick Start

### Installation

```bash
# Using uv (recommended)
uv pip install -e .

# Or using pip
pip install -e .
```

### Basic Usage

```python
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters import export_to_canva_css

# Get a theme
theme = get_theme("tech")

# Export to Canva CSS
css = export_to_canva_css(theme)
print(css)
```

## 🎨 Interactive Showcase

View the design system visually:

```bash
# Generate PNG images + open HTML showcase
make showcase

# Open HTML showcase only
make showcase-html
```

The interactive HTML showcase features **click-to-copy** color swatches, **hover animations** for easing curves, **live typography** samples, and **visual gradients**.

## 📚 Design System Structure

### Colors
- **Palettes**: Tailwind-inspired scales (50-950) for 13+ hues
- **Semantic Colors**: Role-based naming (primary, secondary, success, warning, error)
- **Gradients**: 6 pre-defined gradients (sunset, ocean, forest, flame, aurora, cosmic)
- **Chart Colors**: 8-color sequence for data visualization

### Typography
- **Font Families**: Display, Body, Monospace, Decorative
- **Multi-Resolution Scales**: Web (16px), PPTX (18pt), Video 1080p (40px), Video 4K (80px)
- **Text Styles**: Hero Title, Title, Heading, Body, Caption
- **Font Weights**: Thin (100) to Black (900)

### Spacing
- **8px Unit System**: Canva-compatible (1u = 8px)
- **Platform Safe Areas**: YouTube Shorts, TikTok, Instagram Story
- **Grid Systems**: 4, 8, 12 column grids

### Motion
- **Durations**: Video-optimized with frame conversions (30fps, 60fps)
- **Easing Curves**: Linear, Ease Out, Ease In Out, Smooth, Snappy, Bouncy
- **Spring Configs**: Remotion-compatible physics
- **Transitions**: Enter/exit presets (fade, slide, scale)

## 🎭 Available Themes

| Theme | Primary Color | Use Case |
|-------|---------------|----------|
| Tech | Blue (#3b82f6) | Technology, SaaS products |
| Finance | Green (#22c55e) | Financial services, dashboards |
| Education | Purple (#a855f7) | Learning platforms, courses |
| Lifestyle | Pink (#db2777) | Fashion, beauty, wellness |
| Gaming | Green (#10b981) | Gaming platforms, esports |
| Business | Blue (#3b82f6) | Corporate, professional services |
| Minimal | Zinc (#71717a) | Minimalist designs, portfolios |

## 📦 Export Formats

### Canva CSS
```python
from chuk_design_system.exporters import export_to_canva_css
css = export_to_canva_css(theme)
# Output: --content-primary: #3b82f6;
```

### Remotion TypeScript
```python
from chuk_design_system.exporters import export_to_remotion_ts
ts_code = export_to_remotion_ts(theme)
# Output: export const colorPrimary = "#3b82f6";
```

### python-pptx
```python
from chuk_design_system.exporters.pptx import create_pptx_theme_dict
pptx_theme = create_pptx_theme_dict(theme)
```

### Standard CSS
```python
from chuk_design_system.exporters import export_to_css
css = export_to_css(theme)
```

### W3C Design Tokens JSON
```python
from chuk_design_system.exporters import export_to_w3c_json
json_str = export_to_w3c_json(theme)
```

## 🛠️ Development

### Setup
```bash
make setup
```

### Testing
```bash
make test-cov      # Run tests with coverage
make test-watch    # Run tests in watch mode
make test-quick    # Quick test (stop on first failure)
```

### Code Quality
```bash
make format        # Format code
make lint          # Run linters
make type-check    # Type checking
make all           # Run all checks
```

## 📖 Usage Examples

### Export All Themes
```python
from chuk_design_system.themes import THEMES, get_theme
from chuk_design_system.exporters import export_to_canva_css

for theme_name in THEMES.keys():
    theme = get_theme(theme_name)
    css = export_to_canva_css(theme)
    with open(f"exports/{theme_name}.css", "w") as f:
        f.write(css)
```

### Custom Token Access
```python
from chuk_design_system.tokens import ColorTokens, TypographyTokens

colors = ColorTokens()
primary_blue = colors.palette["blue"][500]  # #3b82f6

typography = TypographyTokens()
hero_style = typography.get_text_style("hero_title", "web")
```

### Motion Tokens for Remotion
```python
from chuk_design_system.tokens import MotionTokens

motion = MotionTokens()
spring_config = motion.get_spring_config("smooth")
# {'damping': 22.0, 'stiffness': 150.0, 'mass': 1.0}

frames = motion.get_duration_frames("normal", fps=30)  # 9 frames
```

## 🔗 Integration

This design system powers:
- **[chuk-mcp-remotion](https://github.com/chrishayuk/chuk-mcp-remotion)**: Video generation
- **[chuk-mcp-pptx](https://github.com/chrishayuk/chuk-mcp-pptx)**: PowerPoint generation
- **Canva Apps**: Design apps with matching UI

## 🤖 MCP Server

Use with Claude via Model Context Protocol:

```json
{
  "mcpServers": {
    "chuk-design-system": {
      "command": "python",
      "args": ["-m", "chuk_design_system.server"]
    }
  }
}
```

## 📝 Makefile Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make test-cov` | Run tests with coverage report |
| `make format` | Format code with black + ruff |
| `make showcase` | Generate visual showcases |
| `make all` | Run all checks |

## 🧪 Test Coverage

Current coverage: **89%** (729 statements, 82 missed)

- tokens/colors.py: **100%**
- tokens/typography.py: **100%**
- tokens/spacing.py: **100%**
- tokens/motion.py: **100%**
- exporters/canva.py: **100%**
- exporters/remotion.py: **100%**
- exporters/pptx.py: **94%**

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Run `make all` to verify
5. Submit a pull request

## 📜 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by Tailwind CSS color palette
- Canva's design token system
- Remotion's spring physics
- W3C Design Tokens specification

