"""
Motion tokens - Animation and timing system.

Optimized for video generation (Remotion) but also useful for web/presentation animations.

Includes:
- Duration tokens with frame conversions (30fps, 60fps)
- Easing curves (cubic bezier)
- Spring configurations (Remotion-compatible)
- Transition presets
"""

from typing import Any
from chuk_design_system.tokens.models import (
    DurationConfig,
    EasingConfig,
    SpringConfig,
    TransitionConfig,
)


# ============================================================================
# DURATION TOKENS
# ============================================================================


def create_duration(ms: int, description: str) -> DurationConfig:
    """Helper to create duration config with all representations."""
    return DurationConfig(
        ms=ms,
        frames_30fps=round(ms / 1000 * 30),
        frames_60fps=round(ms / 1000 * 60),
        seconds=ms / 1000,
        css=f"{ms}ms",
        description=description,
    )


DURATIONS = {
    "instant": create_duration(0, "No delay"),
    "fastest": create_duration(100, "Fastest animation"),
    "faster": create_duration(150, "Very fast animation"),
    "fast": create_duration(200, "Fast animation"),
    "normal": create_duration(300, "Normal animation speed"),
    "moderate": create_duration(400, "Moderate animation"),
    "slow": create_duration(500, "Slow animation"),
    "slower": create_duration(700, "Very slow animation"),
    "slowest": create_duration(1000, "Slowest animation"),
}


# ============================================================================
# EASING CURVES
# ============================================================================

EASINGS = {
    "linear": EasingConfig(
        curve=[0.0, 0.0, 1.0, 1.0],
        css="cubic-bezier(0.0, 0.0, 1.0, 1.0)",
        description="Linear motion, no acceleration",
        usage="Loading indicators, continuous rotation",
    ),
    "ease": EasingConfig(
        curve=[0.25, 0.1, 0.25, 1.0],
        css="cubic-bezier(0.25, 0.1, 0.25, 1.0)",
        description="Default ease, gentle acceleration and deceleration",
        usage="General purpose animations",
    ),
    "ease_in": EasingConfig(
        curve=[0.42, 0.0, 1.0, 1.0],
        css="cubic-bezier(0.42, 0.0, 1.0, 1.0)",
        description="Slow start, fast end",
        usage="Exit animations, elements leaving the screen",
    ),
    "ease_out": EasingConfig(
        curve=[0.0, 0.0, 0.58, 1.0],
        css="cubic-bezier(0.0, 0.0, 0.58, 1.0)",
        description="Fast start, slow end",
        usage="Enter animations, elements appearing",
    ),
    "ease_in_out": EasingConfig(
        curve=[0.42, 0.0, 0.58, 1.0],
        css="cubic-bezier(0.42, 0.0, 0.58, 1.0)",
        description="Slow start and end, fast middle",
        usage="Position changes, scaling",
    ),
    # Advanced easings
    "smooth": EasingConfig(
        curve=[0.4, 0.0, 0.2, 1.0],
        css="cubic-bezier(0.4, 0.0, 0.2, 1.0)",
        description="Very smooth acceleration and deceleration",
        usage="Polished UI transitions",
    ),
    "snappy": EasingConfig(
        curve=[0.4, 0.0, 0.6, 1.0],
        css="cubic-bezier(0.4, 0.0, 0.6, 1.0)",
        description="Quick, responsive feel",
        usage="Interactive elements, buttons",
    ),
    "bouncy": EasingConfig(
        curve=[0.68, -0.55, 0.265, 1.55],
        css="cubic-bezier(0.68, -0.55, 0.265, 1.55)",
        description="Bounce effect at end",
        usage="Playful animations, emphasis",
    ),
}


# ============================================================================
# SPRING CONFIGURATIONS (Remotion-compatible)
# ============================================================================

SPRINGS = {
    "gentle": SpringConfig(
        damping=26,
        mass=1,
        stiffness=120,
        overshootClamping=False,
        description="Gentle, smooth spring",
        feel="Calm and controlled",
        usage="Subtle animations, background elements",
    ),
    "smooth": SpringConfig(
        damping=22,
        mass=1,
        stiffness=150,
        overshootClamping=False,
        description="Smooth spring with slight bounce",
        feel="Natural and fluid",
        usage="General purpose spring animations",
    ),
    "bouncy": SpringConfig(
        damping=10,
        mass=1,
        stiffness=200,
        overshootClamping=False,
        description="Bouncy spring with overshoot",
        feel="Energetic and playful",
        usage="Playful elements, emphasis",
    ),
    "snappy": SpringConfig(
        damping=20,
        mass=0.5,
        stiffness=300,
        overshootClamping=False,
        description="Quick, snappy spring",
        feel="Fast and responsive",
        usage="Interactive UI, quick transitions",
    ),
    "stiff": SpringConfig(
        damping=30,
        mass=1,
        stiffness=400,
        overshootClamping=True,
        description="Stiff spring, no overshoot",
        feel="Mechanical and precise",
        usage="Precise movements, technical content",
    ),
}


# ============================================================================
# TRANSITION PRESETS
# ============================================================================

# Enter transitions
ENTER_TRANSITIONS = {
    "fade_in": TransitionConfig(
        properties={
            "opacity": {"from": 0, "to": 1},
        },
        description="Simple fade in",
        usage="General purpose enter animation",
        default_duration="normal",
        default_easing="ease_out",
    ),
    "slide_in_up": TransitionConfig(
        properties={
            "opacity": {"from": 0, "to": 1},
            "translateY": {"from": "40px", "to": "0px"},
        },
        description="Slide in from bottom with fade",
        usage="Content appearing from below",
        default_duration="normal",
        default_easing="ease_out",
    ),
    "slide_in_down": TransitionConfig(
        properties={
            "opacity": {"from": 0, "to": 1},
            "translateY": {"from": "-40px", "to": "0px"},
        },
        description="Slide in from top with fade",
        usage="Headers, titles appearing",
        default_duration="normal",
        default_easing="ease_out",
    ),
    "scale_in": TransitionConfig(
        properties={
            "opacity": {"from": 0, "to": 1},
            "scale": {"from": 0.8, "to": 1.0},
        },
        description="Scale up with fade",
        usage="Emphasis, important elements",
        default_duration="normal",
        default_easing="smooth",
    ),
}

# Exit transitions
EXIT_TRANSITIONS = {
    "fade_out": TransitionConfig(
        properties={
            "opacity": {"from": 1, "to": 0},
        },
        description="Simple fade out",
        usage="General purpose exit animation",
        default_duration="normal",
        default_easing="ease_in",
    ),
    "slide_out_up": TransitionConfig(
        properties={
            "opacity": {"from": 1, "to": 0},
            "translateY": {"from": "0px", "to": "-40px"},
        },
        description="Slide out to top with fade",
        usage="Content exiting upward",
        default_duration="normal",
        default_easing="ease_in",
    ),
    "slide_out_down": TransitionConfig(
        properties={
            "opacity": {"from": 1, "to": 0},
            "translateY": {"from": "0px", "to": "40px"},
        },
        description="Slide out to bottom with fade",
        usage="Content exiting downward",
        default_duration="normal",
        default_easing="ease_in",
    ),
    "scale_out": TransitionConfig(
        properties={
            "opacity": {"from": 1, "to": 0},
            "scale": {"from": 1.0, "to": 0.8},
        },
        description="Scale down with fade",
        usage="Elements disappearing",
        default_duration="normal",
        default_easing="ease_in",
    ),
}


# ============================================================================
# MOTION TOKENS CLASS
# ============================================================================


class MotionTokens:
    """Complete motion token system."""

    def __init__(self) -> None:
        self.durations = DURATIONS
        self.easings = EASINGS
        self.springs = SPRINGS
        self.enter_transitions = ENTER_TRANSITIONS
        self.exit_transitions = EXIT_TRANSITIONS

    def get_duration_ms(self, name: str) -> int:
        """Get duration in milliseconds."""
        if name not in self.durations:
            raise ValueError(f"Unknown duration: {name}")
        return self.durations[name].ms

    def get_duration_frames(self, name: str, fps: int = 30) -> int:
        """Get duration in frames."""
        if name not in self.durations:
            raise ValueError(f"Unknown duration: {name}")
        duration = self.durations[name]
        return duration.frames_30fps if fps == 30 else duration.frames_60fps

    def get_easing_curve(self, name: str) -> list[float]:
        """Get easing curve as cubic bezier array."""
        if name not in self.easings:
            raise ValueError(f"Unknown easing: {name}")
        return self.easings[name].curve

    def get_spring_config(self, name: str) -> dict[str, Any]:
        """Get spring configuration for Remotion."""
        if name not in self.springs:
            raise ValueError(f"Unknown spring: {name}")
        spring = self.springs[name]
        return {
            "damping": spring.damping,
            "mass": spring.mass,
            "stiffness": spring.stiffness,
            "overshootClamping": spring.overshootClamping,
        }

    def get_all(self) -> dict[str, Any]:
        """Get all motion tokens as dictionary."""
        return {
            "durations": {k: v.model_dump() for k, v in self.durations.items()},
            "easings": {k: v.model_dump() for k, v in self.easings.items()},
            "springs": {k: v.model_dump() for k, v in self.springs.items()},
            "enterTransitions": {k: v.model_dump() for k, v in self.enter_transitions.items()},
            "exitTransitions": {k: v.model_dump() for k, v in self.exit_transitions.items()},
        }
