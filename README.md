

# Explainable RAG – DataForge Prototype

This repository contains a **minimal working prototype** of an **Explainable Retrieval-Augmented Generation (RAG)** system developed as part of the **DataForge Challenge** by E-SUMMIT,IIT-Roorkee.

The system demonstrates how a language-model-based question answering pipeline can be made **transparent and interpretable** by grounding answers in retrieved documents and exposing a **lightweight knowledge graph** (entities and relationships) derived from the same evidence.

The current prototype is implemented on a **medical use case (Lung Cancer)** to highlight the importance of explainability in high-risk domains.

---

## ✨ Key Features

* Evidence-based question answering
* TF-IDF–based document retrieval
* Medical entity extraction from retrieved text
* Context-local knowledge graph construction
* Visual explanation graph (entities & relationships)
* Web-based UI for interaction and visualization

---

## 🧠 System Overview

**Pipeline:**

```
User Query
   → Document Retrieval
   → Relevant Text Chunks
   → Entity Extraction
   → Lightweight Knowledge Graph
   → Answer Generation
   → Answer + Structured Explanation
```

All components operate on the **same retrieved evidence**, ensuring correctness, consistency, and auditability.

---

## 📂 Project Structure

```
DataForge/
├── app.py                 # Flask application entry point
├── retrieval.py           # Document retrieval logic (TF-IDF)
├── entity_graph.py        # Entity extraction and graph construction
├── answer.py              # Answer generation logic   
├── templates/
│   └── index.html         # Web UI (answer, evidence, explanation graph)
    └── lung_cancer.txt    # corpus of data
├── graph.html             # Optional standalone graph visualization
├── requirements.txt       # Python dependencies

```

---

## 🚀 How to Run the Prototype

### 1️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Windows (PowerShell):**

```bash
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```bash
venv\Scripts\activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
python app.py
```

Then open your browser at:

```
http://127.0.0.1:5000
```

---

## 🖥️ Web Interface

The interface allows users to:

* Ask medical questions
* View the AI-generated answer
* Inspect retrieved evidence chunks with relevance scores
* Visualize the **explanation graph** showing entities and relationships

This directly reflects the explainable RAG design described in the accompanying technical report.

---

## ⚠️ Notes and Limitations

* The prototype is **intentionally simple** and optimized for interpretability, not performance
* The knowledge graph is **query-specific** and not persisted
* Entity extraction quality depends on retrieved text the most
* No external knowledge bases or complex reasoning are used

These trade-offs were made deliberately to preserve transparency and clarity...

---

## 🌐 Domain Generality

Although demonstrated on a medical dataset, the architecture is **domain-agnostic**.
By replacing the document corpus and entity schema, the same pipeline can be applied to legal, technical, or policy documents making it versatile for each approach and context.

---

## 📌 Submission Context

This repository accompanies the **DataForge Challenge submission** and serves as a **demonstration prototype** for the proposed explainable RAG system.


