from app.config import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)
