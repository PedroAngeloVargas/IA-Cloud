import os
import json

def load_json_documents(data_dir):
    documents = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    if isinstance(data, dict):
                        documents.append(json.dumps(data))
                    elif isinstance(data, list):
                        documents.extend([json.dumps(item) for item in data])
                except Exception as e:
                    print(f"Erro ao carregar {filename}: {e}")
    return documents