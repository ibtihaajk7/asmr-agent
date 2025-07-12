"""Script generation module using OpenAI API."""

import os
from openai import OpenAI
from dotenv import load_dotenv
from src.config.constants import MODEL_NAME, get_session_folder, save_session_info


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_script():
    """Generate ASMR script using OpenAI API and save to session folder."""
    # Create session folder
    session_path = get_session_folder()
    print(f"📁 Created session folder: {session_path}")

    prompt = (
        "Write a short ASMR script about ocean waves and nighttime calm. "
        "Keep it under 30 words and whisper-style. "
        'The script should be in the format of <speak prompt="Speak in whisper-style, soft tone">'
        "Close your eyes... imagine the ocean... </speak>"
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an ASMR script generator."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    script = response.choices[0].message.content

    # Save script to session folder
    script_path = os.path.join(session_path, "script.txt")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script.strip())

    # Save session info
    session_info = {
        "session_path": session_path,
        "model_used": MODEL_NAME,
        "prompt": prompt,
        "script": script.strip(),
        "files": {"script": "script.txt"},
    }
    save_session_info(session_path, session_info)

    print(f"✅ Script saved to {script_path}")
    return session_path


if __name__ == "__main__":
    result_session_path = generate_script()
    print(f"🎯 Session folder: {result_session_path}")
