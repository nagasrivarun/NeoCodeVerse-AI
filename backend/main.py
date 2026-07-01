from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

app = FastAPI(title="NeoCodeVerse AI API")


class TopicRequest(BaseModel):
    topic: str


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to NeoCodeVerse AI!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/config")
def config():
    return {
        "gemini_api_key_loaded": GEMINI_API_KEY is not None
    }


@app.post("/generate-script")
def generate_script(request: TopicRequest):

    prompt = f"""
Write a YouTube Shorts script about:

{request.topic}

Requirements:
- 120 to 150 words
- Beginner friendly
- Interesting hook
- End with a call to action
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "topic": request.topic,
        "script": response.text
    }
