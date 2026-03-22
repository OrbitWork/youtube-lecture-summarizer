import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# CONFIG
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
SIMILARITY_THRESHOLD = 0.20
TOP_K = 3

model = SentenceTransformer(EMBEDDING_MODEL)

def load_vector_store(video_id):
    index = faiss.read_index(f"backend/data/embeddings/{video_id}.index")
    with open(f"backend/data/embeddings/{video_id}_meta.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    return index, metadata


def retrieve_relevant_chunks(query, video_id):
    index, metadata = load_vector_store(video_id)

    query_embedding = model.encode([query])
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, TOP_K)

    relevant_chunks = []

    for score, idx in zip(scores[0], indices[0]):
        if score < SIMILARITY_THRESHOLD:
            continue

        relevant_chunks.append({
            "score": float(score),
            "text": metadata[idx]["text"],
            "start": metadata[idx]["start"],
            "end": metadata[idx]["end"]
        })

    return relevant_chunks

