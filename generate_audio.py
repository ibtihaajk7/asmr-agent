import os
from dotenv import load_dotenv
from resemble import Resemble
import json

# Load API key from .env file
load_dotenv()
RESEMBLE_API_KEY = os.getenv("RESEMBLE_API_KEY")

# Initialize Resemble SDK
Resemble.api_key(RESEMBLE_API_KEY)

# ✅ Get your default project
projects = Resemble.v2.projects.all(1, 10)
project_uuid = projects['items'][0]['uuid']

# ✅ Get your voice UUID
voice_uuid = "ba4210af"

# ✅ Read your ASMR script
with open("script.txt", "r") as f:
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

# Download and save the audio file
import requests
audio = requests.get(audio_url)
with open("asmr.wav", "wb") as f:
    f.write(audio.content)

print("✅ Saved to asmr.wav")