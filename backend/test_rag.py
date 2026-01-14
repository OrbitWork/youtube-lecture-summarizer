from core.rag import retrieve_relevant_chunks, generate_answer

VIDEO_ID = "lecture_001"

question = "What advice is given about interviews?"

chunks = retrieve_relevant_chunks(question, VIDEO_ID)

print("\nRetrieved Chunks:")
for c in chunks:
    print(f"\nScore: {c['score']:.3f}")
    print(c["text"][:300])
    print("-" * 60)

result = generate_answer(question, chunks)

print("\nFINAL ANSWER:\n")
print(result["answer"])

print("\nSOURCES:")
print(result["sources"])
