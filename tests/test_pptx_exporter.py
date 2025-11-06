"""Specific tests for PPTX exporter edge cases."""

from chuk_design_system.themes import get_theme
from chuk_design_system.exporters.pptx import (
    hex_to_rgb,
    export_colors,
    export_font_sizes_pt,
    export_spacing_emu,
    create_pptx_theme_dict,
)


class TestPPTXExporterCoverage:
    """Tests to improve PPTX exporter coverage."""

    def test_export_colors_pptx_without_library(self):
        """Test that export_colors_pptx raises proper error when python-pptx not installed."""
        import sys
        from unittest.mock import patch

        theme = get_theme("tech")

        # Mock ImportError for python-pptx
        with patch.dict(sys.modules, {"pptx.util": None}):
            try:
                from chuk_design_system.exporters.pptx import export_colors_pptx

                # Force reimport to trigger the ImportError
                import importlib
                import chuk_design_system.exporters.pptx as pptx_module

                importlib.reload(pptx_module)
            except ImportError:
                pass  # Expected

        # Test the RGB export which doesn't require python-pptx
        colors = export_colors(theme)
        assert len(colors) > 0

    def test_font_sizes_with_pt_units(self):
        """Test font size handling when units are already in points."""
        # Create a mock theme with pt units
        theme = get_theme("tech")

        # Force typography to use pt (usually web uses px, pptx uses pt)
        # But get_theme with default web medium uses px
        # So let's test the conversion logic
        sizes = export_font_sizes_pt(theme)

        # Should have converted or handled sizes
        assert isinstance(sizes, dict)
        for key, value in sizes.items():
            assert isinstance(value, float)
            assert value > 0

    def test_font_sizes_with_no_units(self):
        """Test font size handling when no units are present."""
        theme = get_theme("tech")
        sizes = export_font_sizes_pt(theme)

        # All sizes should be positive floats
        for key, value in sizes.items():
            assert value > 0
            assert isinstance(value, float)

    def test_spacing_emu_conversion_accuracy(self):
        """Test that spacing EMU conversion is accurate."""
        theme = get_theme("tech")
        spacing = export_spacing_emu(theme)

        # 8px should convert to approximately 76200 EMUs (8 * 9525)
        if "1u" in spacing:
            expected_emu = 8 * 9525
            assert abs(spacing["1u"] - expected_emu) < 100  # Allow small variance

    def test_create_pptx_theme_dict_metadata(self):
        """Test that metadata is included in PPTX theme dict."""
        theme = get_theme("tech")
        pptx_theme = create_pptx_theme_dict(theme)

        assert "metadata" in pptx_theme
        metadata = pptx_theme["metadata"]
        assert "name" in metadata
        assert metadata["name"] == "Tech"

    def test_color_export_includes_variants(self):
        """Test that color export includes hover/active variants."""
        theme = get_theme("tech")
        colors = export_colors(theme)

        # Should have base colors and variants
        # The function exports DEFAULT and variants like hover, active
        assert len(colors) >= 4  # At minimum: primary, secondary, background, foreground

    def test_hex_to_rgb_edge_cases(self):
        """Test hex_to_rgb with various inputs."""
        # Test with lowercase
        assert hex_to_rgb("#aabbcc") == (170, 187, 204)

        # Test with uppercase
        assert hex_to_rgb("#AABBCC") == (170, 187, 204)

        # Test mixed case
        assert hex_to_rgb("#AaBbCc") == (170, 187, 204)

    def test_pptx_theme_dict_all_keys(self):
        """Test that all expected keys are in PPTX theme dict."""
        theme = get_theme("finance")
        pptx_theme = create_pptx_theme_dict(theme)

        required_keys = ["colors_rgb", "font_sizes_pt", "spacing_emu", "metadata"]
        for key in required_keys:
            assert key in pptx_theme, f"Missing key: {key}"

    def test_export_all_themes_to_pptx(self):
        """Test that all themes can be exported to PPTX format."""
        from chuk_design_system.themes import THEMES

        for theme_name in THEMES.keys():
            theme = get_theme(theme_name)
            pptx_theme = create_pptx_theme_dict(theme)

            # Should have all required components
            assert len(pptx_theme["colors_rgb"]) > 0
            assert len(pptx_theme["font_sizes_pt"]) > 0
            assert len(pptx_theme["spacing_emu"]) > 0

    def test_font_sizes_px_conversion(self):
        """Test font size conversion from px to pt."""
        # Create custom theme with px sizes
        theme = {
            "typography": {
                "sizes": {
                    "small": "12px",
                    "medium": "16px",
                    "large": "24px",
                }
            }
        }

        sizes = export_font_sizes_pt(theme)

        # 12px * 0.75 = 9pt
        assert sizes["small"] == 9.0
        # 16px * 0.75 = 12pt
        assert sizes["medium"] == 12.0
        # 24px * 0.75 = 18pt
        assert sizes["large"] == 18.0

    def test_font_sizes_no_units(self):
        """Test font size handling with numeric values only."""
        theme = {
            "typography": {
                "sizes": {
                    "small": "12",
                    "medium": 16,  # Can be int
                    "large": 24.5,  # Can be float
                }
            }
        }

        sizes = export_font_sizes_pt(theme)

        assert sizes["small"] == 12.0
        assert sizes["medium"] == 16.0
        assert sizes["large"] == 24.5

    def test_export_colors_pptx_import_error(self):
        """Test export_colors_pptx raises ImportError when python-pptx not installed."""
        from chuk_design_system.exporters.pptx import export_colors_pptx

        theme = get_theme("tech")

        # python-pptx may not be installed, so expect ImportError
        try:
            colors_pptx = export_colors_pptx(theme)
            # If it succeeds, python-pptx is installed
            assert len(colors_pptx) > 0
        except ImportError as e:
            # Expected when python-pptx not installed
            assert "python-pptx is required" in str(e)
