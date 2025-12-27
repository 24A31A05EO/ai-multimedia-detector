import httpx
from bs4 import BeautifulSoup
from app.config import settings
import os

async def detect_url(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text().strip()

        # Use Gemini Pro to analyze writing style
        import openai
        openai.api_key = settings.GEMINI_API_KEY

        prompt = f"Is the following webpage content likely AI-generated? Justify your answer.\n\n{text[:2000]}"
        completion = openai.ChatCompletion.create(
            model="models/gemini-pro",
            messages=[{"role": "user", "content": prompt}]
        )

        reply = completion.choices[0].message.content
        is_fake = "yes" in reply.lower()
        confidence = 0.8 if is_fake else 0.3

        return {
            "type": "url",
            "is_fake": is_fake,
            "confidence": round(confidence, 2),
            "reason": reply
        }

    except Exception as e:
        return {
            "type": "url",
            "is_fake": False,
            "confidence": 0.0,
            "reason": f"Error analyzing URL: {str(e)}"
        }
