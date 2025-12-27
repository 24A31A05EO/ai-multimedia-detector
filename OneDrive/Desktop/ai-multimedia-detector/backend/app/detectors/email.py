from app.config import settings
import openai

async def detect_email(headers: str, body: str):
    try:
        openai.api_key = settings.GEMINI_API_KEY

        prompt = f"Analyze the following email headers and body. Is it likely AI-generated or phishing? Justify your answer.\n\nHeaders:\n{headers}\n\nBody:\n{body}"
        completion = openai.ChatCompletion.create(
            model="models/gemini-pro",
            messages=[{"role": "user", "content": prompt}]
        )

        reply = completion.choices[0].message.content
        is_fake = "yes" in reply.lower()
        confidence = 0.85 if is_fake else 0.4

        return {
            "type": "email",
            "is_fake": is_fake,
            "confidence": round(confidence, 2),
            "reason": reply
        }

    except Exception as e:
        return {
            "type": "email",
            "is_fake": False,
            "confidence": 0.0,
            "reason": f"Error analyzing email: {str(e)}"
        }
