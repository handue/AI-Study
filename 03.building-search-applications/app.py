from dotenv import load_dotenv
from openai import OpenAI
import math

load_dotenv()

client = OpenAI()

documents = [
    "Python lists are mutable collections that can store multiple values.",
    "JavaScript arrays provide methods such as map, filter, and reduce.",
    "Gradient descent is an optimization algorithm used to minimize a loss function.",
    "Neural networks are composed of layers of interconnected neurons.",
]


def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    return response.data[0].embedding


def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    # Calculate the magnitude of each vector
    # ex) a = [1,2,3], b = [4,5,6]
    # ex) x * y = 1*4 + 2*5 + 3*6 = 32


    magnitude_a = math.sqrt(sum(x * x for x in a))
    # Calculate the magnitude of vector a
    # ex) a = [1,2,3], magnitude_a = sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
   
    magnitude_b = math.sqrt(sum(y * y for y in b))
    # Calculate the magnitude of vector b
    # ex) b = [4,5,6], magnitude_b = sqrt(4^2 + 5^2 + 6^2) = sqrt(77)
    return dot_product / (magnitude_a * magnitude_b)


document_embeddings = []

for document in documents:
    embedding = get_embedding(document)

    document_embeddings.append({
        "text": document,
        "embedding": embedding,
    })


query = input("Search: ")
query_embedding = get_embedding(query)

results = []

for document in document_embeddings:
    similarity = cosine_similarity(
        query_embedding,
        document["embedding"],
    )

    results.append({
        "text": document["text"],
        "similarity": similarity,
    })


results.sort(
    key=lambda result: result["similarity"],
    reverse=True,
)

print("\nSearch results:\n")

for result in results:
    print(result["similarity"], result["text"])