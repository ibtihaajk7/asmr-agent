"""Configuration constants for ASMR generation."""

import os
import json
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


def save_session_info(session_path, session_info):
    """Save session information to JSON file."""
    session_info_path = os.path.join(session_path, "session_info.json")
    with open(session_info_path, "w", encoding="utf-8") as f:
        json.dump(session_info, f, indent=2)
