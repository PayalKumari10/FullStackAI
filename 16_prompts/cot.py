from dotenv import load_dotenv
from openai import OpenAI
import os
import json

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Check your .env file.")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
Return responses strictly in JSON.
Format:
{ "step": "START | PLAN | OUTPUT", "content": "string" }
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=message_history,
        response_format={"type": "json_object"}
    )

    raw = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw})

    data = json.loads(raw)

    step = data.get("step")
    content = data.get("content")

    if step == "START":
        print("🔥", content)
        continue

    if step == "PLAN":
        print("🧠", content)
        continue

    if step == "OUTPUT":
        print("🤖", content)
        break

print("\nDone ✅")
