# app/models/api.py

import requests
import json
from .db import get_db, get_next_sequence, get_timestamp

API_KEY = ""
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# --- FUNÇÃO CORRIGIDA QUE ACEITA 2 ARGUMENTOS ---
def send_message_to_openrouter(pergunta_original, contexto):
    db = get_db()
    pergunta_id = get_next_sequence("perguntas")
    hora = get_timestamp()

    # Salva a pergunta original do usuário no banco
    db.perguntas.insert_one({
        "_id": pergunta_id,
        "mensagem": pergunta_original,
        "timestamp": hora
    })

    # --- LÓGICA DE PROMPT CORRIGIDA ---
    instrucao_sistema = """
    Você é um assistente de chatbot para um sistema de agronegócio.
    Use estritamente o CONTEXTO fornecido para responder à PERGUNTA do usuário.
    Não use nenhum conhecimento externo. Se a resposta não estiver no CONTEXTO,
    diga exatamente: 'Não encontrei essa informação nos meus documentos.'
    """
    prompt_usuario = f"CONTEXTO:\n{contexto}\n\nPERGUNTA:\n{pergunta_original}"
    messages = [
        {"role": "system", "content": instrucao_sistema},
        {"role": "user", "content": prompt_usuario}
    ]
    if not contexto:
        messages = [{"role": "user", "content": pergunta_original}]

    # --- MONTAGEM DO REQUEST ---
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": messages
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.RequestException as e:
        erro = f"Erro de conexão com a API: {e}"
        return erro
    except json.JSONDecodeError:
        erro = "Erro: resposta da API não é um JSON válido."
        return erro

    # --- PROCESSAMENTO DA RESPOSTA ---
    if "choices" in result:
        resposta = result["choices"][0]["message"]["content"]
        db.respostas.insert_one({"_id": pergunta_id, "mensagem": resposta, "timestamp": get_timestamp()})
        return resposta
    elif "error" in result:
        erro = result['error'].get('message', 'mensagem desconhecida')
        db.respostas.insert_one({"_id": pergunta_id, "mensagem": f"Erro da API: {erro}", "timestamp": get_timestamp()})
        return f"Erro da API: {erro}"
    else:
        erro = f"Erro inesperado: {result}"
        db.respostas.insert_one({"_id": pergunta_id, "mensagem": erro, "timestamp": get_timestamp()})
        return erro