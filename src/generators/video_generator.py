"""Video generation module using Pexels API."""

import os
import sys
import json
from src.utils.pexels_utils import search_pexels_video, download_video
from src.config.constants import (
    save_session_info,
    get_latest_session_folder,
    load_session_info,
)


def generate_video(session_folder=None):
    """Generate video using Pexels API and save to session folder."""
    if session_folder is None:
        session_folder = get_latest_session_folder()
        if session_folder is None:
            return None

    # Choose video type based on the voice script or audio background
    video_type = "ocean"  # you can vary this dynamically later
    video_url = search_pexels_video(query=video_type, duration=30)

    # Download video to session folder
    video_path = os.path.join(session_folder, "pexels_video.mp4")
    download_video(video_url, video_path)

    # Update session info
    session_info = load_session_info(session_folder)
    session_info["files"]["video"] = "pexels_video.mp4"
    session_info["video_type"] = video_type
    session_info["video_url"] = video_url
    save_session_info(session_folder, session_info)

    print(f"✅ Video saved to {video_path}")
    return session_folder


if __name__ == "__main__":
    # Check if session path was provided as command line argument
    session_arg = sys.argv[1] if len(sys.argv) > 1 else None
    result_session_path = generate_video(session_arg)
    if result_session_path:
        print(f"🎯 Session folder: {result_session_path}")
