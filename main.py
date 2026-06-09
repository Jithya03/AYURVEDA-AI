from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "FastAPI is working"}

@app.post("/ask")
def ask(data: ChatRequest):

    prompt = f"""
    You are Vaidya AI.

    Detect the user's language and answer in the same language.

    Question:
    {data.question}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }
    )

    return {
        "answer": response.json()["response"]
    }