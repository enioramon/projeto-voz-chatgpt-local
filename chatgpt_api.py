from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatgpt(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=text
    )
    return response.output_text
