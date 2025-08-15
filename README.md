# Elasticsearch Document Management with LLM Integration

## 📌 Overview
This project provides a complete workflow for managing documents in Elasticsearch, enhanced with Large Language Model (LLM) integration to automatically generate titles and keywords.  
It allows users to **add** documents with metadata or **query** them using multi-field full-text search.

## 🛠 Features
- **Add Mode**
  - Deletes and recreates a specified Elasticsearch index
  - Reads documents from a local file
  - Uses an LLM to:
    - Generate a descriptive title
    - Extract relevant keywords
  - Automatically generates:
    - Unique document ID
    - Random creator name
    - Random creation timestamp
  - Stores documents with metadata in Elasticsearch
- **Query Mode**
  - Counts documents in the index
  - Performs a full-text search across `title`, `keywords`, and `content` fields

---

## 📂 Project Structure
```
elasticsearch_project/
│
├── es/                  # Elasticsearch client and function wrappers
│   ├── es_client.py     # Initializes Elasticsearch client connection
│   ├── es_function.py   # CRUD operations and search helpers
│
├── helpers/             # Utility functions and prompts
│   ├── doc_helper.py    # Random data generation and file reading
│   ├── prompt.py        # Prompt templates for LLM
│
├── llm/                 # LLM client integration
│   ├── llm_client.py    # Calls to LLM for prompt processing
│
├── data/                # Sample document files
│
├── main.py              # Entry point for running Add or Query workflows
```

---

## ✨ Future Improvements

- [ ] Add multi-language support
- [ ] Combine Elasticsearch with Chroma vdb to perform preciser RAG function
