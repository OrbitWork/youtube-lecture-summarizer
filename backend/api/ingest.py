from fastapi import APIRouter
from backend.models.schemas import IngestRequest
from backend.core.transcript import generate_transcript
from backend.core.chunker import chunk_transcript
from backend.core.embeddings import create_vector_store


router = APIRouter()


@router.post("/ingest")
def ingest_video(data: IngestRequest):
    transcript_path = generate_transcript(
        data.youtube_url,
        data.video_id
    )

    chunk_path = chunk_transcript(
        transcript_path,
        data.video_id
    )

    create_vector_store(
        chunk_path,
        data.video_id
    )

    return {
        "status": "success",
        "video_id": data.video_id
    }
