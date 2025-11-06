"""Comprehensive tests for spacing token system."""

import pytest
from chuk_design_system.tokens.spacing import (
    SpacingTokens,
    SPACING,
    SPACING_TSHIRT,
    MARGINS,
    PADDING,
    GAPS,
    RADIUS,
    BORDER_WIDTH,
    SAFE_AREAS,
    GRID,
    CONTAINERS,
    ASPECT_RATIOS,
    Z_INDEX,
)


class TestSpacing:
    """Test spacing scale."""

    def test_spacing_exists(self):
        """Test that spacing scale is defined."""
        assert SPACING is not None
        assert isinstance(SPACING, dict)

    def test_spacing_unit_system(self):
        """Test 8px base unit system (Canva-compatible)."""
        assert SPACING["1u"] == "8px"
        assert SPACING["2u"] == "16px"
        assert SPACING["0.5u"] == "4px"

    def test_spacing_values_are_pixels(self):
        """Test that spacing values are in pixels."""
        for key, value in SPACING.items():
            assert value.endswith("px") or value == "0px"

    def test_spacing_progression(self):
        """Test that spacing increases properly."""

        # Extract numeric values for comparison
        def extract_px(value):
            return int(value.replace("px", ""))

        assert extract_px(SPACING["0.5u"]) < extract_px(SPACING["1u"]) < extract_px(SPACING["2u"])

    def test_spacing_tshirt_mapping(self):
        """Test t-shirt size mapping."""
        assert SPACING_TSHIRT["sm"] == SPACING["1u"]
        assert SPACING_TSHIRT["md"] == SPACING["2u"]
        assert SPACING_TSHIRT["lg"] == SPACING["3u"]


class TestLayoutDimensions:
    """Test layout dimension tokens."""

    def test_margins_exist(self):
        """Test that margins are defined."""
        assert MARGINS is not None
        assert "page" in MARGINS
        assert "section" in MARGINS

    def test_padding_exist(self):
        """Test that padding is defined."""
        assert PADDING is not None
        assert "normal" in PADDING

    def test_gaps_exist(self):
        """Test that gaps are defined."""
        assert GAPS is not None
        assert "normal" in GAPS


class TestBorderRadius:
    """Test border radius scale."""

    def test_radius_exists(self):
        """Test that radius is defined."""
        assert RADIUS is not None
        assert isinstance(RADIUS, dict)

    def test_radius_has_none_and_full(self):
        """Test that radius has none and full."""
        assert RADIUS["none"] == "0"
        assert RADIUS["full"] == "9999px"

    def test_radius_progression(self):
        """Test that radius increases."""
        sm_val = int(RADIUS["sm"].replace("px", ""))
        md_val = int(RADIUS["md"].replace("px", ""))
        lg_val = int(RADIUS["lg"].replace("px", ""))
        assert sm_val < md_val < lg_val


class TestBorderWidth:
    """Test border width scale."""

    def test_border_width_exists(self):
        """Test that border width is defined."""
        assert BORDER_WIDTH is not None
        assert isinstance(BORDER_WIDTH, dict)

    def test_border_width_values(self):
        """Test that border widths are valid."""
        assert BORDER_WIDTH["none"] == "0"
        assert "px" in BORDER_WIDTH["thin"]


class TestSafeAreas:
    """Test platform-specific safe areas."""

    def test_safe_areas_exist(self):
        """Test that safe areas are defined."""
        assert SAFE_AREAS is not None
        assert isinstance(SAFE_AREAS, dict)

    def test_platform_safe_areas(self):
        """Test that platform-specific safe areas exist."""
        platforms = ["youtube_shorts", "tiktok", "instagram_story", "instagram_reel"]
        for platform in platforms:
            assert platform in SAFE_AREAS

    def test_safe_area_structure(self):
        """Test that each safe area has required fields."""
        for platform, safe_area in SAFE_AREAS.items():
            assert safe_area.top is not None
            assert safe_area.bottom is not None
            assert safe_area.left is not None
            assert safe_area.right is not None
            assert safe_area.description is not None
            assert safe_area.aspect_ratio is not None

    def test_vertical_video_safe_areas(self):
        """Test that vertical video safe areas are 9:16."""
        assert SAFE_AREAS["youtube_shorts"].aspect_ratio == "9:16"
        assert SAFE_AREAS["tiktok"].aspect_ratio == "9:16"
        assert SAFE_AREAS["instagram_story"].aspect_ratio == "9:16"

    def test_horizontal_video_safe_areas(self):
        """Test that horizontal video safe areas are 16:9."""
        assert SAFE_AREAS["youtube_landscape"].aspect_ratio == "16:9"

    def test_none_safe_area(self):
        """Test that none safe area has zero padding."""
        none_safe = SAFE_AREAS["none"]
        assert none_safe.top == 0
        assert none_safe.bottom == 0
        assert none_safe.left == 0
        assert none_safe.right == 0


class TestGrid:
    """Test grid system configurations."""

    def test_grid_exists(self):
        """Test that grid configurations exist."""
        assert GRID is not None
        assert isinstance(GRID, dict)

    def test_grid_configurations(self):
        """Test that standard grid configurations exist."""
        assert "12_column" in GRID
        assert "8_column" in GRID
        assert "4_column" in GRID

    def test_grid_structure(self):
        """Test that each grid has required fields."""
        for name, grid in GRID.items():
            assert grid.columns > 0
            assert grid.gap is not None
            assert grid.margin is not None

    def test_12_column_grid(self):
        """Test 12-column grid configuration."""
        grid = GRID["12_column"]
        assert grid.columns == 12


class TestContainers:
    """Test container widths."""

    def test_containers_exist(self):
        """Test that container widths are defined."""
        assert CONTAINERS is not None
        assert isinstance(CONTAINERS, dict)

    def test_container_sizes(self):
        """Test that standard container sizes exist."""
        sizes = ["sm", "md", "lg", "xl", "2xl", "full"]
        for size in sizes:
            assert size in CONTAINERS

    def test_container_full_width(self):
        """Test that full container is 100%."""
        assert CONTAINERS["full"] == "100%"

    def test_container_progression(self):
        """Test that containers increase in size."""
        sm = int(CONTAINERS["sm"].replace("px", ""))
        md = int(CONTAINERS["md"].replace("px", ""))
        lg = int(CONTAINERS["lg"].replace("px", ""))
        assert sm < md < lg


class TestAspectRatios:
    """Test aspect ratio definitions."""

    def test_aspect_ratios_exist(self):
        """Test that aspect ratios are defined."""
        assert ASPECT_RATIOS is not None
        assert isinstance(ASPECT_RATIOS, dict)

    def test_common_aspect_ratios(self):
        """Test that common aspect ratios exist."""
        assert ASPECT_RATIOS["square"] == "1:1"
        assert ASPECT_RATIOS["video"] == "16:9"
        assert ASPECT_RATIOS["portrait"] == "9:16"

    def test_aspect_ratio_format(self):
        """Test that aspect ratios are in correct format."""
        for name, ratio in ASPECT_RATIOS.items():
            assert ":" in ratio


class TestZIndex:
    """Test z-index layering."""

    def test_z_index_exists(self):
        """Test that z-index is defined."""
        assert Z_INDEX is not None
        assert isinstance(Z_INDEX, dict)

    def test_z_index_layering(self):
        """Test that z-index values layer correctly."""
        assert Z_INDEX["base"] < Z_INDEX["dropdown"]
        assert Z_INDEX["dropdown"] < Z_INDEX["modal"]
        assert Z_INDEX["modal"] < Z_INDEX["tooltip"]

    def test_z_index_values_are_integers(self):
        """Test that z-index values are integers."""
        for name, value in Z_INDEX.items():
            assert isinstance(value, int)


class TestSpacingTokens:
    """Test SpacingTokens class."""

    def test_spacing_tokens_init(self):
        """Test SpacingTokens initialization."""
        tokens = SpacingTokens()
        assert tokens.spacing is not None
        assert tokens.spacing_tshirt is not None
        assert tokens.margins is not None
        assert tokens.padding is not None
        assert tokens.gaps is not None
        assert tokens.radius is not None
        assert tokens.border_width is not None
        assert tokens.safe_areas is not None
        assert tokens.grid is not None
        assert tokens.containers is not None
        assert tokens.aspect_ratios is not None
        assert tokens.z_index is not None

    def test_get_safe_area(self):
        """Test get_safe_area method."""
        tokens = SpacingTokens()
        safe_area = tokens.get_safe_area("youtube_shorts")
        assert safe_area is not None
        assert safe_area.aspect_ratio == "9:16"

    def test_get_safe_area_invalid(self):
        """Test error handling for invalid platform."""
        tokens = SpacingTokens()
        with pytest.raises(ValueError, match="Unknown platform"):
            tokens.get_safe_area("nonexistent")

    def test_get_grid(self):
        """Test get_grid method."""
        tokens = SpacingTokens()
        grid = tokens.get_grid(12)
        assert grid is not None
        assert grid.columns == 12

    def test_get_grid_invalid(self):
        """Test error handling for invalid grid."""
        tokens = SpacingTokens()
        with pytest.raises(ValueError, match="Unknown grid"):
            tokens.get_grid(99)

    def test_get_all(self):
        """Test get_all method."""
        tokens = SpacingTokens()
        all_tokens = tokens.get_all()
        assert "spacing" in all_tokens
        assert "spacingTshirt" in all_tokens
        assert "margins" in all_tokens
        assert "padding" in all_tokens
        assert "gaps" in all_tokens
        assert "radius" in all_tokens
        assert "borderWidth" in all_tokens
        assert "safeAreas" in all_tokens
        assert "grid" in all_tokens
        assert "containers" in all_tokens
        assert "aspectRatios" in all_tokens
        assert "zIndex" in all_tokens

    def test_get_all_returns_serializable(self):
        """Test that get_all returns JSON-serializable dict."""
        tokens = SpacingTokens()
        all_tokens = tokens.get_all()
        import json

        # Should not raise
        json.dumps(all_tokens)

    def test_safe_areas_serialization(self):
        """Test that safe areas are properly serialized."""
        tokens = SpacingTokens()
        all_tokens = tokens.get_all()
        safe_areas = all_tokens["safeAreas"]
        assert isinstance(safe_areas, dict)
        assert "youtube_shorts" in safe_areas
        assert isinstance(safe_areas["youtube_shorts"], dict)
