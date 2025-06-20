from flask import Blueprint, render_template, request, jsonify
from app.models.api import send_message_to_openrouter

chat_bp = Blueprint('chat', __name__)

@chat_bp.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.json.get("message")
        response = send_message_to_openrouter(user_input)
        return jsonify({"response": response})

    return render_template("chat.html")
