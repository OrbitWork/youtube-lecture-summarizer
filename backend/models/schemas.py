from pydantic import BaseModel


class IngestRequest(BaseModel):
    youtube_url: str
    video_id: str


class QuestionRequest(BaseModel):
    video_id: str
    question: str


class SummaryRequest(BaseModel):
    video_id: str
    mode: str  # tldr | detailed | revision
