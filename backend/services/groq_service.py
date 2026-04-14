from groq import Groq
from backend.config import Config
from services.prompt_templates import SYSTEM_PROMPT, build_user_prompt


_client = None


def get_client() -> Groq:
    global _client
    if _client is None:
        _client = Groq(api_key=Config.GROQ_API_KEY)
    return _client


def query_groq(user_input: str) -> str:
    """Send user query to Groq and return the AI response text."""
    client = get_client()
    completion = client.chat.completions.create(
        model=Config.GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": build_user_prompt(user_input)},
        ],
        temperature=0.3,
        max_tokens=1024,
    )
    return completion.choices[0].message.content.strip()
