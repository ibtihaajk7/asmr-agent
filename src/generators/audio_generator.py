"""Audio generation module using Resemble AI API."""

import os
import sys
import json
import requests
from dotenv import load_dotenv
from resemble import Resemble
from src.config.constants import (
    save_session_info,
    get_latest_session_folder,
    load_session_info,
)

# Load API key from .env file
load_dotenv()
RESEMBLE_API_KEY = os.getenv("RESEMBLE_API_KEY")

# Initialize Resemble SDK
Resemble.api_key(RESEMBLE_API_KEY)


def generate_audio(session_folder=None):
    """Generate ASMR audio using Resemble AI and save to session folder."""
    if session_folder is None:
        session_folder = get_latest_session_folder()
        if session_folder is None:
            return None

    # Get your default project
    projects = Resemble.v2.projects.all(1, 10)
    project_uuid = projects["items"][0]["uuid"]

    # Get your voice UUID
    voice_uuid = "ba4210af"

    # Read your ASMR script from session folder
    script_path = os.path.join(session_folder, "script.txt")
    with open(script_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Create the clip synchronously
    clip = Resemble.v2.clips.create_sync(
        project_uuid,
        voice_uuid,
        text,
        title="asmr-clip",
        output_format="wav",
        precision="PCM_16",
    )

    # Download the audio
    print(json.dumps(clip, indent=2))
    audio_url = clip["item"]["audio_src"]
    print(f"🎧 Audio URL: {audio_url}")

    audio = requests.get(audio_url, timeout=90)
    audio_path = os.path.join(session_folder, "asmr.wav")
    with open(audio_path, "wb") as f:
        f.write(audio.content)

    # Update session info
    session_info = load_session_info(session_folder)
    session_info["files"]["audio"] = "asmr.wav"
    session_info["audio_url"] = audio_url
    save_session_info(session_folder, session_info)

    print(f"✅ Audio saved to {audio_path}")
    return session_folder


if __name__ == "__main__":
    # Check if session path was provided as command line argument
    session_arg = sys.argv[1] if len(sys.argv) > 1 else None
    result_path = generate_audio(session_arg)
    if result_path:
        print(f"🎯 Session folder: {result_path}")
