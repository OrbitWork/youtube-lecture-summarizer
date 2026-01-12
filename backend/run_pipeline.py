from core.transcript import generate_transcript
from core.chunker import chunk_transcript
from core.embeddings import create_vector_store

YOUTUBE_URL = "https://youtu.be/FNgg3V6zI9I?si=TCGmuZcOi71JUKLS"
VIDEO_ID = "lecture_001"

transcript_path = generate_transcript(YOUTUBE_URL, VIDEO_ID)
chunk_path = chunk_transcript(transcript_path, VIDEO_ID)
create_vector_store(chunk_path, VIDEO_ID)

print("✅ Pipeline completed successfully")
