"""Full pipeline script for ASMR generation."""

from src.generators.script_generator import generate_script
from src.generators.audio_generator import generate_audio
from src.generators.video_generator import generate_video


def run_full_pipeline():
    """Run the complete ASMR generation pipeline."""
    print("🎬 Starting ASMR Generation Pipeline")
    print("=" * 40)

    # Step 1: Generate script
    print("\n1️⃣ Generating script...")
    session_path = generate_script()
    print(f"✅ Script generated in: {session_path}")

    # Step 2: Generate audio
    print("\n2️⃣ Generating audio...")
    session_path = generate_audio(session_path)
    print(f"✅ Audio generated in: {session_path}")

    # Step 3: Generate video
    print("\n3️⃣ Generating video...")
    session_path = generate_video(session_path)
    print(f"✅ Video generated in: {session_path}")

    print("\n🎯 Pipeline Complete!")
    print(f"📁 All files saved in: {session_path}")
    print("🎉 Your ASMR content is ready!")

    return session_path


if __name__ == "__main__":
    result_path = run_full_pipeline()
    print(f"\n🎯 Final session folder: {result_path}")
