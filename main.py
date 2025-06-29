import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get(GEMINI_API_KEY)
client = genai.Client(api_key=api_key)
