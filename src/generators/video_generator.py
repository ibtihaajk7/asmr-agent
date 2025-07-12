"""Video generation module using Pexels API."""

import os
import sys
import json
from src.utils.pexels_utils import search_pexels_video, download_video
from src.config.constants import save_session_info


def generate_video(session_path=None):
    """Generate video using Pexels API and save to session folder."""
    if session_path is None:
        # If no session path provided, look for the most recent session
        output_dir = "output"
        if not os.path.exists(output_dir):
            print("❌ No output directory found. Run generate_script.py first.")
            return None

        # Find the most recent session folder
        sessions = [d for d in os.listdir(output_dir) if d.startswith("asmr_session_")]
        if not sessions:
            print("❌ No session folders found. Run generate_script.py first.")
            return None

        sessions.sort(reverse=True)  # Most recent first
        session_path = os.path.join(output_dir, sessions[0])
        print(f"📁 Using existing session: {session_path}")

    # Choose video type based on the voice script or audio background
    video_type = "ocean"  # you can vary this dynamically later
    video_url = search_pexels_video(query=video_type, duration=30)

    # Download video to session folder
    video_path = os.path.join(session_path, "pexels_video.mp4")
    download_video(video_url, video_path)

    # Update session info
    session_info_path = os.path.join(session_path, "session_info.json")
    if os.path.exists(session_info_path):
        with open(session_info_path, "r", encoding="utf-8") as f:
            session_info = json.load(f)
    else:
        session_info = {"session_path": session_path, "files": {}}

    session_info["files"]["video"] = "pexels_video.mp4"
    session_info["video_type"] = video_type
    session_info["video_url"] = video_url
    save_session_info(session_path, session_info)

    print(f"✅ Video saved to {video_path}")
    return session_path


if __name__ == "__main__":
    # Check if session path was provided as command line argument
    session_arg = sys.argv[1] if len(sys.argv) > 1 else None
    result_session_path = generate_video(session_arg)
    if result_session_path:
        print(f"🎯 Session folder: {result_session_path}")
