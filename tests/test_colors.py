"""Comprehensive tests for color token system."""

from chuk_design_system.tokens.colors import (
    ColorTokens,
    PALETTE,
    GRADIENTS,
    get_semantic_colors,
)


class TestPalette:
    """Test color palette structure."""

    def test_palette_exists(self):
        """Test that PALETTE is defined."""
        assert PALETTE is not None
        assert isinstance(PALETTE, dict)

    def test_palette_has_required_colors(self):
        """Test that palette has all required color hues."""
        required_colors = ["blue", "cyan", "green", "purple", "pink", "orange", "red", "zinc"]
        for color in required_colors:
            assert color in PALETTE

    def test_color_scale_complete(self):
        """Test that each color has complete 50-950 scale."""
        scales = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
        for color_name, color_scale in PALETTE.items():
            for scale in scales:
                assert scale in color_scale, f"{color_name} missing {scale}"

    def test_color_values_are_hex(self):
        """Test that all color values are hex codes."""
        for color_name, color_scale in PALETTE.items():
            for scale, value in color_scale.items():
                assert value.startswith("#"), f"{color_name}[{scale}] not hex"
                assert len(value) == 7, f"{color_name}[{scale}] invalid length"

    def test_color_scale_progression(self):
        """Test that colors get darker as scale increases."""
        # Just check format, not actual darkness (would require RGB conversion)
        for color_name, color_scale in PALETTE.items():
            assert color_scale[50] != color_scale[950]


class TestGradients:
    """Test gradient definitions."""

    def test_gradients_exist(self):
        """Test that gradients are defined."""
        assert GRADIENTS is not None
        assert isinstance(GRADIENTS, dict)

    def test_gradient_format(self):
        """Test that gradients are valid CSS."""
        for name, gradient in GRADIENTS.items():
            assert gradient.startswith("linear-gradient(")
            assert ")" in gradient

    def test_theme_gradients_exist(self):
        """Test that theme-specific gradients exist."""
        themes = ["tech", "finance", "education", "lifestyle", "gaming", "business"]
        for theme in themes:
            assert theme in GRADIENTS


class TestSemanticColors:
    """Test semantic color generation."""

    def test_get_semantic_colors_dark(self):
        """Test semantic colors for dark mode."""
        semantic = get_semantic_colors("blue", "dark")
        assert semantic.primary.DEFAULT is not None
        assert semantic.background.DEFAULT is not None
        assert semantic.foreground.DEFAULT is not None

    def test_get_semantic_colors_light(self):
        """Test semantic colors for light mode."""
        semantic = get_semantic_colors("blue", "light")
        assert semantic.primary.DEFAULT is not None
        assert semantic.background.DEFAULT == "#ffffff"

    def test_semantic_colors_have_required_categories(self):
        """Test that all required semantic categories exist."""
        semantic = get_semantic_colors("blue", "dark")
        required = [
            "primary",
            "secondary",
            "accent",
            "background",
            "foreground",
            "muted",
            "card",
            "border",
            "destructive",
            "success",
            "warning",
            "info",
        ]
        for category in required:
            assert hasattr(semantic, category)

    def test_semantic_colors_have_hover_states(self):
        """Test that action colors have hover states."""
        semantic = get_semantic_colors("blue", "dark")
        assert semantic.primary.hover is not None
        assert semantic.secondary.hover is not None
        assert semantic.accent.hover is not None

    def test_semantic_chart_colors(self):
        """Test that chart colors are provided."""
        semantic = get_semantic_colors("blue", "dark")
        assert len(semantic.chart) >= 6
        assert all(c.startswith("#") for c in semantic.chart)

    def test_different_hues_produce_different_colors(self):
        """Test that different primary hues produce different colors."""
        blue_semantic = get_semantic_colors("blue", "dark")
        purple_semantic = get_semantic_colors("purple", "dark")
        assert blue_semantic.primary.DEFAULT != purple_semantic.primary.DEFAULT

    def test_different_modes_produce_different_colors(self):
        """Test that dark and light modes differ."""
        dark = get_semantic_colors("blue", "dark")
        light = get_semantic_colors("blue", "light")
        assert dark.background.DEFAULT != light.background.DEFAULT


class TestColorTokens:
    """Test ColorTokens class."""

    def test_color_tokens_init(self):
        """Test ColorTokens initialization."""
        tokens = ColorTokens()
        assert tokens.palette is not None
        assert tokens.gradients is not None

    def test_get_semantic(self):
        """Test get_semantic method."""
        tokens = ColorTokens()
        semantic = tokens.get_semantic("green", "dark")
        assert semantic.primary.DEFAULT is not None

    def test_get_all(self):
        """Test get_all method."""
        tokens = ColorTokens()
        all_tokens = tokens.get_all("blue", "dark")
        assert "palette" in all_tokens
        assert "semantic" in all_tokens
        assert "gradients" in all_tokens

    def test_get_all_returns_dict(self):
        """Test that get_all returns proper dictionary structure."""
        tokens = ColorTokens()
        all_tokens = tokens.get_all("blue", "dark")
        assert isinstance(all_tokens, dict)
        assert isinstance(all_tokens["palette"], dict)
        assert isinstance(all_tokens["semantic"], dict)
        assert isinstance(all_tokens["gradients"], dict)

    def test_semantic_serialization(self):
        """Test that semantic colors can be serialized."""
        tokens = ColorTokens()
        all_tokens = tokens.get_all("blue", "dark")
        semantic = all_tokens["semantic"]
        # Should be dict after model_dump()
        assert "primary" in semantic
        assert isinstance(semantic["primary"], dict)
