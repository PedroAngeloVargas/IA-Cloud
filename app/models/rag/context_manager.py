import os
from app.models.rag.loader import load_json_documents
from app.models.rag.retriever import get_relevant_chunks
import json
from .loader import load_json_documents
from .retriever import get_relevant_chunks

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

def build_context(question):
    # --- INÍCIO DO CÓDIGO DE DEBUG ---
    try:

        data_dir_path = os.path.join(os.path.dirname(__file__), '..', 'data')
        

        absolute_path = os.path.abspath(data_dir_path)
        
        print("\n--- DEBUG DE CAMINHO DO RAG ---")
        print(f"Caminho absoluto que estou tentando acessar: {absolute_path}")
        

        is_dir = os.path.isdir(absolute_path)
        print(f"O caminho acima é um diretório válido? {is_dir}")
        
   
        if is_dir:
            print(f"Conteúdo encontrado no diretório: {os.listdir(absolute_path)}")
        
        print("---------------------------------\n")

    except Exception as e:
        print(f"\n--- ERRO CRÍTICO NO DEBUG DE CAMINHO: {e} ---\n")
    # --- FIM DO CÓDIGO DE DEBUG ---

    docs = load_json_documents(data_dir_path)
    if not docs:
        return ""
    
    relevant_parts = get_relevant_chunks(question, docs, top_k=1)
    
    if not relevant_parts:
        return ""

    try:
        json_string = relevant_parts[0]
        data = json.loads(json_string)
        clean_context = data.get('descricao', '')
        return clean_context
    except (json.JSONDecodeError, IndexError) as e:
        print(f"Erro ao extrair contexto: {e}")
        return "\n".join(relevant_parts)