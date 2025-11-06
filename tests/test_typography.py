"""Comprehensive tests for typography token system."""

import pytest
from chuk_design_system.tokens.typography import (
    TypographyTokens,
    FONT_FAMILIES,
    FONT_SIZES,
    FONT_WEIGHTS,
    LINE_HEIGHTS,
    LETTER_SPACING,
    TEXT_STYLES,
    TYPOGRAPHY_SCALE,
)


class TestFontFamilies:
    """Test font family definitions."""

    def test_font_families_exist(self):
        """Test that font families are defined."""
        assert FONT_FAMILIES is not None
        assert isinstance(FONT_FAMILIES, dict)

    def test_required_font_families(self):
        """Test that required font families exist."""
        required = ["display", "body", "mono", "decorative"]
        for family in required:
            assert family in FONT_FAMILIES

    def test_font_family_structure(self):
        """Test that each font family has required fields."""
        for name, family in FONT_FAMILIES.items():
            assert family.name is not None
            assert family.fonts is not None
            assert isinstance(family.fonts, list)
            assert len(family.fonts) > 0
            assert family.description is not None
            assert family.usage is not None


class TestFontSizes:
    """Test font size scales."""

    def test_font_sizes_exist(self):
        """Test that font sizes dictionary exists."""
        assert FONT_SIZES is not None
        assert isinstance(FONT_SIZES, dict)

    def test_required_size_scales(self):
        """Test that all required size scales exist."""
        required_scales = ["web", "pptx", "video_1080p", "video_4k"]
        for scale in required_scales:
            assert scale in FONT_SIZES

    def test_size_scale_completeness(self):
        """Test that each scale has all size variants."""
        required_sizes = ["xs", "sm", "base", "lg", "xl", "xxl", "xxxl", "xxxxl"]
        for scale_name, scale in FONT_SIZES.items():
            for size in required_sizes:
                # Check using both attribute and alias access
                assert hasattr(scale, size) or hasattr(scale, size.replace("x", ""))

    def test_video_sizes_larger_than_web(self):
        """Test that video sizes are larger than web sizes."""
        web_base = FONT_SIZES["web"].base
        video_base = FONT_SIZES["video_1080p"].base

        # Extract numeric values
        web_value = int(web_base.replace("px", ""))
        video_value = int(video_base.replace("px", ""))

        assert video_value > web_value

    def test_4k_sizes_larger_than_1080p(self):
        """Test that 4K sizes are larger than 1080p sizes."""
        hd_base = FONT_SIZES["video_1080p"].base
        uhd_base = FONT_SIZES["video_4k"].base

        hd_value = int(hd_base.replace("px", ""))
        uhd_value = int(uhd_base.replace("px", ""))

        assert uhd_value > hd_value


class TestFontWeights:
    """Test font weight scale."""

    def test_font_weights_exist(self):
        """Test that font weights are defined."""
        assert FONT_WEIGHTS is not None
        assert isinstance(FONT_WEIGHTS, dict)

    def test_weight_range(self):
        """Test that weights are in valid range."""
        for name, weight in FONT_WEIGHTS.items():
            assert 100 <= weight <= 900
            assert weight % 100 == 0

    def test_required_weights(self):
        """Test that standard weights exist."""
        required = ["regular", "medium", "semibold", "bold"]
        for weight in required:
            assert weight in FONT_WEIGHTS

    def test_weight_progression(self):
        """Test that weights increase properly."""
        assert FONT_WEIGHTS["thin"] < FONT_WEIGHTS["regular"]
        assert FONT_WEIGHTS["regular"] < FONT_WEIGHTS["bold"]
        assert FONT_WEIGHTS["bold"] < FONT_WEIGHTS["black"]


class TestLineHeights:
    """Test line height scale."""

    def test_line_heights_exist(self):
        """Test that line heights are defined."""
        assert LINE_HEIGHTS is not None
        assert isinstance(LINE_HEIGHTS, dict)

    def test_line_height_values(self):
        """Test that line heights are reasonable."""
        for name, height in LINE_HEIGHTS.items():
            assert 1.0 <= height <= 2.5

    def test_line_height_progression(self):
        """Test that line heights increase."""
        assert LINE_HEIGHTS["tight"] < LINE_HEIGHTS["normal"]
        assert LINE_HEIGHTS["normal"] < LINE_HEIGHTS["loose"]


class TestLetterSpacing:
    """Test letter spacing scale."""

    def test_letter_spacing_exists(self):
        """Test that letter spacing is defined."""
        assert LETTER_SPACING is not None
        assert isinstance(LETTER_SPACING, dict)

    def test_letter_spacing_format(self):
        """Test that letter spacing values are valid."""
        for name, spacing in LETTER_SPACING.items():
            assert "em" in spacing or spacing == "0"


class TestTextStyles:
    """Test text style presets."""

    def test_text_styles_exist(self):
        """Test that text styles are defined."""
        assert TEXT_STYLES is not None
        assert isinstance(TEXT_STYLES, dict)

    def test_required_text_styles(self):
        """Test that standard text styles exist."""
        required = ["hero_title", "title", "heading", "body", "caption"]
        for style in required:
            assert style in TEXT_STYLES

    def test_text_style_structure(self):
        """Test that each text style has required fields."""
        for name, style in TEXT_STYLES.items():
            assert style.name is not None
            assert style.fontSize is not None
            assert style.fontWeight is not None
            assert style.lineHeight is not None
            assert style.letterSpacing is not None
            assert style.fontFamily is not None

    def test_heading_hierarchy(self):
        """Test that heading sizes follow hierarchy."""
        # Hero should be largest
        assert TEXT_STYLES["hero_title"].fontSize == "4xl"
        assert TEXT_STYLES["title"].fontSize == "3xl"


class TestTypographyScale:
    """Test typography scale mapping."""

    def test_typography_scale_exists(self):
        """Test that typography scale mapping exists."""
        assert TYPOGRAPHY_SCALE is not None
        assert isinstance(TYPOGRAPHY_SCALE, dict)

    def test_scale_canva_compatibility(self):
        """Test Canva-compatible naming."""
        # Should have semantic names
        assert "title_large" in TYPOGRAPHY_SCALE
        assert "body_medium" in TYPOGRAPHY_SCALE


class TestTypographyTokens:
    """Test TypographyTokens class."""

    def test_typography_tokens_init(self):
        """Test TypographyTokens initialization."""
        tokens = TypographyTokens()
        assert tokens.families is not None
        assert tokens.sizes is not None
        assert tokens.weights is not None
        assert tokens.line_heights is not None
        assert tokens.letter_spacing is not None
        assert tokens.text_styles is not None
        assert tokens.scale is not None

    def test_get_text_style_web(self):
        """Test getting text style for web."""
        tokens = TypographyTokens()
        style = tokens.get_text_style("hero_title", "web")
        assert "fontSize" in style
        assert "fontWeight" in style
        assert "fontFamily" in style
        assert isinstance(style["fontWeight"], int)

    def test_get_text_style_video(self):
        """Test getting text style for video."""
        tokens = TypographyTokens()
        style = tokens.get_text_style("body", "video_1080p")
        assert "fontSize" in style
        # Video sizes should be larger
        assert "px" in style["fontSize"]

    def test_get_text_style_invalid(self):
        """Test error handling for invalid style."""
        tokens = TypographyTokens()
        with pytest.raises(ValueError, match="Unknown text style"):
            tokens.get_text_style("nonexistent", "web")

    def test_get_text_style_all_styles(self):
        """Test that all text styles can be resolved."""
        tokens = TypographyTokens()
        for style_name in TEXT_STYLES.keys():
            style = tokens.get_text_style(style_name, "web")
            assert style is not None
            assert "fontSize" in style

    def test_get_all_web(self):
        """Test get_all for web medium."""
        tokens = TypographyTokens()
        all_tokens = tokens.get_all("web")
        assert "families" in all_tokens
        assert "sizes" in all_tokens
        assert "weights" in all_tokens
        assert "lineHeights" in all_tokens
        assert "letterSpacing" in all_tokens
        assert "textStyles" in all_tokens
        assert "scale" in all_tokens

    def test_get_all_pptx(self):
        """Test get_all for pptx medium."""
        tokens = TypographyTokens()
        all_tokens = tokens.get_all("pptx")
        # Should have pt values
        assert "pt" in all_tokens["sizes"]["base"]

    def test_get_all_returns_serializable(self):
        """Test that get_all returns JSON-serializable dict."""
        tokens = TypographyTokens()
        all_tokens = tokens.get_all("web")
        import json

        # Should not raise
        json.dumps(all_tokens)

    def test_different_mediums_different_sizes(self):
        """Test that different mediums have different font sizes."""
        tokens = TypographyTokens()
        web = tokens.get_all("web")
        video = tokens.get_all("video_1080p")
        assert web["sizes"]["base"] != video["sizes"]["base"]
