# Telecom Threat Intelligence System RAG
## Overview
This project implements a Retrieval-Augmented Generation (RAG) system for telecom cybersecurity vulnerability analysis.

## Features
- Semantic search using embeddings
- FAISS vector database
- FastAPI backend
- Telecom vulnerability filtering (NVD)
## Install
pip install -r requirements.txt

## Build Vector Index
python scripts/build_index.py

## Run API
uvicorn app.main:app --reload

## API Docs
http://localhost:8000/docs

## Example Query
critical 5g vulnerability
