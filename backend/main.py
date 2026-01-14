from fastapi import FastAPI
from backend.api import ingest, qa, summary

app = FastAPI(
    title="AI YouTube Lecture Summarizer",
    description="Summarize lectures, ask questions, and generate study notes",
    version="1.0.0"
)

app.include_router(ingest.router, prefix="/api")
app.include_router(qa.router, prefix="/api")
app.include_router(summary.router, prefix="/api")


@app.get("/")
def health_check():
    return {"status": "running"}
