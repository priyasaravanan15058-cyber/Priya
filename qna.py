from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME


client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


SYSTEM_PROMPT = """
You are EduGenie AI, a friendly educational assistant.

Explain topics clearly for students.
Use simple English, short sections, examples, and bullet points when useful.
Do not invent facts.
If the question is unclear, ask for clarification.
"""


def answer_question(prompt):

    if not prompt or not prompt.strip():
        return "Please enter a question or topic."

    if client is None:
        return "Gemini API key is not configured."

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt.strip(),
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.4,
                max_output_tokens=1000,
            ),
        )

        text = (response.text or "").strip()

        if text:
            return text

        return "I could not generate a response. Please try again."

    except Exception as error:
        return f"Gemini API error: {error}"