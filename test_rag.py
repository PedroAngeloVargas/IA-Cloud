import os
from app.models.rag.loader import load_json_documents
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def debug_relevance(question, documents):
    """
    Calcula e imprime a pontuação de relevância de todos os documentos
    em relação a uma pergunta, ordenados do mais relevante para o menos.
    """
    print(f"\n--- DEBUGANDO RELEVÂNCIA PARA A PERGUNTA: '{question}' ---")

    if not documents:
        print("Nenhum documento foi fornecido para análise.")
        return

    doc_embeddings = model.encode(documents, convert_to_tensor=True)
    question_embedding = model.encode(question, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(question_embedding, doc_embeddings)[0]

    results = zip(scores, documents)

    sorted_results = sorted(results, key=lambda x: x[0], reverse=True)

    print("\n--- RANKING DE RELEVÂNCIA ---")
    for i, (score, doc) in enumerate(sorted_results):
        print(f"{i+1}. Score: {score:.4f} | Documento: {doc}")
        if "PENA-DOURADA" in doc:
            print("    -> CÓDIGO SECRETO ENCONTRADO AQUI!")
    print("---------------------------------")


# --- BLOCO DE EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":

    DATA_DIR = "./app/models/data"

    documentos_carregados = load_json_documents(DATA_DIR)

    pergunta_teste = "Qual o item raro guardado no celeiro da Fazenda Jupiter?"

    debug_relevance(pergunta_teste, documentos_carregados)
