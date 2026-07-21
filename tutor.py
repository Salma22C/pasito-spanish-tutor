import os

from dotenv import load_dotenv
from openai import OpenAI

from prompts import build_system_prompt


# Load variables from the .env file.
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY was not found. Add it to your .env file."
    )


# The OpenAI Python SDK communicates with OpenRouter through this base URL.
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def get_tutor_response(
    user_message: str,
    explanation_language: str,
) -> str:
    system_prompt = build_system_prompt(explanation_language)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=messages,
    )

    assistant_reply = response.choices[0].message.content

    if not assistant_reply:
        raise ValueError("The model returned an empty response.")

    return assistant_reply