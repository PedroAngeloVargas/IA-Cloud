from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_relevant_chunks(question, documents, top_k=1):
    doc_embeddings = model.encode(documents, convert_to_tensor=True)
    question_embedding = model.encode(question, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(question_embedding, doc_embeddings)[0]
    top_results = scores.topk(top_k)

    relevant_chunks = [documents[idx] for idx in top_results.indices]
    return relevant_chunks


def debug_relevance(question, documents):
    print(f"\n--- DEBUGANDO RELEVÂNCIA PARA A PERGUNTA: '{question}' ---")
    
    doc_embeddings = model.encode(documents, convert_to_tensor=True)
    question_embedding = model.encode(question, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(question_embedding, doc_embeddings)[0]
    
    results = zip(scores, documents)
    
    sorted_results = sorted(results, key=lambda x: x[0], reverse=True)
    
    for score, doc in sorted_results:
        print(f"Score: {score:.4f} | Documento: {doc}")

from app.models.rag.loader import load_json_documents

def test_relevance_system():
    DATA_DIR = "./app/models/data" 
    docs = load_json_documents(DATA_DIR)
    pergunta = "Qual o código secreto da Fazenda Júpiter?"
    debug_relevance(pergunta, docs)

if __name__ == "__main__":
    test_relevance_system()