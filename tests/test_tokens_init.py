"""Tests for tokens/__init__.py module."""

from chuk_design_system.tokens import get_all_tokens


class TestGetAllTokens:
    """Test the get_all_tokens function."""

    def test_get_all_tokens_default(self):
        """Test getting all tokens with default parameters."""
        tokens = get_all_tokens()
        assert "colors" in tokens
        assert "typography" in tokens
        assert "spacing" in tokens
        assert "motion" in tokens

    def test_get_all_tokens_custom_params(self):
        """Test getting all tokens with custom parameters."""
        tokens = get_all_tokens(primary_hue="purple", mode="light", medium="video_1080p")
        assert "colors" in tokens
        assert "typography" in tokens
        # Verify custom params were applied
        assert isinstance(tokens["colors"], dict)
        assert isinstance(tokens["typography"], dict)

    def test_get_all_tokens_structure(self):
        """Test that get_all_tokens returns correct structure."""
        tokens = get_all_tokens()
        # Colors should have palette, semantic, gradients
        assert "palette" in tokens["colors"]
        assert "semantic" in tokens["colors"]
        assert "gradients" in tokens["colors"]

        # Typography should have families, sizes, etc.
        assert "families" in tokens["typography"]
        assert "sizes" in tokens["typography"]

        # Spacing should have spacing, safe_areas, etc.
        assert "spacing" in tokens["spacing"]
        assert "safeAreas" in tokens["spacing"]

        # Motion should have durations, easings, etc.
        assert "durations" in tokens["motion"]
        assert "easings" in tokens["motion"]

    def test_get_all_tokens_different_hues(self):
        """Test that different hues produce different colors."""
        blue_tokens = get_all_tokens(primary_hue="blue")
        green_tokens = get_all_tokens(primary_hue="green")

        assert (
            blue_tokens["colors"]["semantic"]["primary"]["DEFAULT"]
            != green_tokens["colors"]["semantic"]["primary"]["DEFAULT"]
        )

    def test_get_all_tokens_different_modes(self):
        """Test that different modes produce different colors."""
        dark_tokens = get_all_tokens(mode="dark")
        light_tokens = get_all_tokens(mode="light")

        assert (
            dark_tokens["colors"]["semantic"]["background"]["DEFAULT"]
            != light_tokens["colors"]["semantic"]["background"]["DEFAULT"]
        )

    def test_get_all_tokens_different_mediums(self):
        """Test that different mediums produce different typography."""
        web_tokens = get_all_tokens(medium="web")
        video_tokens = get_all_tokens(medium="video_1080p")

        assert (
            web_tokens["typography"]["sizes"]["base"] != video_tokens["typography"]["sizes"]["base"]
        )
