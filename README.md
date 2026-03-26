# Telecom Threat Intelligence System RAG

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
