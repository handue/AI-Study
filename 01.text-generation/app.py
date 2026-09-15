from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Explain gradient descent in one sentence.",
    reasoning={"effort": "minimal"},
    max_output_tokens=1024,
    store=False,
)

print(response.output_text)