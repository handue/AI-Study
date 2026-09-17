from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()


def search_courses(product, role, level):
    return [
        {
            "title": f"{product} Fundamentals",
            "role": role,
            "level": level,
        },
        {
            "title": f"Introduction to {product}",
            "role": role,
            "level": level,
        },
    ]


tools = [
    {
        "type": "function",
        "name": "search_courses",
        "description": "Search for technical courses based on product, role, and skill level.",
        "parameters": {
            "type": "object",
            "properties": {
                "product": {
                    "type": "string",
                    "description": "The technology the user wants to learn.",
                },
                "role": {
                    "type": "string",
                    "description": "The user's role, for example student or developer.",
                },
                "level": {
                    "type": "string",
                    "description": "The user's skill level.",
                },
            },
            "required": ["product", "role", "level"],
        },
    }
]


user_input = input("You: ")

response = client.responses.create(
    model="gpt-5-nano",
    input=user_input,
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        arguments = json.loads(item.arguments)

        result = search_courses(
            product=arguments["product"],
            role=arguments["role"],
            level=arguments["level"],
        )

        final_response = client.responses.create(
            model="gpt-5-nano",
            previous_response_id=response.id,
            # previous_response_id = references for the previous response, so the model can see the context of the conversation
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    # call_id = previous function call id, so the model can see the context of the function call
                    "output": json.dumps(result),
                }
            ],
        )

        print(final_response.output_text)
