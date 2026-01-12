import faiss
import json
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("backend/data/embeddings/lecture_001.index")

with open("backend/data/embeddings/lecture_001_meta.json", "r") as f:
    metadata = json.load(f)

query = "What is the speaker talking about?"

query_embedding = model.encode([query])
faiss.normalize_L2(query_embedding)

D, I = index.search(query_embedding, k=2)

print("Top matching chunks:\n")
for score, idx in zip(D[0], I[0]):
    # FAISS invalid score check
    if score < 0 or score == float("-inf"):
        continue

    print(f"\nScore: {score:.4f}")
    print(metadata[idx]["text"][:400])
    print("-" * 80)

