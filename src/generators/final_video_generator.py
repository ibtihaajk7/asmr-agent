"""Final video generation module that mixes audio and combines with video."""

import os
import random
from pathlib import Path
from dotenv import load_dotenv
from src.config.constants import (
    get_latest_session_folder,
    load_session_info,
    save_session_info,
)

load_dotenv()
import ffmpeg as ffmpeg_lib
print("🔍 ffmpeg module loaded from:", ffmpeg_lib.__file__)



def get_background_audio_files():
    """Get available ocean background audio files from assets directory."""
    background_dir = Path("assets/background_audio")
    if not background_dir.exists():
        print("⚠️  Background audio directory not found. Creating it...")
        background_dir.mkdir(parents=True, exist_ok=True)
        return []
    
    # Only look for ocean files
    ocean_files = list(background_dir.glob("ocean_*.mp3")) + list(background_dir.glob("ocean_*.wav"))
    return ocean_files


def mix_audio_with_background(asmr_audio_path, session_folder):
    """Mix ASMR audio (70%) with random background audio (30%)."""
    background_files = get_background_audio_files()
    
    if not background_files:
        print("⚠️  No background audio files found. Using ASMR audio only.")
        mixed_audio_path = os.path.join(session_folder, "mixed_audio.wav")
        # Copy ASMR audio as mixed audio
        try:
            stream = ffmpeg_lib.input(asmr_audio_path)
            stream = ffmpeg_lib.output(stream, mixed_audio_path, acodec='copy')
            ffmpeg_lib.run(stream, overwrite_output=True, quiet=True)
            return mixed_audio_path
        except Exception as e:
            print(f"❌ Error copying audio: {e}")
            return None
    
    # Select random background audio
    background_file = random.choice(background_files)
    print(f"🎵 Using background audio: {background_file.name}")
    
    mixed_audio_path = os.path.join(session_folder, "mixed_audio.wav")
    
    # Mix audio using ffmpeg_lib: ASMR at 80% volume, background at 20%
    try:
        asmr_stream = ffmpeg_lib.input(asmr_audio_path)
        bg_stream = ffmpeg_lib.input(str(background_file))
        
        # Apply volume filters
        asmr_volume = ffmpeg_lib.filter(asmr_stream, 'volume', 0.9)
        bg_volume = ffmpeg_lib.filter(bg_stream, 'volume', 0.1)
        
        # Mix the audio streams - use 'longest' so background loops to match video duration
        mixed_stream = ffmpeg_lib.filter([asmr_volume, bg_volume], 'amix', inputs=2, duration='longest')
        
        # Output the mixed audio
        output_stream = ffmpeg_lib.output(mixed_stream, mixed_audio_path)
        ffmpeg_lib.run(output_stream, overwrite_output=True, quiet=True)
        
        print(f"✅ Audio mixed successfully: {mixed_audio_path}")
        return mixed_audio_path
        
    except Exception as e:
        print(f"❌ Error mixing audio: {e}")
        print("⚠️  Using ASMR audio only.")
        # Fallback to just ASMR audio
        try:
            stream = ffmpeg_lib.input(asmr_audio_path)
            stream = ffmpeg_lib.output(stream, mixed_audio_path, acodec='copy')
            ffmpeg_lib.run(stream, overwrite_output=True, quiet=True)
            return mixed_audio_path
        except Exception as e:
            print(f"❌ Error copying audio: {e}")
            return None


def combine_audio_with_video(video_path, audio_path, session_folder):
    """Combine mixed audio with video to create final video."""
    final_video_path = os.path.join(session_folder, "final_video.mp4")
    
    try:
        video_stream = ffmpeg_lib.input(video_path)
        audio_stream = ffmpeg_lib.input(audio_path)
        
        # Combine video and audio - video ends at full video duration (30 seconds)
        output_stream = ffmpeg_lib.output(
            video_stream, 
            audio_stream, 
            final_video_path,
            vcodec='copy',
            acodec='aac'
        )
        
        ffmpeg_lib.run(output_stream, overwrite_output=True, quiet=True)
        
        print(f"✅ Final video created: {final_video_path}")
        return final_video_path
        
    except Exception as e:
        print(f"❌ Error creating final video: {e}")
        return None


def generate_final_video(session_folder=None):
    """Generate final ASMR video with mixed audio and video."""
    if session_folder is None:
        session_folder = get_latest_session_folder()
        if session_folder is None:
            print("❌ No session folder found. Please generate a script first.")
            return None
    
    print(f"🎬 Generating final video for session: {session_folder}")
    
    # Check if required files exist
    asmr_audio_path = os.path.join(session_folder, "asmr.wav")
    video_path = os.path.join(session_folder, "pexels_video.mp4")
    
    if not os.path.exists(asmr_audio_path):
        print("❌ ASMR audio not found. Please generate audio first.")
        return None
    
    if not os.path.exists(video_path):
        print("❌ Video not found. Please generate video first.")
        print(f"Expected: {video_path}")
        return None
    
    # Step 1: Mix audio with background
    print("\n1️⃣ Mixing audio with background sounds...")
    mixed_audio_path = mix_audio_with_background(asmr_audio_path, session_folder)
    
    # Step 2: Combine with video
    print("\n2️⃣ Combining audio with video...")
    final_video_path = combine_audio_with_video(video_path, mixed_audio_path, session_folder)
    
    if final_video_path:
        # Update session info
        session_info = load_session_info(session_folder)
        session_info["files"]["mixed_audio"] = "mixed_audio.wav"
        session_info["files"]["final_video"] = "final_video.mp4"
        session_info["final_video_path"] = final_video_path
        save_session_info(session_folder, session_info)
        
        print(f"\n🎯 Final video ready for sharing: {final_video_path}")
        return final_video_path
    else:
        print("❌ Failed to create final video.")
        return None


if __name__ == "__main__":
    import sys
    
    # Check if session path was provided as command line argument
    session_arg = sys.argv[1] if len(sys.argv) > 1 else None
    result_path = generate_final_video(session_arg)
    if result_path:
        print(f"🎯 Session folder: {result_path}") 