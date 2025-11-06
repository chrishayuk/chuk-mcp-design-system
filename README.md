# Chuk Design System

Universal design system with tokens, themes, and multi-format export capabilities. Built to power consistent design across Remotion videos, PowerPoint presentations, LinkedIn carousels, and more.

## Features

- **Universal Design Tokens**: Colors, typography, spacing, motion tokens that work everywhere
- **Multi-Format Export**: Export to Canva CSS, Remotion TypeScript, python-pptx, standard CSS, Tailwind config, W3C Design Tokens spec
- **Theme System**: Pre-built themes (Tech, Finance, Education, Lifestyle, Gaming, etc.)
- **Semantic Tokens**: Canva-compatible semantic naming (action, typography, background roles)
- **Type-Safe**: Pydantic models for all tokens and themes
- **MCP Server**: Claude-friendly MCP server for LLM integration

## Architecture

```
Your Design System (Single Source of Truth)
           ↓
    Multiple Exporters
           ↓
┌─────────┬──────────┬─────────┬─────────┐
│ Remotion│   PPTX   │  Canva  │   CSS   │
│  Videos │  Slides  │  Apps   │   Web   │
└─────────┴──────────┴─────────┴─────────┘
```

## Installation

```bash
pip install -e .
```

## Usage

### Python API

```python
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters import canva, remotion, pptx

# Get a theme
theme = get_theme("tech")

# Export to different formats
canva_css = canva.export_to_css(theme)
remotion_ts = remotion.export_to_typescript(theme)
pptx_colors = pptx.export_colors(theme)
```

### MCP Server

```bash
# Start the MCP server
python -m chuk_design_system.server
```

Claude can then use tools like:
- `get_theme(name)` - Get a complete theme
- `list_themes()` - List available themes
- `get_tokens(category)` - Get specific token category
- `export_theme(name, format)` - Export theme to specific format

## Token Categories

- **Colors**: Palette (50-950 scales), semantic tokens, gradients
- **Typography**: Font families, sizes, weights, line heights, text styles
- **Spacing**: Scale, margins, padding, grid, containers
- **Motion**: Durations, easings, springs, transitions (Remotion-specific)

## Themes

Pre-built themes optimized for different content types:
- **Tech**: Modern blue/cyan palette
- **Finance**: Professional green/gold
- **Education**: Friendly purple/orange
- **Lifestyle**: Warm coral/pink
- **Gaming**: High-energy neon
- **Business**: Professional navy/teal
- **Minimal**: Clean monochrome

## Export Formats

### Canva CSS Variables
```css
:root {
  --content-color-primary: #0066FF;
  --content-space-1: 8px;
  --content-typography-title-large: 48px;
}
```

### Remotion TypeScript
```typescript
export const colorPrimary = "#0066FF";
export const spacing1 = "8px";
```

### python-pptx
```python
from pptx.util import RGBColor
colors = {"primary": RGBColor(0, 102, 255)}
```

### W3C Design Tokens
```json
{
  "color": {
    "primary": {
      "$type": "color",
      "$value": "#0066FF"
    }
  }
}
```

## Philosophy

This design system follows the principle: **Your tokens → Multiple export targets = Maximum leverage**

- Single source of truth for all design decisions
- Export to any format without vendor lock-in
- Semantic naming for clarity and Canva compatibility
- Type-safe for reliability
- LLM-friendly for AI-assisted design

## Related Projects

- [chuk-mcp-remotion](https://github.com/chrishayuk/chuk-mcp-remotion) - Remotion video generation
- [chuk-mcp-pptx](https://github.com/chrishayuk/chuk-mcp-pptx) - PowerPoint generation
- [chuk-mcp-linkedin](https://github.com/chrishayuk/chuk-mcp-linkedin) - LinkedIn carousel generation (coming soon)

## License

MIT
