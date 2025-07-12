import os
import sys
from dotenv import load_dotenv
from resemble import Resemble
import json
from constants import save_session_info

# Load API key from .env file
load_dotenv()
RESEMBLE_API_KEY = os.getenv("RESEMBLE_API_KEY")

# Initialize Resemble SDK
Resemble.api_key(RESEMBLE_API_KEY)

def generate_audio(session_path=None):
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
    
    # ✅ Get your default project
    projects = Resemble.v2.projects.all(1, 10)
    project_uuid = projects['items'][0]['uuid']

    # ✅ Get your voice UUID
    voice_uuid = "ba4210af"

    # ✅ Read your ASMR script from session folder
    script_path = os.path.join(session_path, "script.txt")
    with open(script_path, "r") as f:
        text = f.read()

    # ✅ Create the clip synchronously
    clip = Resemble.v2.clips.create_sync(
        project_uuid,
        voice_uuid,
        text,
        title="asmr-clip",
        output_format="wav",
        precision="PCM_16"
    )

    # ✅ Download the audio
    print(json.dumps(clip, indent=2))
    audio_url = clip['item']['audio_src']
    print(f"🎧 Audio URL: {audio_url}")

    # Download and save the audio file to session folder
    import requests
    audio = requests.get(audio_url)
    audio_path = os.path.join(session_path, "asmr.wav")
    with open(audio_path, "wb") as f:
        f.write(audio.content)

    # Update session info
    session_info_path = os.path.join(session_path, "session_info.json")
    if os.path.exists(session_info_path):
        with open(session_info_path, "r") as f:
            session_info = json.load(f)
    else:
        session_info = {"session_path": session_path, "files": {}}
    
    session_info["files"]["audio"] = "asmr.wav"
    session_info["audio_url"] = audio_url
    save_session_info(session_path, session_info)

    print(f"✅ Audio saved to {audio_path}")
    return session_path

if __name__ == "__main__":
    # Check if session path was provided as command line argument
    session_path = sys.argv[1] if len(sys.argv) > 1 else None
    session_path = generate_audio(session_path)
    if session_path:
        print(f"🎯 Session folder: {session_path}")