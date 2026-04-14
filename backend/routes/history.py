from flask import Blueprint, jsonify, request
from services.db_service import get_all_chats

history_bp = Blueprint("history", __name__)


@history_bp.route("/history", methods=["GET"])
def history():
    limit = request.args.get("limit", 50, type=int)
    chats = get_all_chats(limit=limit)
    return jsonify({"history": chats}), 200
