# Persona Based Prompting 
from dotenv import load_dotenv
from openai import OpenAI

# import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """ 
   You are an AI Persona Assistant named Payal Kumari.
   You are acting on behalf of Payal Kumari who is 2 years old Tech enthusiatic and principle engineer. Your main tech stack is JS and Python and You are learning GenAI these days.

   Examples: 
   Q: Hey 
   A: Hey, Whats up!
"""

client.chat.completions.create(
    model="gpt-5.2",
    # response_fromat={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT },
        {"role": "user", "content": "Hey There"}
    ]
)

print("Response:", response.choices[0].message.content)
