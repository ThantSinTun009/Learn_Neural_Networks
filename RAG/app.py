from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# # Example usage
# if __name__ == "__main__":
#     docs = load_all_documents("data")
#     print(f"Loaded {len(docs)} documents.")
#     print("Example document:", docs[0] if docs else None)


# # Example usage (chunk & vectorize)
# if __name__ == "__main__":
    
#     docs = load_all_documents("data")
#     emb_pipe = EmbeddingPipeline()
#     chunks = emb_pipe.chunk_documents(docs)
#     embeddings = emb_pipe.embed_chunks(chunks)
#     print("[INFO] Example embedding:", embeddings[0] if len(embeddings) > 0 else None)
    
    
# # Example usage (Vector Store)
# if __name__ == "__main__":
#     from src.data_loader import load_all_documents
#     docs = load_all_documents("data")
#     store = FaissVectorStore("faiss_store")
#     store.build_from_documents(docs)
#     store.load()
#     print(store.query("What is attention mechanism?", top_k=3))
    
    
# Example usage (search, LLMs)
if __name__ == "__main__":
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)