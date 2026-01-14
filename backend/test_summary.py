from core.summarizer import load_chunks, summarize_chunks

VIDEO_ID = "lecture_001"

chunks = load_chunks(VIDEO_ID)

print("\n===== TL;DR SUMMARY =====\n")
print(summarize_chunks(chunks, mode="tldr"))

print("\n===== DETAILED NOTES =====\n")
print(summarize_chunks(chunks, mode="detailed"))

print("\n===== REVISION NOTES =====\n")
print(summarize_chunks(chunks, mode="revision"))
