"""Configuration constants for ASMR generation."""

import json
import os
from datetime import datetime

# Model configuration
MODEL_NAME = "gpt-4o-mini"
VOICE_ID = "ba4210af"
OUTPUT_DIR = "output"


def get_session_folder():
    """Create and return a unique session folder path."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    counter = 1
    while True:
        session_name = f"asmr_session_{timestamp}_{counter:03d}"
        session_path = os.path.join(OUTPUT_DIR, session_name)
        if not os.path.exists(session_path):
            os.makedirs(session_path, exist_ok=True)
            return session_path
        counter += 1


def get_latest_session_folder():
    """Get the most recent session folder or None if none exists."""
    if not os.path.exists(OUTPUT_DIR):
        print("❌ No output directory found. Run generate_script.py first.")
        return None

    # Find the most recent session folder
    sessions = [d for d in os.listdir(OUTPUT_DIR) if d.startswith("asmr_session_")]
    if not sessions:
        print("❌ No session folders found. Run generate_script.py first.")
        return None

    sessions.sort(reverse=True)  # Most recent first
    session_folder = os.path.join(OUTPUT_DIR, sessions[0])
    print(f"📁 Using existing session: {session_folder}")
    return session_folder


def load_session_info(session_folder):
    """Load session info from JSON file or create default structure."""
    session_info_path = os.path.join(session_folder, "session_info.json")
    if os.path.exists(session_info_path):
        with open(session_info_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"session_path": session_folder, "files": {}}


def save_session_info(session_path, session_info):
    """Save session information to JSON file."""
    session_info_path = os.path.join(session_path, "session_info.json")
    with open(session_info_path, "w", encoding="utf-8") as f:
        json.dump(session_info, f, indent=2)
