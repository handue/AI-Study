# from dotenv import load_dotenv
from openai import OpenAI

from supabase_client import supabase

# load_dotenv()

client = OpenAI()


content = "Python is a programming language commonly used for AI development."

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=content,
)
embedding = response.data[0].embedding


supabase.table("documents").insert(
    {
        "content": content,
        "embedding": embedding,
    }
).execute()


print("Document saved")
