from openai import OpenAI
import os
from constants import MODEL_NAME
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script():
    prompt = (
        "Write a short ASMR script about ocean waves and nighttime calm. "
        "Keep it under 30 words and whisper-style."
        "The script should be in the format of <speak prompt=\"Speak in whisper-style, soft tone\">Close your eyes... imagine the ocean... </speak>"
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an ASMR script generator."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )

    script = response.choices[0].message.content
    with open("script.txt", "w") as f:
        f.write(script.strip())

    print("✅ Script saved to script.txt")

if __name__ == "__main__":
    generate_script()
