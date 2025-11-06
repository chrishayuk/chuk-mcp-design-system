"""
Motion System Showcase

Demonstrates all motion/animation features:
- Durations with frame conversions
- Easing curves
- Spring configurations (Remotion-compatible)
- Transition presets
"""

from chuk_design_system.tokens import MotionTokens, DURATIONS, EASINGS, SPRINGS


def showcase_durations():
    """Showcase duration tokens."""
    print("=" * 60)
    print("DURATIONS (Video-optimized)")
    print("=" * 60)
    print("\nDurations with frame conversions for video:\n")

    motion = MotionTokens()

    durations_to_show = ["instant", "fast", "normal", "slow", "slowest"]

    for name in durations_to_show:
        duration = DURATIONS[name]
        print(f"{name.capitalize()}:")
        print(f"  {duration.ms}ms ({duration.seconds}s)")
        print(f"  30fps: {duration.frames_30fps} frames | 60fps: {duration.frames_60fps} frames")
        print(f"  CSS: {duration.css}")
        print()


def showcase_easings():
    """Showcase easing curves."""
    print("=" * 60)
    print("EASING CURVES")
    print("=" * 60)
    print("\nCubic bezier curves for smooth animations:\n")

    easings_to_show = ["linear", "ease_out", "ease_in_out", "smooth", "snappy", "bouncy"]

    def visualize_easing(curve, width=40):
        """Create a simple ASCII visualization of easing curve."""
        # Sample the curve at different points
        points = []
        for i in range(width):
            t = i / (width - 1)
            # Approximate bezier curve output (simplified)
            if curve == [0.0, 0.0, 1.0, 1.0]:  # linear
                y = t
            elif curve == [0.0, 0.0, 0.58, 1.0]:  # ease_out
                y = 1 - (1 - t) ** 2
            elif curve == [0.42, 0.0, 0.58, 1.0]:  # ease_in_out
                y = t ** 2 if t < 0.5 else 1 - (1 - t) ** 2
            elif curve == [0.4, 0.0, 0.2, 1.0]:  # smooth
                y = 1 - (1 - t) ** 1.8
            elif curve == [0.4, 0.0, 0.6, 1.0]:  # snappy
                y = 1 - (1 - t) ** 1.5
            else:  # bouncy - overshoots
                y = min(1.2, 1 - (1 - t) ** 2 * (1 + 0.2 * (1 - t)))

            points.append(int(y * 10))

        # Draw the curve
        viz = ""
        for height in range(10, -1, -1):
            line = "  "
            for point in points:
                if point == height:
                    line += "•"
                elif abs(point - height) <= 1:
                    line += "·"
                else:
                    line += " "
            if height == 10:
                viz += line + " ← end\n"
            elif height == 0:
                viz += line + " ← start\n"
            else:
                viz += line + "\n"
        return viz

    for name in easings_to_show:
        easing = EASINGS[name]
        print(f"{name.replace('_', ' ').title()}:")
        print(f"  Curve: {easing.curve}")
        print(visualize_easing(easing.curve))
        print(f"  Usage: {easing.usage}")
        print()


def showcase_springs():
    """Showcase spring configurations."""
    print("=" * 60)
    print("SPRING CONFIGURATIONS (Remotion-compatible)")
    print("=" * 60)
    print("\nPhysics-based spring animations:\n")

    motion = MotionTokens()

    for name in ["gentle", "smooth", "bouncy", "snappy", "stiff"]:
        spring = SPRINGS[name]
        config = motion.get_spring_config(name)

        print(f"{name.capitalize()}:")
        print(f"  Config: damping={config['damping']}, stiffness={config['stiffness']}, mass={config['mass']}")
        print(f"  Feel: {spring.feel}")
        print(f"  Usage: {spring.usage}")
        print()


def showcase_transitions():
    """Showcase transition presets."""
    print("=" * 60)
    print("TRANSITION PRESETS")
    print("=" * 60)

    motion = MotionTokens()

    print("\nEnter Transitions:")
    for name in ["fade_in", "slide_in_up", "scale_in"]:
        transition = motion.enter_transitions[name]
        print(f"\n  {name.replace('_', ' ').title()}:")
        print(f"    Description: {transition.description}")
        print(f"    Duration: {transition.default_duration}")
        print(f"    Easing: {transition.default_easing}")
        print(f"    Properties: {', '.join(transition.properties.keys())}")

    print("\nExit Transitions:")
    for name in ["fade_out", "slide_out_up", "scale_out"]:
        transition = motion.exit_transitions[name]
        print(f"\n  {name.replace('_', ' ').title()}:")
        print(f"    Description: {transition.description}")
        print(f"    Duration: {transition.default_duration}")
        print(f"    Easing: {transition.default_easing}")


def showcase_usage_examples():
    """Show practical usage examples."""
    print("\n" + "=" * 60)
    print("USAGE EXAMPLES")
    print("=" * 60)

    motion = MotionTokens()

    print("\nFor Remotion video (TypeScript):")
    spring = motion.get_spring_config("smooth")
    print(f"  spring({{ damping: {spring['damping']}, stiffness: {spring['stiffness']}, mass: {spring['mass']} }})")

    print("\nFor CSS animations:")
    print(f"  transition: all {DURATIONS['normal'].css} {EASINGS['ease_out'].css};")

    print("\nFor frame-based animations (30fps):")
    duration_frames = motion.get_duration_frames("normal", 30)
    print(f"  {duration_frames} frames @ 30fps")


def main():
    """Run all motion showcases."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "   ⚡ CHUK DESIGN SYSTEM - MOTION SHOWCASE   ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    showcase_durations()
    showcase_easings()
    showcase_springs()
    showcase_transitions()
    showcase_usage_examples()

    print("\n" + "=" * 60)
    print("✅ Motion showcase complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  - Try: python examples/showcase_colors.py")
    print("  - Try: python examples/showcase_typography.py")
    print("  - Try: python examples/showcase_spacing.py")
    print()


if __name__ == "__main__":
    main()
