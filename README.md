# 🕹️ Lazy Gamer Helper

**Smart and modular game recommender** — a RAG-based assistant that analyzes your library, understands your tastes, and suggests what to play next.

[![Status](https://img.shields.io/badge/status-in%20development-yellow)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Python](https://img.shields.io/badge/python-3.13+-green)]()

---

## 📖 Overview

**Lazy Gamer Helper** is an open-source project in active development that combines **RAG (Retrieval-Augmented Generation)**, relational and semantic databases, and **local language models** to deliver **personalized game recommendations** based on your library.

The system gathers and processes data from your **Steam** account (with planned support for other stores), enriches metadata using **AI models**, and builds a **semantic and vector graph** that enables complex, context-aware queries and responses.

- Swap the AI model (Gemma, Mistral, Llama, etc.);
- Add new game stores;
- Expand external data sources with custom connectors;
- Extend logical and semantic reasoning via new modules.

The project is designed to be **modular and extensible**.  
New integrations (such as stores, data sources, databases, or AI models) can be easily added by **implementing the base class interfaces**.

---

### Core Modules

| Module | Function | Status |
|--------|-----------|--------|
| **Data** | Collects and processes Steam data (descriptions, tags, playtime) | ✅ In progress |
| **LLM Tagging** | Generates tags and descriptive synthesis using local models (Ollama / DeepSeek) | ⚙️ In development |
| **MongoDB** | Stores raw and processed data | ✅ In progress |
| **ChromaDB** | Lexical processing and vector embeddings | 🚧 Prototype |
| **Neo4j** | Graph of relationships between games and players | 🚧 Prototype |
| **LangChain + Ollama** | RAG pipeline and recommendation generation | 🚧 Prototype |
| **Future Extensions** | Support for Epic Games, GOG, PlayStation, Xbox, and more | 🧩 Planned |

---

## 🧱 Core Technologies

- **Python 3.13+**
- **LangChain**
- **Ollama / DeepSeek / Gemma**
- **MongoDB**
- **ChromaDB**
- **Neo4j**
- **Podman**
- **Poetry**

---

📜 **License**

Distributed under the **MIT License**.  
Feel free to use, modify, and contribute.




---
Usefull links:
- https://steamapi.xpaw.me/#IFamilyGroupsService/GetSharedLibraryApps
