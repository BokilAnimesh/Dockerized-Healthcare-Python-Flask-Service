import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL   = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), "database", "chat_history.db")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
