import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY missing")

client = Groq(api_key=api_key)

def generate_ai_response(review: str, rating: int) -> str:
    prompt = f"""
    A customer gave a rating of {rating}/5.

    Review:
    "{review}"

    Write a polite, professional service reply.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ supported
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
