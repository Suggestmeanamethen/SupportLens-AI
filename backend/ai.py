import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from backend.prompts import SYSTEM_PROMPT

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_issue(issue, logs="", image=None):

    prompt = f"""
{SYSTEM_PROMPT}

User Issue:
{issue}

Logs:
{logs}
"""

    contents = [prompt]

    # If a screenshot was uploaded, send it to Gemini too
    if image is not None:

        image_bytes = image.file.read()

        contents.append(
            genai.types.Part.from_bytes(
                data=image_bytes,
                mime_type=image.content_type
            )
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents
    )

    return response.text