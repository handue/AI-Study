# AI Study

A collection of Python examples covering text generation, chat applications,
semantic search, function calling, retrieval-augmented generation (RAG),
and AI agents.

## Examples

| Directory | Description |
| --- | --- |
| `01.text-generation` | Generate text from a fixed prompt or build an interactive study prompt. |
| `02.building-chat-applications` | Build a terminal chatbot with in-memory conversation history. |
| `03.building-search-applications` | Rank sample documents using embeddings and cosine similarity. |
| `04.integrating-with-function-calling` | Call a sample course-search function and return its results to the model. |
| `05.rag-and-vector-databases` | Store document embeddings in Supabase and answer questions using retrieved context. |
| `06.ai-agents` | Use a tool-calling loop to retrieve a learning profile and search for courses. |

## Setup

Create and activate a virtual environment from the project root (macOS/Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

`requirements.txt` pins the three direct dependencies. Their transitive
dependencies are installed automatically and are not pinned separately.

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key

# Required only for example 05
SUPABASE_URL=https://your_project.supabase.co
SUPABASE_KEY=your_supabase_api_key
```

Keep `.env` out of version control. It is already listed in `.gitignore`.

## Run the Examples

Run these commands from the project root.

### 01. Text Generation

Generate a response to a fixed prompt:

```bash
python 01.text-generation/app.py
```

Create a study explanation based on a topic and skill level:

```bash
python 01.text-generation/app2.py
```

### 02. Chat Applications

```bash
python 02.building-chat-applications/app.py
```

Enter `exit` to stop the chatbot.
Conversation history is kept only while the program is running.

### 03. Semantic Search

```bash
python 03.building-search-applications/app.py
```

Enter a query to rank four sample documents by cosine similarity.
Document embeddings are generated again on each run.

### 04. Function Calling

```bash
python 04.integrating-with-function-calling/app.py
```

Example input:

> Find beginner Python courses for a student.

The course-search function returns sample data, not live course listings.

### 05. RAG and Vector Databases

Before running this example, configure your Supabase database with:

- The `vector` extension (pgvector).
- A `documents` table with `content` and `embedding` columns.
- A `match_documents` database function accepting `query_embedding`,
  `match_threshold`, and `match_count`.
- Permissions that allow the configured API key to insert and retrieve documents.

The embedding column must match the dimensions of the generated embeddings.
The search function must return a `content` field for each matched document.

Database setup SQL is not included in this repository.

To insert the sample document:

```bash
python 05.rag-and-vector-databases/ingest.py
```

To run the question-answering example:

```bash
python 05.rag-and-vector-databases/app.py
```

Both scripts import the shared Supabase client from `supabase_client.py`.

Currently, `app.py` also inserts the sample document before asking a question.
Running either script repeatedly can create duplicate documents; running
`ingest.py` first is not required for the current `app.py`.

### 06. AI Agents

```bash
python 06.ai-agents/app.py
```

Example input:

> Use my learning profile to recommend suitable courses.

The example provides two tools:

- `get_learning_profile`: Returns a fixed sample learning profile.
- `search_courses`: Returns sample courses based on product, role, and level.

The loop processes tool calls until the model returns a response without
function calls.

## Models Used in the Code

- Text generation: `gpt-5-nano`
- Embeddings: `text-embedding-3-small`

## Current Limitations

- Examples require network access and configured API credentials.
- Course listings and learning profiles are sample data.
- Example 04 prints an answer only when the model requests a function call.
- Example 06 submits tool results individually and does not batch multiple
  tool calls from the same response.
- The agent loop has no iteration limit.
