from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#Zero Shot Prompting: Directly giving the inst to the model
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other then coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-1.5-flash",
    n=1,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey , can you help me solve the a + b whole square."
        }
        

    ]
)

print(response.choices[0].message)