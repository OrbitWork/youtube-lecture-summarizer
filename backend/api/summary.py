from fastapi import APIRouter
from backend.models.schemas import SummaryRequest
from backend.core.summarizer import load_chunks, summarize_chunks

router = APIRouter()


@router.post("/summary")
def generate_summary(data: SummaryRequest):
    chunks = load_chunks(data.video_id)

    summary = summarize_chunks(
        chunks,
        mode=data.mode
    )

    return {
        "video_id": data.video_id,
        "mode": data.mode,
        "summary": summary
    }
