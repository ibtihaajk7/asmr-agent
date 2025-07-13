"""Individual generator script for ASMR components."""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import after path setup
try:
    from src.generators.script_generator import generate_script
    from src.generators.audio_generator import generate_audio
    from src.generators.video_generator import generate_video
    from src.generators.final_video_generator import generate_final_video
except ImportError:
    print("Error: Could not import generator modules. Make sure you're running from the project root.")
    sys.exit(1)


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


def run_final_video_generator(session_folder=None):
    """Run the final video generator with mixed audio."""
    result_path = generate_final_video(session_folder)
    print(f"✅ Final video generated in: {result_path}")


if __name__ == "__main__":
    print("🎬 ASMR Individual Component Generator")
    print("=" * 40)
    print("Available components:")
    print("1. Script")
    print("2. Audio") 
    print("3. Video")
    print("4. Final Video (mixed audio + video)")
    print("5. All components")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        print("\n1️⃣ Generating script...")
        run_script_generator()
        print("✅ Script generation complete!")
    elif choice == "2":
        print("\n2️⃣ Generating audio...")
        run_audio_generator()
        print("✅ Audio generation complete!")
    elif choice == "3":
        print("\n3️⃣ Generating video...")
        run_video_generator()
        print("✅ Video generation complete!")
    elif choice == "4":
        print("\n🎬 Generating final video with mixed audio...")
        run_final_video_generator()
        print("✅ Final video generation complete!")
    elif choice == "5":
        print("\n1️⃣ Generating script...")
        run_script_generator()
        print("\n2️⃣ Generating audio...")
        run_audio_generator()
        print("\n3️⃣ Generating video...")
        run_video_generator()
        print("\n4️⃣ Generating final video...")
        run_final_video_generator()
        print("\n🎯 All components generated!")
    else:
        print("❌ Invalid choice. Please run again and select 1-5.")
