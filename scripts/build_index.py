import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore
from app.preprocessing.cleaner import clean_text
from app.preprocessing.tagger import telecom_tags
from app.config import *

embedder = Embedder(EMBEDDING_MODEL)
store = VectorStore(VECTOR_DIM)

with open("data/processed/telecom_cves.json") as f:
    data = json.load(f)

texts = []
processed = []

for d in data:
    c = clean_text(d["description"])
    tags = telecom_tags(c)

    rec = {
        "id": d["id"],
        "description": d["description"],
        "clean": c,
        "tags": tags
    }

    texts.append(c)
    processed.append(rec)

emb = embedder.encode(texts)
store.add(emb,processed)

print("Index built successfully with",len(processed),"records")
