"""Standalone script to create final ASMR video with mixed audio."""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import after path setup
try:
    from src.generators.final_video_generator import generate_final_video
except ImportError:
    print("Error: Could not import final video generator. Make sure you're running from the project root.")
    sys.exit(1)


def main():
    """Main function to run final video generation."""
    print("🎬 ASMR Final Video Generator")
    print("=" * 40)
    print("This will:")
    print("1. Mix ASMR audio (70%) with random background audio (30%)")
    print("2. Combine mixed audio with video")
    print("3. Save as final_video.mp4 in the session folder")
    print()
    
    # Check if session path was provided as command line argument
    session_arg = sys.argv[1] if len(sys.argv) > 1 else None
    
    if session_arg:
        print(f"Using specified session: {session_arg}")
    else:
        print("Using latest session folder")
    
    print("\n🎬 Starting final video generation...")
    result_path = generate_final_video(session_arg)
    
    if result_path:
        print(f"\n🎯 Final video created successfully!")
        print(f"📁 Location: {result_path}")
        print("✅ Ready to share!")
    else:
        print("❌ Failed to create final video.")
        print("Make sure you have:")
        print("- Generated a script")
        print("- Generated audio (asmr.wav)")
        print("- Generated video (pexels_video.mp4)")
        print("- Background audio files in assets/background_audio/")
        print("- FFmpeg installed on your system")


if __name__ == "__main__":
    main() 