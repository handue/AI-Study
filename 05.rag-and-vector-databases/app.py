from dotenv import load_dotenv
from openai import OpenAI

from supabase_client import supabase

load_dotenv()

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

query = input("Ask: ")

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query,
)

query_embedding = query_response.data[0].embedding

# rpc = Remote Procedure Call, which means calling function made in Supabase DB
result = supabase.rpc(
    "match_documents",
    # function name in Supabase DB
    {
        "query_embedding": query_embedding,
        "match_threshold": 0.3,
        "match_count": 3,
    },
).execute()

context = "\n\n".join(document["content"] for document in result.data)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{query}
"""

final_response = client.responses.create(
    model="gpt-5-nano",
    input=prompt,
)

print("\nAnswer:")
print(final_response.output_text)
