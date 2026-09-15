from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.responses.create(
        model="gpt-5-nano",
        input=messages,
        reasoning={"effort": "minimal"},
        max_output_tokens=2000,
        store=False,
    )

    assistant_message = response.output_text

    print(f"AI: {assistant_message}")

    messages.append({
        "role": "assistant",
        "content": assistant_message
    })