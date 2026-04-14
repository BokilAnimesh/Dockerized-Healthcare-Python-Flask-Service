# PharmaSafe AI 💊

> **AI-Powered Drug Safety Assistant** — Get accurate, structured drug side effects and safety insights instantly using Groq LLaMA AI.

---

## 🚀 Features

- 🤖 **Groq AI** (LLaMA 3) powered drug safety responses
- 📋 **Structured output** — Side effects, warnings, precautions
- 💬 **ChatGPT-style** chatbot interface
- 🗄️ **SQLite** chat history with sidebar
- 🎨 **Clean, minimal** medical UI

---

## 📁 Project Structure

```
pharmasafe-ai/
├── backend/
│   ├── app.py                  # Flask entry point
│   ├── config.py               # Environment config
│   ├── requirements.txt
│   ├── routes/
│   │   ├── chat.py             # POST /api/chat, /api/store-history
│   │   └── history.py          # GET /api/history
│   ├── services/
│   │   ├── groq_service.py     # Groq API client
│   │   ├── db_service.py       # SQLite helpers
│   │   └── prompt_templates.py # System + user prompt
│   └── database/
│       └── chat_history.db     # Auto-created on first run
│
├── frontend/
│   └── templates/
│       ├── index.html          # Landing page
│       ├── about.html          # About page
│       └── chatbot.html        # Chat interface
│
└── README.md
```

---

## ⚙️ Setup

### 1. Clone & navigate

```bash
git clone <repo-url>
cd pharmasafe-ai/backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file inside `backend/`

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama3-8b-8192
FLASK_DEBUG=true
```

> Get your free Groq API key at https://console.groq.com

### 4. Run the server

```bash
python app.py
```

Open: **http://localhost:5000**

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/chat` | Send query, get AI response |
| `POST` | `/api/store-history` | Manually store a chat entry |
| `GET`  | `/api/history` | Retrieve past chats |

### POST `/api/chat`
```json
{ "query": "Ibuprofen side effects" }
```
Response:
```json
{ "response": "Drug Name: Ibuprofen\n\nCommon Side Effects:\n- ..." }
```

---

## 🎨 Design System

| Token | Value |
|-------|-------|
| Primary | `#2563EB` (Medical Blue) |
| Background | `#F8FAFC` |
| Text | `#0F172A` |
| Font | DM Serif Display + DM Sans |

---

## ⚕️ Disclaimer

PharmaSafe AI is for **informational purposes only**. It does not replace professional medical advice. Always consult a qualified healthcare provider.