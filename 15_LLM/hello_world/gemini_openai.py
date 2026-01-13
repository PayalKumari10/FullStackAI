from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDTFgC2x8V5lAAeykAykL3H6sTuau431xQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.responses.create(
    model="gemini-1.5-flash",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "You are an expert in Maths and only answer maths-related questions. "
                        "If the query is not related to maths, say sorry and do not answer.\n\n"
                        "Question: Solve (a + b) whole square."
                    )
                }
            ]
        }
    ]
)

print(response.output_text)








