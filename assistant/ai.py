import requests

def ask_ai(question):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": question,
            "stream": False
        }
    )

    return response.json()["response"]


import requests

def ask_ai(question):

    prompt = f"""
    You are Vaidya AI, an Ayurvedic assistant.

    Rules:
    - Detect the user's language automatically.
    - Answer in the SAME language as the question.
    - If the question is in Malayalam, answer in Malayalam.
    - If the question is in English, answer in English.
    - If the question is in Hindi, answer in Hindi.
    - Provide Ayurvedic information and remedies when appropriate.
    - For serious medical conditions, advise consulting a qualified doctor.

    User Question:
    {question}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]