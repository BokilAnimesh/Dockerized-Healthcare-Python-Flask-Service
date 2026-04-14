import sqlite3
from datetime import datetime
from backend.config import Config


def get_connection():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            user_query TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp  TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_chat(user_query: str, bot_response: str):
    conn = get_connection()
    conn.execute(
        "INSERT INTO chat_history (user_query, bot_response, timestamp) VALUES (?, ?, ?)",
        (user_query, bot_response, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()


def get_all_chats(limit: int = 50):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM chat_history ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
