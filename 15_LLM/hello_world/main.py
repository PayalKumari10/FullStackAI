from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()  # key auto-picked

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Hey there"
)

print(response.output_text)
