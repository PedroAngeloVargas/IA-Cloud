import requests
from .db import get_db, get_next_sequence, get_timestamp

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def send_message_to_openrouter(user_input):
    db = get_db()

    # Gera ID e timestamp para a pergunta
    pergunta_id = get_next_sequence("perguntas")
    hora = get_timestamp()

    db.perguntas.insert_one({
        "_id": pergunta_id,
        "mensagem": user_input,
        "timestamp": hora
    })

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    try:
        result = response.json()
    except Exception:
        erro = "Erro: resposta inválida da API."
        db.respostas.insert_one({
            "_id": pergunta_id,
            "mensagem": erro,
            "timestamp": get_timestamp()
        })
        return erro

    if "choices" in result:
        resposta = result["choices"][0]["message"]["content"]
        db.respostas.insert_one({
            "_id": pergunta_id,
            "mensagem": resposta,
            "timestamp": get_timestamp()
        })
        return resposta
    elif "error" in result:
        erro = result['error'].get('message', 'mensagem desconhecida')
        db.respostas.insert_one({
            "_id": pergunta_id,
            "mensagem": f"Erro da API: {erro}",
            "timestamp": get_timestamp()
        })
        return f"Erro da API: {erro}"
    else:
        erro = f"Erro inesperado: {result}"
        db.respostas.insert_one({
            "_id": pergunta_id,
            "mensagem": erro,
            "timestamp": get_timestamp()
        })
        return erro
