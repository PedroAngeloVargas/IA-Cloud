from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from app.models.api import send_message_to_openrouter
from app.utils.auth import login_required


# Criando o blueprint do chat
chat_bp = Blueprint('chat', __name__)

# Rota principal do chat
@chat_bp.route("/", methods=["GET", "POST"])
@login_required
def chat():
    if request.method == "POST":
        user_input = request.json.get("mensagem")  # deve bater com o JS
        resposta = send_message_to_openrouter(user_input)
        return jsonify({"mensagem": resposta})  # chave 'mensagem' para JS

    return render_template("chat.html", usuario=session.get("usuario"))
