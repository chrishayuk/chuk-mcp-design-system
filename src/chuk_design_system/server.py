"""
MCP Server for Chuk Design System.

Provides Claude with tools to query themes, tokens, and export to various formats.
"""

import json
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent

from chuk_design_system.themes import list_themes, get_theme, get_theme_metadata
from chuk_design_system.tokens import get_all_tokens
from chuk_design_system.exporters import (
    export_to_canva_css,
    export_to_css,
    export_to_remotion_ts,
    export_to_w3c_json,
)


# Initialize MCP server
server = Server("chuk-design-system")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available MCP tools."""
    return [
        Tool(
            name="list_themes",
            description="List all available design themes with their metadata",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        Tool(
            name="get_theme",
            description="Get a complete theme with all resolved design tokens",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Theme name (tech, finance, education, lifestyle, gaming, business, minimal)",
                    }
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="get_theme_metadata",
            description="Get theme metadata without full token resolution (faster)",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Theme name",
                    }
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="get_tokens",
            description="Get specific token category (colors, typography, spacing, motion)",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["colors", "typography", "spacing", "motion", "all"],
                        "description": "Token category to retrieve",
                    },
                    "primary_hue": {
                        "type": "string",
                        "description": "Primary color hue (for colors)",
                        "default": "blue",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["dark", "light"],
                        "description": "Color mode (for colors)",
                        "default": "dark",
                    },
                    "medium": {
                        "type": "string",
                        "enum": ["web", "pptx", "video_1080p", "video_4k"],
                        "description": "Typography medium",
                        "default": "web",
                    },
                },
                "required": ["category"],
            },
        ),
        Tool(
            name="export_theme",
            description="Export theme to specific format (canva, css, remotion, w3c_json)",
            inputSchema={
                "type": "object",
                "properties": {
                    "theme_name": {
                        "type": "string",
                        "description": "Theme name to export",
                    },
                    "format": {
                        "type": "string",
                        "enum": ["canva", "css", "remotion", "w3c_json"],
                        "description": "Export format",
                    },
                    "css_prefix": {
                        "type": "string",
                        "description": "CSS variable prefix (for css format)",
                        "default": "ds",
                    },
                },
                "required": ["theme_name", "format"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls."""

    try:
        if name == "list_themes":
            themes = list_themes()
            result = json.dumps(themes, indent=2)
            return [TextContent(type="text", text=result)]

        elif name == "get_theme":
            theme_name = arguments.get("name")
            theme = get_theme(theme_name)
            result = json.dumps(theme, indent=2)
            return [TextContent(type="text", text=result)]

        elif name == "get_theme_metadata":
            theme_name = arguments.get("name")
            metadata = get_theme_metadata(theme_name)
            result = json.dumps(metadata, indent=2)
            return [TextContent(type="text", text=result)]

        elif name == "get_tokens":
            category = arguments.get("category")
            primary_hue = arguments.get("primary_hue", "blue")
            mode = arguments.get("mode", "dark")
            medium = arguments.get("medium", "web")

            if category == "all":
                tokens = get_all_tokens(primary_hue, mode, medium)
            else:
                from chuk_design_system.tokens import (
                    ColorTokens,
                    TypographyTokens,
                    SpacingTokens,
                    MotionTokens,
                )

                if category == "colors":
                    color_tokens = ColorTokens()
                    tokens = color_tokens.get_all(primary_hue, mode)
                elif category == "typography":
                    typo_tokens = TypographyTokens()
                    tokens = typo_tokens.get_all(medium)
                elif category == "spacing":
                    spacing_tokens = SpacingTokens()
                    tokens = spacing_tokens.get_all()
                elif category == "motion":
                    motion_tokens = MotionTokens()
                    tokens = motion_tokens.get_all()
                else:
                    return [
                        TextContent(
                            type="text",
                            text=f"Unknown category: {category}",
                        )
                    ]

            result = json.dumps(tokens, indent=2)
            return [TextContent(type="text", text=result)]

        elif name == "export_theme":
            theme_name = arguments.get("theme_name")
            export_format = arguments.get("format")
            css_prefix = arguments.get("css_prefix", "ds")

            # Get the theme
            theme = get_theme(theme_name)

            # Export to requested format
            if export_format == "canva":
                output = export_to_canva_css(theme)
            elif export_format == "css":
                output = export_to_css(theme, prefix=css_prefix)
            elif export_format == "remotion":
                output = export_to_remotion_ts(theme)
            elif export_format == "w3c_json":
                output = export_to_w3c_json(theme)
            else:
                return [
                    TextContent(
                        type="text",
                        text=f"Unknown export format: {export_format}",
                    )
                ]

            return [TextContent(type="text", text=output)]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        error_msg = f"Error executing {name}: {str(e)}"
        return [TextContent(type="text", text=error_msg)]


async def main():
    """Run the MCP server."""
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
