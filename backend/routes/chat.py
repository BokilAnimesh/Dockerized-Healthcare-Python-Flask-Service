from flask import Blueprint, request, jsonify
from services.groq_service import query_groq
from services.db_service import save_chat

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_query = (data.get("query") or "").strip()

    if not user_query:
        return jsonify({"error": "Query cannot be empty."}), 400

    try:
        bot_response = query_groq(user_query)
        save_chat(user_query, bot_response)
        return jsonify({"response": bot_response}), 200
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@chat_bp.route("/store-history", methods=["POST"])
def store_history():
    data = request.get_json(silent=True) or {}
    user_query   = (data.get("user_query") or "").strip()
    bot_response = (data.get("bot_response") or "").strip()

    if not user_query or not bot_response:
        return jsonify({"error": "Both user_query and bot_response are required."}), 400

    save_chat(user_query, bot_response)
    return jsonify({"message": "Stored successfully."}), 201
