#!/usr/bin/env python3
"""
Individual Generator Runner
Run specific generators from the root directory.
"""

import sys
import os

# Add src to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def run_script_generator():
    """Run the script generator."""
    from src.generators.script_generator import generate_script

    return generate_script()


def run_audio_generator(session_path=None):
    """Run the audio generator."""
    from src.generators.audio_generator import generate_audio

    return generate_audio(session_path)


def run_video_generator(session_path=None):
    """Run the video generator."""
    from src.generators.video_generator import generate_video

    return generate_video(session_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python scripts/generate_individual.py [script|audio|video] [session_path]"
        )
        print("Examples:")
        print("  python scripts/generate_individual.py script")
        print("  python scripts/generate_individual.py audio")
        print("  python scripts/generate_individual.py video")
        print(
            "  python scripts/generate_individual.py audio output/asmr_session_20241201_143022_001"
        )
        sys.exit(1)

    generator_type = sys.argv[1]
    session_path = sys.argv[2] if len(sys.argv) > 2 else None

    if generator_type == "script":
        session_path = run_script_generator()
    elif generator_type == "audio":
        session_path = run_audio_generator(session_path)
    elif generator_type == "video":
        session_path = run_video_generator(session_path)
    else:
        print(f"❌ Unknown generator type: {generator_type}")
        sys.exit(1)

    if session_path:
        print(f"🎯 Session folder: {session_path}")
