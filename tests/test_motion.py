"""Comprehensive tests for motion token system."""

import pytest
from chuk_design_system.tokens.motion import (
    MotionTokens,
    DURATIONS,
    EASINGS,
    SPRINGS,
    ENTER_TRANSITIONS,
    EXIT_TRANSITIONS,
    create_duration,
)


class TestDurations:
    """Test duration tokens."""

    def test_durations_exist(self):
        """Test that durations are defined."""
        assert DURATIONS is not None
        assert isinstance(DURATIONS, dict)

    def test_required_durations(self):
        """Test that standard durations exist."""
        required = ["instant", "fast", "normal", "slow"]
        for duration in required:
            assert duration in DURATIONS

    def test_duration_structure(self):
        """Test that each duration has required fields."""
        for name, duration in DURATIONS.items():
            assert duration.ms is not None
            assert duration.frames_30fps is not None
            assert duration.frames_60fps is not None
            assert duration.seconds is not None
            assert duration.css is not None
            assert duration.description is not None

    def test_duration_instant(self):
        """Test that instant duration is 0."""
        assert DURATIONS["instant"].ms == 0
        assert DURATIONS["instant"].frames_30fps == 0
        assert DURATIONS["instant"].seconds == 0.0

    def test_duration_progression(self):
        """Test that durations increase properly."""
        assert DURATIONS["fastest"].ms < DURATIONS["fast"].ms
        assert DURATIONS["fast"].ms < DURATIONS["normal"].ms
        assert DURATIONS["normal"].ms < DURATIONS["slow"].ms

    def test_duration_frame_conversion(self):
        """Test frame conversion for 30fps."""
        # 300ms at 30fps should be 9 frames (300/1000 * 30)
        normal = DURATIONS["normal"]
        assert normal.ms == 300
        assert normal.frames_30fps == 9

    def test_duration_60fps_double_30fps(self):
        """Test that 60fps is roughly double 30fps."""
        for name, duration in DURATIONS.items():
            if duration.ms > 0:
                ratio = duration.frames_60fps / duration.frames_30fps
                assert 1.7 <= ratio <= 2.3  # Allow for rounding

    def test_duration_css_format(self):
        """Test that CSS duration is properly formatted."""
        for name, duration in DURATIONS.items():
            assert duration.css.endswith("ms")
            assert str(duration.ms) in duration.css

    def test_create_duration_helper(self):
        """Test create_duration helper function."""
        duration = create_duration(500, "Test duration")
        assert duration.ms == 500
        assert duration.seconds == 0.5
        assert duration.css == "500ms"
        assert duration.description == "Test duration"


class TestEasings:
    """Test easing curve definitions."""

    def test_easings_exist(self):
        """Test that easings are defined."""
        assert EASINGS is not None
        assert isinstance(EASINGS, dict)

    def test_required_easings(self):
        """Test that standard easings exist."""
        required = ["linear", "ease", "ease_in", "ease_out", "ease_in_out"]
        for easing in required:
            assert easing in EASINGS

    def test_easing_structure(self):
        """Test that each easing has required fields."""
        for name, easing in EASINGS.items():
            assert easing.curve is not None
            assert len(easing.curve) == 4  # Cubic bezier has 4 values
            assert easing.css is not None
            assert easing.description is not None
            assert easing.usage is not None

    def test_linear_easing(self):
        """Test that linear easing is correct."""
        linear = EASINGS["linear"]
        assert linear.curve == [0.0, 0.0, 1.0, 1.0]
        assert "linear" in linear.css or "0.0, 0.0, 1.0, 1.0" in linear.css

    def test_cubic_bezier_values(self):
        """Test that cubic bezier values are in valid range."""
        for name, easing in EASINGS.items():
            for value in easing.curve:
                # Y values can be outside 0-1 for bounce effects
                assert -2.0 <= value <= 2.0

    def test_easing_css_format(self):
        """Test that CSS easing is properly formatted."""
        for name, easing in EASINGS.items():
            assert "cubic-bezier" in easing.css


class TestSprings:
    """Test spring animation configurations."""

    def test_springs_exist(self):
        """Test that springs are defined."""
        assert SPRINGS is not None
        assert isinstance(SPRINGS, dict)

    def test_required_springs(self):
        """Test that standard springs exist."""
        required = ["gentle", "smooth", "bouncy", "snappy", "stiff"]
        for spring in required:
            assert spring in SPRINGS

    def test_spring_structure(self):
        """Test that each spring has required fields."""
        for name, spring in SPRINGS.items():
            assert spring.damping is not None
            assert spring.mass is not None
            assert spring.stiffness is not None
            assert hasattr(spring, "overshootClamping")
            assert spring.description is not None
            assert spring.feel is not None
            assert spring.usage is not None

    def test_spring_values_are_positive(self):
        """Test that spring values are positive."""
        for name, spring in SPRINGS.items():
            assert spring.damping > 0
            assert spring.mass > 0
            assert spring.stiffness > 0

    def test_spring_remotion_compatibility(self):
        """Test that spring configs are Remotion-compatible."""
        # Remotion expects these specific fields
        for name, spring in SPRINGS.items():
            assert hasattr(spring, "damping")
            assert hasattr(spring, "mass")
            assert hasattr(spring, "stiffness")
            assert hasattr(spring, "overshootClamping")

    def test_spring_stiffness_progression(self):
        """Test that stiffness increases from gentle to stiff."""
        assert SPRINGS["gentle"].stiffness < SPRINGS["smooth"].stiffness
        assert SPRINGS["smooth"].stiffness < SPRINGS["stiff"].stiffness


class TestEnterTransitions:
    """Test enter transition presets."""

    def test_enter_transitions_exist(self):
        """Test that enter transitions are defined."""
        assert ENTER_TRANSITIONS is not None
        assert isinstance(ENTER_TRANSITIONS, dict)

    def test_required_enter_transitions(self):
        """Test that standard enter transitions exist."""
        required = ["fade_in", "slide_in_up", "scale_in"]
        for transition in required:
            assert transition in ENTER_TRANSITIONS

    def test_enter_transition_structure(self):
        """Test that each transition has required fields."""
        for name, transition in ENTER_TRANSITIONS.items():
            assert transition.properties is not None
            assert transition.description is not None
            assert transition.usage is not None
            assert transition.default_duration is not None
            assert transition.default_easing is not None

    def test_fade_in_properties(self):
        """Test fade_in transition properties."""
        fade_in = ENTER_TRANSITIONS["fade_in"]
        assert "opacity" in fade_in.properties
        assert fade_in.properties["opacity"]["from"] == 0
        assert fade_in.properties["opacity"]["to"] == 1

    def test_slide_transitions_have_transform(self):
        """Test that slide transitions include transform properties."""
        slide_up = ENTER_TRANSITIONS["slide_in_up"]
        assert "translateY" in slide_up.properties or "transform" in slide_up.properties

    def test_transition_defaults_are_valid(self):
        """Test that default durations and easings exist."""
        for name, transition in ENTER_TRANSITIONS.items():
            # Duration should be a valid duration name
            assert transition.default_duration in DURATIONS
            # Easing should be a valid easing name
            assert transition.default_easing in EASINGS


class TestExitTransitions:
    """Test exit transition presets."""

    def test_exit_transitions_exist(self):
        """Test that exit transitions are defined."""
        assert EXIT_TRANSITIONS is not None
        assert isinstance(EXIT_TRANSITIONS, dict)

    def test_required_exit_transitions(self):
        """Test that standard exit transitions exist."""
        required = ["fade_out", "slide_out_up", "scale_out"]
        for transition in required:
            assert transition in EXIT_TRANSITIONS

    def test_exit_transition_structure(self):
        """Test that each transition has required fields."""
        for name, transition in EXIT_TRANSITIONS.items():
            assert transition.properties is not None
            assert transition.description is not None
            assert transition.usage is not None
            assert transition.default_duration is not None
            assert transition.default_easing is not None

    def test_fade_out_properties(self):
        """Test fade_out transition properties."""
        fade_out = EXIT_TRANSITIONS["fade_out"]
        assert "opacity" in fade_out.properties
        assert fade_out.properties["opacity"]["from"] == 1
        assert fade_out.properties["opacity"]["to"] == 0


class TestMotionTokens:
    """Test MotionTokens class."""

    def test_motion_tokens_init(self):
        """Test MotionTokens initialization."""
        tokens = MotionTokens()
        assert tokens.durations is not None
        assert tokens.easings is not None
        assert tokens.springs is not None
        assert tokens.enter_transitions is not None
        assert tokens.exit_transitions is not None

    def test_get_duration_ms(self):
        """Test get_duration_ms method."""
        tokens = MotionTokens()
        duration_ms = tokens.get_duration_ms("normal")
        assert duration_ms == 300

    def test_get_duration_ms_invalid(self):
        """Test error handling for invalid duration."""
        tokens = MotionTokens()
        with pytest.raises(ValueError, match="Unknown duration"):
            tokens.get_duration_ms("nonexistent")

    def test_get_duration_frames_30fps(self):
        """Test get_duration_frames for 30fps."""
        tokens = MotionTokens()
        frames = tokens.get_duration_frames("normal", 30)
        assert frames == 9  # 300ms at 30fps

    def test_get_duration_frames_60fps(self):
        """Test get_duration_frames for 60fps."""
        tokens = MotionTokens()
        frames = tokens.get_duration_frames("normal", 60)
        assert frames == 18  # 300ms at 60fps

    def test_get_duration_frames_invalid(self):
        """Test error handling for invalid duration in frames."""
        tokens = MotionTokens()
        with pytest.raises(ValueError, match="Unknown duration"):
            tokens.get_duration_frames("nonexistent", 30)

    def test_get_easing_curve(self):
        """Test get_easing_curve method."""
        tokens = MotionTokens()
        curve = tokens.get_easing_curve("linear")
        assert curve == [0.0, 0.0, 1.0, 1.0]

    def test_get_easing_curve_invalid(self):
        """Test error handling for invalid easing."""
        tokens = MotionTokens()
        with pytest.raises(ValueError, match="Unknown easing"):
            tokens.get_easing_curve("nonexistent")

    def test_get_spring_config(self):
        """Test get_spring_config method."""
        tokens = MotionTokens()
        config = tokens.get_spring_config("smooth")
        assert "damping" in config
        assert "mass" in config
        assert "stiffness" in config
        assert "overshootClamping" in config
        assert config["damping"] == 22
        assert config["mass"] == 1
        assert config["stiffness"] == 150

    def test_get_spring_config_invalid(self):
        """Test error handling for invalid spring."""
        tokens = MotionTokens()
        with pytest.raises(ValueError, match="Unknown spring"):
            tokens.get_spring_config("nonexistent")

    def test_get_all(self):
        """Test get_all method."""
        tokens = MotionTokens()
        all_tokens = tokens.get_all()
        assert "durations" in all_tokens
        assert "easings" in all_tokens
        assert "springs" in all_tokens
        assert "enterTransitions" in all_tokens
        assert "exitTransitions" in all_tokens

    def test_get_all_returns_serializable(self):
        """Test that get_all returns JSON-serializable dict."""
        tokens = MotionTokens()
        all_tokens = tokens.get_all()
        import json

        # Should not raise
        json.dumps(all_tokens)

    def test_all_durations_accessible(self):
        """Test that all durations can be accessed."""
        tokens = MotionTokens()
        for duration_name in DURATIONS.keys():
            ms = tokens.get_duration_ms(duration_name)
            assert ms >= 0

    def test_all_easings_accessible(self):
        """Test that all easings can be accessed."""
        tokens = MotionTokens()
        for easing_name in EASINGS.keys():
            curve = tokens.get_easing_curve(easing_name)
            assert len(curve) == 4

    def test_all_springs_accessible(self):
        """Test that all springs can be accessed."""
        tokens = MotionTokens()
        for spring_name in SPRINGS.keys():
            config = tokens.get_spring_config(spring_name)
            assert config is not None
