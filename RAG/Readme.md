# Learning RAG (Retrieval-Augmented Generation)

A hands-on repository for learning and experimenting with Retrieval-Augmented Generation (RAG) systems using modern LLMs, vector databases, embeddings, and retrieval techniques.

## Overview

This project explores the core concepts behind RAG pipelines, including:

* Document ingestion
* Text chunking
* Embedding generation
* Vector storage and similarity search
* Retrieval strategies
* Context augmentation
* LLM-powered question answering

The goal is to understand how external knowledge can be combined with Large Language Models (LLMs) to improve factual accuracy and reduce hallucinations.

---

## Learning Objectives

By working through this repository, you will learn:

* How RAG architectures work
* How embeddings represent semantic meaning
* How vector databases enable efficient retrieval
* Different chunking strategies and their trade-offs
* Prompt engineering for RAG applications
* Evaluation and optimization techniques
* Best practices for building production-ready RAG systems

---

## RAG Pipeline

```text
Documents
    ↓
Loading
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Context Retrieval
    ↓
LLM Prompt
    ↓
Generated Answer
```

---

## Sample Workflow

1. Load documents.
2. Split documents into chunks.
3. Generate embeddings.
4. Store embeddings in a vector database.
5. Retrieve relevant chunks for a query.
6. Pass retrieved context to an LLM.
7. Generate a grounded response.

---
