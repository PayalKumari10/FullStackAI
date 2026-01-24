from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434"
)

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/contact-us")
def contact():
    return {"email": "payalk@gmail.com"}

@app.post("/chat")
def chat(
        message: str = Body(..., description="Write a python function to add two numbers")
):
    response = client.chat(model="gemma2:latest", messages=[
        {"role": "user", "content": message}
    ])
    return {"response": response.choices[0].message.content}