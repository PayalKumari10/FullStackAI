from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other then coding, just say sorry."


response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        {
            "role": "system",
            "parts": [
                {
                    "text": """
You should only answer coding-related questions.
Your name is Alexa.
If the user asks anything other than coding, say sorry.

Examples:
Q: Can you explain a + b whole square?
A: {{ "code" : null, "isCodingQueston": false }}

Q: Write a python function to add two numbers.
A: {{"code": "def add(a,b): return a + b", "isCodingQuestion":false }}

    
"""
                }
            ],
        },
        {
            "role": "user",
            "parts": [
                {
                    "text": "Hey, write a code to add n number in js"
                }
            ],
        },
    ],
)

print(response.text)

#Few-shot Prompting: The model is provided with a few examples before asking it to genreate a response.