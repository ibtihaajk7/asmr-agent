"""Individual generator script for ASMR components."""

from src.generators.script_generator import generate_script
from src.generators.audio_generator import generate_audio
from src.generators.video_generator import generate_video


def run_script_generator():
    """Run the script generator."""
    result_path = generate_script()
    print(f"✅ Script generated in: {result_path}")


def run_audio_generator(session_folder=None):
    """Run the audio generator."""
    result_path = generate_audio(session_folder)
    print(f"✅ Audio generated in: {result_path}")


def run_video_generator(session_folder=None):
    """Run the video generator."""
    result_path = generate_video(session_folder)
    print(f"✅ Video generated in: {result_path}")


if __name__ == "__main__":
    print("🎬 ASMR Individual Component Generator")
    print("=" * 40)

    # Generate script first
    print("\n1️⃣ Generating script...")
    run_script_generator()

    # Generate audio using the script session
    print("\n2️⃣ Generating audio...")
    run_audio_generator()

    # Generate video using the same session
    print("\n3️⃣ Generating video...")
    run_video_generator()

    print("\n🎯 All components generated!")
    print("✅ Individual generation complete!")
