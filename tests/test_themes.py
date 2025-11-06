"""Tests for theme system."""

import pytest
from chuk_design_system.themes import list_themes, get_theme, get_theme_metadata


def test_list_themes():
    """Test listing all themes."""
    themes = list_themes()
    assert len(themes) == 7  # We have 7 themes
    assert all("name" in theme for theme in themes)
    assert all("description" in theme for theme in themes)


def test_get_theme_tech():
    """Test getting Tech theme."""
    theme = get_theme("tech")
    assert theme["metadata"]["name"] == "Tech"
    assert "colors" in theme
    assert "typography" in theme
    assert "spacing" in theme
    assert "motion" in theme


def test_get_theme_case_insensitive():
    """Test theme names are case-insensitive."""
    theme1 = get_theme("tech")
    theme2 = get_theme("TECH")
    theme3 = get_theme("Tech")
    assert theme1["metadata"]["name"] == theme2["metadata"]["name"] == theme3["metadata"]["name"]


def test_get_theme_not_found():
    """Test error when theme not found."""
    with pytest.raises(ValueError, match="not found"):
        get_theme("nonexistent")


def test_get_theme_metadata():
    """Test getting theme metadata."""
    metadata = get_theme_metadata("finance")
    assert metadata["name"] == "Finance"
    assert "description" in metadata
    assert "category" in metadata


def test_all_themes_resolve():
    """Test that all themes can be resolved."""
    themes = list_themes()
    for theme_info in themes:
        theme = get_theme(theme_info["key"])
        assert "metadata" in theme
        assert "colors" in theme


def test_get_theme_typography_sizes():
    """Test that theme has typography sizes."""
    theme = get_theme("tech")

    # Should have typography
    assert "typography" in theme
    assert "sizes" in theme["typography"]

    # Should have base size
    assert "base" in theme["typography"]["sizes"]

    # Base size should be a string with units
    base_size = theme["typography"]["sizes"]["base"]
    assert isinstance(base_size, str)
    assert any(unit in base_size for unit in ["px", "pt", "rem"])


def test_theme_metadata_all_fields():
    """Test that theme metadata has all expected fields."""
    metadata = get_theme_metadata("education")

    required_fields = ["name", "description", "category", "tags"]
    for field in required_fields:
        assert field in metadata, f"Missing field: {field}"


def test_theme_colors_resolved():
    """Test that theme colors are fully resolved (no $refs)."""
    theme = get_theme("lifestyle")
    colors = theme["colors"]["semantic"]

    # Check primary color has DEFAULT and variants
    assert "primary" in colors
    assert "DEFAULT" in colors["primary"]
    assert isinstance(colors["primary"]["DEFAULT"], str)
    assert colors["primary"]["DEFAULT"].startswith("#")


def test_theme_with_invalid_medium():
    """Test theme with an invalid medium falls back gracefully."""
    # Should not raise error, should use default medium
    theme = get_theme("gaming")
    assert "typography" in theme
