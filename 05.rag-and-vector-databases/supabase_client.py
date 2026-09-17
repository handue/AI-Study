import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(
    supabase_url=os.getenv("SUPABASE_URL"),
    supabase_key=os.getenv("SUPABASE_KEY"),
)
