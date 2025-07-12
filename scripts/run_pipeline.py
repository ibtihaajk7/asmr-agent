#!/usr/bin/env python3
"""
Full ASMR Pipeline Runner
Runs script generation, audio generation, and video generation in sequence.
"""

from src.generators.script_generator import generate_script
from src.generators.audio_generator import generate_audio
from src.generators.video_generator import generate_video
import time

def run_full_pipeline():
    print("🎬 Starting ASMR Pipeline...")
    print("=" * 50)
    
    # Step 1: Generate script
    print("📝 Step 1: Generating ASMR script...")
    session_path = generate_script()
    if not session_path:
        print("❌ Failed to generate script")
        return None
    
    print("=" * 50)
    
    # Step 2: Generate audio
    print("🎧 Step 2: Generating ASMR audio...")
    session_path = generate_audio(session_path)
    if not session_path:
        print("❌ Failed to generate audio")
        return None
    
    print("=" * 50)
    
    # Step 3: Generate video
    print("🎥 Step 3: Generating video...")
    session_path = generate_video(session_path)
    if not session_path:
        print("❌ Failed to generate video")
        return None
    
    print("=" * 50)
    print("🎉 Pipeline completed successfully!")
    print(f"📁 All files saved in: {session_path}")
    print("📋 Files created:")
    print("   - script.txt")
    print("   - asmr.wav")
    print("   - pexels_video.mp4")
    print("   - session_info.json")
    
    return session_path

if __name__ == "__main__":
    run_full_pipeline() 