import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, send_from_directory
from flask_cors import CORS
from config import Config
from services.db_service import init_db
from routes.chat import chat_bp
from routes.history import history_bp

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "..", "frontend", "templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "..", "frontend", "static"),
)
CORS(app)

# Register blueprints
app.register_blueprint(chat_bp,    url_prefix="/api")
app.register_blueprint(history_bp, url_prefix="/api")

# Serve frontend pages
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=Config.DEBUG, port=5000)
