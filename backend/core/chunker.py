import json
import os

CHUNK_DIR = "backend/data/chunks"
os.makedirs(CHUNK_DIR, exist_ok=True)

CHUNK_DURATION = 300  # seconds (5 mins)

def chunk_transcript(transcript_path, video_id):
    with open(transcript_path, "r", encoding="utf-8") as f:
        segments = json.load(f)

    chunks = []
    current_chunk = []
    start_time = segments[0]["start"]

    for seg in segments:
        current_chunk.append(seg["text"])
        if seg["end"] - start_time >= CHUNK_DURATION:
            chunks.append({
                "start": start_time,
                "end": seg["end"],
                "text": " ".join(current_chunk)
            })
            current_chunk = []
            start_time = seg["end"]

    if current_chunk:
        chunks.append({
            "start": start_time,
            "end": segments[-1]["end"],
            "text": " ".join(current_chunk)
        })

    output_path = os.path.join(CHUNK_DIR, f"{video_id}_chunks.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    return output_path
