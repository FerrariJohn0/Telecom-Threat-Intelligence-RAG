# Telecom Threat Intelligence System (RAG)

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system for telecom cybersecurity vulnerability analysis.

## Features
- Semantic search using embeddings
- FAISS vector database
- FastAPI backend
- Telecom vulnerability filtering (NVD)

## How to Run
```bash
pip install -r requirements.txt
python scripts/extract_telecom_cves.py
python scripts/build_vector_db.py
uvicorn app.main:app --reload
