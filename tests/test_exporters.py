"""Comprehensive tests for export functionality."""

import json
from chuk_design_system.themes import get_theme
from chuk_design_system.exporters.canva import export_to_canva_css, export_colors_only
from chuk_design_system.exporters.css import export_to_css, export_utility_classes
from chuk_design_system.exporters.remotion import export_to_remotion_ts, export_spring_only
from chuk_design_system.exporters.json_export import export_to_w3c_json, export_tokens_minimal
from chuk_design_system.exporters.pptx import (
    hex_to_rgb,
    export_colors,
    export_font_sizes_pt,
    export_spacing_emu,
    create_pptx_theme_dict,
)


class TestCanvaExporter:
    """Test Canva CSS export."""

    def test_export_to_canva_css(self):
        """Test basic Canva CSS export."""
        theme = get_theme("tech")
        css = export_to_canva_css(theme)
        assert css is not None
        assert ":root" in css
        assert "--content-color-primary" in css

    def test_canva_color_variables(self):
        """Test that Canva color variables are exported."""
        theme = get_theme("tech")
        css = export_to_canva_css(theme)
        assert "--content-color-primary:" in css
        assert "--content-color-secondary:" in css
        assert "--content-color-bg:" in css

    def test_canva_spacing_variables(self):
        """Test that Canva spacing variables are exported."""
        theme = get_theme("tech")
        css = export_to_canva_css(theme)
        assert "--content-space-" in css

    def test_canva_typography_variables(self):
        """Test that Canva typography variables are exported."""
        theme = get_theme("tech")
        css = export_to_canva_css(theme)
        assert "--content-typography-" in css

    def test_export_colors_only(self):
        """Test export_colors_only function."""
        theme = get_theme("finance")
        css = export_colors_only(theme)
        assert ":root" in css
        assert "--content-color-" in css
        # Should not have spacing or typography
        assert "--content-space-" not in css

    def test_canva_status_colors(self):
        """Test that status colors are exported."""
        theme = get_theme("tech")
        css = export_to_canva_css(theme)
        assert "--content-color-success:" in css
        assert "--content-color-warning:" in css
        assert "--content-color-error:" in css


class TestCSSExporter:
    """Test standard CSS export."""

    def test_export_to_css(self):
        """Test basic CSS export."""
        theme = get_theme("tech")
        css = export_to_css(theme)
        assert css is not None
        assert ":root" in css

    def test_css_with_custom_prefix(self):
        """Test CSS export with custom prefix."""
        theme = get_theme("tech")
        css = export_to_css(theme, prefix="custom")
        assert "--custom-color-" in css
        assert "--custom-space-" in css

    def test_css_includes_comments(self):
        """Test that CSS includes helpful comments."""
        theme = get_theme("tech")
        css = export_to_css(theme)
        assert "/*" in css
        assert "*/" in css

    def test_css_color_variables(self):
        """Test that CSS exports color variables."""
        theme = get_theme("tech")
        css = export_to_css(theme, prefix="test")
        assert "--test-color-primary" in css

    def test_css_spacing_variables(self):
        """Test that CSS exports spacing variables."""
        theme = get_theme("tech")
        css = export_to_css(theme, prefix="test")
        assert "--test-space-" in css

    def test_css_duration_variables(self):
        """Test that CSS exports duration variables."""
        theme = get_theme("tech")
        css = export_to_css(theme, prefix="test")
        assert "--test-duration-" in css

    def test_export_utility_classes(self):
        """Test utility class export."""
        theme = get_theme("tech")
        css = export_utility_classes(theme, prefix="test")
        assert ".test-m-" in css  # Margin utilities
        assert ".test-p-" in css  # Padding utilities


class TestRemotionExporter:
    """Test Remotion TypeScript export."""

    def test_export_to_remotion_ts(self):
        """Test basic Remotion export."""
        theme = get_theme("tech")
        ts = export_to_remotion_ts(theme)
        assert ts is not None
        assert "export const" in ts

    def test_remotion_color_exports(self):
        """Test that colors are exported as constants."""
        theme = get_theme("tech")
        ts = export_to_remotion_ts(theme)
        assert "export const colorPrimary" in ts
        assert "#" in ts  # Hex colors

    def test_remotion_spacing_exports(self):
        """Test that spacing is exported."""
        theme = get_theme("tech")
        ts = export_to_remotion_ts(theme)
        assert "export const spacing" in ts

    def test_remotion_spring_exports(self):
        """Test that spring configs are exported."""
        theme = get_theme("tech")
        ts = export_to_remotion_ts(theme)
        assert "export const spring" in ts
        assert "damping:" in ts
        assert "stiffness:" in ts

    def test_remotion_includes_comments(self):
        """Test that export includes documentation comments."""
        theme = get_theme("tech")
        ts = export_to_remotion_ts(theme)
        assert "/**" in ts or "/*" in ts
        assert "Design tokens" in ts

    def test_export_spring_only(self):
        """Test export_spring_only function."""
        theme = get_theme("tech")
        ts = export_spring_only(theme)
        assert "export const spring" in ts
        assert "damping:" in ts
        # Should be springs only, no colors
        assert "colorPrimary" not in ts

    def test_remotion_duration_exports(self):
        """Test that durations are exported."""
        theme = get_theme("tech")
        ts = export_to_remotion_ts(theme)
        assert "export const duration" in ts


class TestW3CJSONExporter:
    """Test W3C Design Tokens JSON export."""

    def test_export_to_w3c_json(self):
        """Test basic W3C JSON export."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme)
        assert json_str is not None
        # Should be valid JSON
        data = json.loads(json_str)
        assert isinstance(data, dict)

    def test_w3c_json_structure(self):
        """Test that W3C JSON has correct structure."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme)
        data = json.loads(json_str)
        # Should have $type and $value fields
        if "color" in data:
            for color_name, color_data in data["color"].items():
                assert "$type" in color_data
                assert "$value" in color_data

    def test_w3c_color_tokens(self):
        """Test that colors are in W3C format."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme)
        data = json.loads(json_str)
        assert "color" in data
        # Check a color token
        if "primary" in data["color"]:
            assert data["color"]["primary"]["$type"] == "color"
            assert "#" in data["color"]["primary"]["$value"]

    def test_w3c_dimension_tokens(self):
        """Test that dimensions are in W3C format."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme)
        data = json.loads(json_str)
        assert "dimension" in data or "fontSize" in data

    def test_w3c_duration_tokens(self):
        """Test that durations are in W3C format."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme)
        data = json.loads(json_str)
        if "duration" in data:
            for duration_name, duration_data in data["duration"].items():
                assert duration_data["$type"] == "duration"

    def test_w3c_cubic_bezier_tokens(self):
        """Test that cubic bezier easings are in W3C format."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme)
        data = json.loads(json_str)
        if "cubicBezier" in data:
            for easing_name, easing_data in data["cubicBezier"].items():
                assert easing_data["$type"] == "cubicBezier"
                assert isinstance(easing_data["$value"], list)
                assert len(easing_data["$value"]) == 4

    def test_export_tokens_minimal(self):
        """Test minimal token export."""
        theme = get_theme("tech")
        json_str = export_tokens_minimal(theme)
        data = json.loads(json_str)
        assert "color" in data
        assert "dimension" in data

    def test_w3c_pretty_print(self):
        """Test pretty printing."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme, pretty=True)
        assert "\n" in json_str  # Should be formatted

    def test_w3c_compact(self):
        """Test compact output."""
        theme = get_theme("tech")
        json_str = export_to_w3c_json(theme, pretty=False)
        # Compact JSON should be shorter
        pretty_str = export_to_w3c_json(theme, pretty=True)
        assert len(json_str) < len(pretty_str)


class TestPPTXExporter:
    """Test python-pptx export helpers."""

    def test_hex_to_rgb(self):
        """Test hex to RGB conversion."""
        rgb = hex_to_rgb("#0066FF")
        assert rgb == (0, 102, 255)

    def test_hex_to_rgb_without_hash(self):
        """Test hex to RGB conversion without #."""
        rgb = hex_to_rgb("0066FF")
        assert rgb == (0, 102, 255)

    def test_hex_to_rgb_black(self):
        """Test black color conversion."""
        rgb = hex_to_rgb("#000000")
        assert rgb == (0, 0, 0)

    def test_hex_to_rgb_white(self):
        """Test white color conversion."""
        rgb = hex_to_rgb("#FFFFFF")
        assert rgb == (255, 255, 255)

    def test_export_colors(self):
        """Test color export for PPTX."""
        theme = get_theme("tech")
        colors = export_colors(theme)
        assert isinstance(colors, dict)
        # Should have semantic color names
        assert len(colors) > 0
        # Check first color is RGB tuple
        first_color = next(iter(colors.values()))
        assert isinstance(first_color, tuple)
        assert len(first_color) == 3

    def test_export_font_sizes_pt(self):
        """Test font size export in points."""
        theme = get_theme("tech")
        sizes = export_font_sizes_pt(theme)
        assert isinstance(sizes, dict)
        assert "base" in sizes
        assert isinstance(sizes["base"], float)

    def test_font_size_px_to_pt_conversion(self):
        """Test pixel to point conversion."""
        theme = get_theme("tech")
        sizes = export_font_sizes_pt(theme)
        # If base is 16px, it should convert to 12pt (16 * 0.75)
        if "px" in theme["typography"]["sizes"]["base"]:
            px_value = float(theme["typography"]["sizes"]["base"].replace("px", ""))
            expected_pt = px_value * 0.75
            assert abs(sizes["base"] - expected_pt) < 0.1

    def test_export_spacing_emu(self):
        """Test spacing export in EMUs."""
        theme = get_theme("tech")
        spacing = export_spacing_emu(theme)
        assert isinstance(spacing, dict)
        # EMUs should be integers
        for key, value in spacing.items():
            assert isinstance(value, int)

    def test_create_pptx_theme_dict(self):
        """Test complete PPTX theme dictionary creation."""
        theme = get_theme("tech")
        pptx_theme = create_pptx_theme_dict(theme)
        assert "colors_rgb" in pptx_theme
        assert "font_sizes_pt" in pptx_theme
        assert "spacing_emu" in pptx_theme
        assert "metadata" in pptx_theme
        # Verify structure
        assert isinstance(pptx_theme["colors_rgb"], dict)
        assert isinstance(pptx_theme["font_sizes_pt"], dict)
        assert isinstance(pptx_theme["spacing_emu"], dict)

    def test_pptx_theme_dict_structure(self):
        """Test PPTX theme dictionary structure."""
        theme = get_theme("tech")
        pptx_theme = create_pptx_theme_dict(theme)
        # Colors should be RGB tuples
        assert isinstance(pptx_theme["colors_rgb"], dict)
        if len(pptx_theme["colors_rgb"]) > 0:
            first_color = next(iter(pptx_theme["colors_rgb"].values()))
            assert isinstance(first_color, tuple)
            assert len(first_color) == 3
        # Font sizes should be floats
        assert isinstance(pptx_theme["font_sizes_pt"], dict)
        if len(pptx_theme["font_sizes_pt"]) > 0:
            first_size = next(iter(pptx_theme["font_sizes_pt"].values()))
            assert isinstance(first_size, float)
        # Spacing should be integers
        assert isinstance(pptx_theme["spacing_emu"], dict)
        if len(pptx_theme["spacing_emu"]) > 0:
            first_spacing = next(iter(pptx_theme["spacing_emu"].values()))
            assert isinstance(first_spacing, int)


class TestExporterIntegration:
    """Integration tests for exporters."""

    def test_all_themes_export_to_canva(self):
        """Test that all themes can export to Canva."""
        from chuk_design_system.themes import THEMES

        for theme_name in THEMES.keys():
            theme = get_theme(theme_name)
            css = export_to_canva_css(theme)
            assert css is not None
            assert len(css) > 0

    def test_all_themes_export_to_remotion(self):
        """Test that all themes can export to Remotion."""
        from chuk_design_system.themes import THEMES

        for theme_name in THEMES.keys():
            theme = get_theme(theme_name)
            ts = export_to_remotion_ts(theme)
            assert ts is not None
            assert len(ts) > 0

    def test_all_themes_export_to_w3c(self):
        """Test that all themes can export to W3C JSON."""
        from chuk_design_system.themes import THEMES

        for theme_name in THEMES.keys():
            theme = get_theme(theme_name)
            json_str = export_to_w3c_json(theme)
            # Should be valid JSON
            data = json.loads(json_str)
            assert isinstance(data, dict)

    def test_export_output_differs_by_theme(self):
        """Test that different themes produce different exports."""
        tech = get_theme("tech")
        finance = get_theme("finance")

        tech_css = export_to_canva_css(tech)
        finance_css = export_to_canva_css(finance)

        assert tech_css != finance_css
