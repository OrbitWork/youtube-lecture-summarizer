# run_pipeline.py
import os
from summarizer import summarize_chunks

# Path to your chunked transcript files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHUNKS_DIR = os.path.join(BASE_DIR, "..", "data", "chunks")
CHUNKS_DIR = os.path.abspath(CHUNKS_DIR)

def load_chunks(directory):
    chunks = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
                chunks.append(f.read())
    return chunks
