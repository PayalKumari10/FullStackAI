from google.genai import client

client.configure(api_key="GEMINI_API_KEY") 

response = client.generate_text(
    model="gemini-1.5",
    prompt=(
        "You are an expert in Maths. Only answer maths-related questions. "
        "If the question is not about maths, say sorry.\n\n"
        "Solve (a + b) whole square."
    ),
)

print(response.result)
