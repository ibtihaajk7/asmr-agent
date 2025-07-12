# constants.py
# Edit this file to change the OpenAI model used throughout the project.
# MODEL_NAME = "gpt-4o" 
# MODEL_NAME = "gpt-3.5-turbo" 
MODEL_NAME = "gpt-4o-mini" 

import os
from datetime import datetime
import json

def get_session_folder():
    """Generate a unique folder name for each session"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Check for existing sessions and increment counter
    session_counter = 1
    while True:
        session_name = f"asmr_session_{timestamp}_{session_counter:03d}"
        session_path = os.path.join(output_dir, session_name)
        if not os.path.exists(session_path):
            os.makedirs(session_path)
            return session_path
        session_counter += 1

def save_session_info(session_path, info_dict):
    """Save session information to a JSON file"""
    info_file = os.path.join(session_path, "session_info.json")
    with open(info_file, "w") as f:
        json.dump(info_dict, f, indent=2)
