from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://root:12345@172.24.0.2/admin")

db = client["chat_db"]

def get_db():
    return db

def get_next_sequence(name):
    """Incrementa e retorna o próximo ID para a coleção especificada."""
    counters = db["counters"]
    counter = counters.find_one_and_update(
        {"_id": name},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=True
    )
    return counter["seq"]

def get_timestamp():
    """Retorna a data e hora atual formatada."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

