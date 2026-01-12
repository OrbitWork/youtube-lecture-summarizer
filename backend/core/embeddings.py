import json
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer

EMBEDDING_DIR = "backend/data/embeddings"
os.makedirs(EMBEDDING_DIR, exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(chunk_path, video_id):
    with open(chunk_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)

    dimension = embeddings.shape[1]
      # Normalize embeddings
    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlatIP(dimension)  # IP = cosine (after normalization)
    index.add(embeddings)

    faiss.write_index(index, f"{EMBEDDING_DIR}/{video_id}.index")

    with open(f"{EMBEDDING_DIR}/{video_id}_meta.json", "w") as f:
        json.dump(chunks, f, indent=2)

    return index
