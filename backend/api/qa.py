from fastapi import APIRouter
from backend.models.schemas import QuestionRequest
from backend.core.rag import retrieve_relevant_chunks, generate_answer

router = APIRouter()


@router.post("/ask")
def ask_question(data: QuestionRequest):
    chunks = retrieve_relevant_chunks(
        data.question,
        data.video_id
    )

    result = generate_answer(
        data.question,
        chunks
    )

    return result
