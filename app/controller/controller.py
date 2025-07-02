from flask import Blueprint, render_template, request, jsonify
from app.models.api import send_message_to_openrouter
from app.models.rag.context_manager import build_context  

chat_bp = Blueprint('chat', __name__)

@chat_bp.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.json.get("message")
        contexto = build_context(user_input)

        if not contexto:
            prompt = user_input
        else:
            template_prompt = """
            Você é um assistente de chatbot para um sistema de agronegócio.
            Use estritamente o CONTEXTO fornecido abaixo para responder à PERGUNTA do usuário.
            Não use nenhum conhecimento externo.
            Se a resposta não estiver no CONTEXTO, diga exatamente: "Não encontrei essa informação nos meus documentos."

            CONTEXTO:
            {contexto_aqui}

            PERGUNTA:
            {pergunta_aqui}
            """
            prompt = template_prompt.format(contexto_aqui=contexto, pergunta_aqui=user_input)

        print(f"--- PROMPT FINAL ENVIADO PARA A API ---\n{prompt}\n---------------------------------------")

        response = send_message_to_openrouter(prompt)
        return jsonify({"response": response})

    return render_template("chat.html")