import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def ask_ai(question):
    prompt = f"""
    You are Vaidya AI, an Ayurvedic assistant.

    Rules:
    - Detect the user's language automatically.
    - Answer in the SAME language as the question.
    - Provide Ayurvedic information and remedies when appropriate.
    - For serious medical conditions, advise consulting a qualified doctor.

    User Question:
    {question}
    """

    response = model.generate_content(prompt)
    return response.text