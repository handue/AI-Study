from dotenv import load_dotenv
from openai import OpenAI

# getting text from user

load_dotenv()

client = OpenAI()

topic = input("What do you want to study? ")
level = input("What is your level of understanding? (beginner, intermediate, advanced) ")

prompt = f"""
You are a helpful study assistant.

Teach me about {topic} for a {level} level student.


Please include:
1. A simple explanation
2. One example
3. Three key points
4. One practice question
"""

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt,
    reasoning={"effort": "minimal"},
    max_output_tokens=300,
    store=False,
)

print("\n--- Study Buddy ---\n")
print(response.output_text)