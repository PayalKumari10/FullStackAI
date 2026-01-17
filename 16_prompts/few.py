from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

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
A: Sorry, I can only help with coding-related questions.

Q: Write a python function to add two numbers.
A:
def add(a, b):
    return a + b
"""
                }
            ],
        },
        {
            "role": "user",
            "parts": [
                {
                    "text": "Hey, can you write a python code to translate the word hello to Hindi"
                }
            ],
        },
    ],
)

print(response.text)

#Few-shot Prompting: The model is provided with a few examples before asking it to genreate a response.