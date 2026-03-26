from fastapi import FastAPI
from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.rag.generator import generate_summary
from app.config import *

import json
from app.preprocessing.cleaner import clean_text
from app.preprocessing.tagger import telecom_tags

app = FastAPI()

# initialize models
embedder = Embedder(EMBEDDING_MODEL)
store = VectorStore(VECTOR_DIM)
retriever = Retriever(embedder, store)

# load dataset at startup
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "data/processed/telecom_cves.json")) as f:
#with open("data/processed/telecom_cves.json") as f:
    data = json.load(f)

texts = []
records = []

for d in data:
    c = clean_text(d["description"])
    tags = telecom_tags(c)

    rec = {
        "id": d["id"],
        "description": d["description"],
        "clean": c,
        "tags": tags,
        "cvss": d.get("cvss", None)
        
    }

    texts.append(c)
    records.append(rec)

emb = embedder.encode(texts)
store.add(emb, records)


@app.get("/")
def root():
    return {"message": "Telecom Threat Intelligence System Running"}


@app.post("/query")
def query_system(q: str):

    docs = retriever.retrieve(q, TOP_K)
    for d in docs:
        d["description"] = d["description"][:200] + "..."  # truncate for display
    summary = generate_summary(q, docs)

    return {
        "results": docs,
        "summary": summary
    }