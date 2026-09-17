from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

topic = input("What do you want to know? : ")


def get_learning_profile():
    return {
        "product": "Python",
        "role": "student",
        "level": "beginner",
    }


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
        "name": "get_learning_profile",
        "description": "Get the user's learning profile.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
    {
        "type": "function",
        "name": "search_courses",
        "description": "Search for courses based on product, role, and level.",
        "parameters": {
            "type": "object",
            "properties": {
                "product": {"type": "string"},
                "role": {"type": "string"},
                "level": {"type": "string"},
            },
            "required": ["product", "role", "level"],
        },
    },
]


response = client.responses.create(
    model="gpt-5-nano",
    input=topic,
    tools=tools,
)

while True:
    tool_called = False

    for item in response.output:
        if item.type == "function_call":
            tool_called = True

            if item.name == "get_learning_profile":
                result = get_learning_profile()

            elif item.name == "search_courses":

                arguments = json.loads(item.arguments)

                result = search_courses(
                    product=arguments["product"],
                    role=arguments["role"],
                    level=arguments["level"],
                )

            response = client.responses.create(
                model="gpt-5-nano",
                previous_response_id=response.id,
                input=[
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": json.dumps(result),
                    }
                ],
                tools=tools,
            )

    if not tool_called:
        print("\nAI: " + response.output_text)
        break
