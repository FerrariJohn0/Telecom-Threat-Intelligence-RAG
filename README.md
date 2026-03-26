# Telecom Threat Intelligence System RAG
## Overview
This project implements a Retrieval-Augmented Generation (RAG) system for telecom cybersecurity vulnerability analysis.

## Features
- Semantic search using embeddings
- FAISS vector database
- FastAPI backend
- Telecom vulnerability filtering (NVD)


## API Docs
http://localhost:8000/docs

## Example Query
critical 5g vulnerability

# 🚀 Telecom Threat Intelligence System using RAG

An **AI-powered Threat Intelligence System** designed to analyze and retrieve telecom-related cybersecurity vulnerabilities using **Retrieval-Augmented Generation (RAG)**, **semantic search**, and **vector databases (FAISS)**.

---

## 📌 Overview

Modern telecom networks (5G, LTE, mobile infrastructure) are highly vulnerable to cyber threats. Traditional keyword-based systems fail to capture semantic meaning and often miss critical vulnerabilities.

This project solves that problem by:

✔ Using **semantic embeddings** to understand query meaning  
✔ Retrieving relevant vulnerabilities from **NVD (CVE dataset)**  
✔ Generating intelligent summaries using **RAG architecture**  

---

## 🧠 Key Features

- 🔍 **Semantic Search (Not Keyword-Based)**
- ⚡ **Fast Retrieval using FAISS Vector Database**
- 🤖 **RAG-Based Intelligent Summarization**
- 🌐 **FastAPI Backend with Swagger UI**
- 📊 **Top-K Vulnerability Retrieval**
- 🏷️ **Telecom-specific tagging (5G, LTE, Core Network, etc.)**

---

## 🏗️ System Architecture

---

## ⚙️ Tech Stack

| Category | Technology |
|--------|-----------|
| Language | Python |
| Backend | FastAPI |
| ML/NLP | Sentence Transformers |
| Vector DB | FAISS |
| Dataset | NVD (CVE JSON) |
| API UI | Swagger UI |
| Server | Uvicorn |

---

## 📂 Project Structure

---

## 🚀 How to Run the Project

### Implementation

```bash
git clone https://github.com/your-username/telecom-threat-intelligence-rag.git
cd telecom-threat-intelligence-rag

##  Crete a Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

## Install dependencies
pip install -r requirements.txt

## Prepare dataset
python scripts/extract_telecom_cves.py

##Build Vector Index
python scripts/build_index.py

##Run Fast API
uvicorn app.main:app --reload