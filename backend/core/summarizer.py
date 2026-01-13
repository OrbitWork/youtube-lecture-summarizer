import json
from openai import OpenAI

client = OpenAI()  # uses OPENAI_API_KEY


def load_chunks(video_id):
    with open(
        f"backend/data/chunks/{video_id}_chunks.json",
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def summarize_chunks(chunks, mode="tldr"):
    """
    mode: tldr | detailed | revision
    """

    combined_text = "\n\n".join(
        [f"- {chunk['text']}" for chunk in chunks]
    )

    if mode == "tldr":
        instruction = """
Create a concise TL;DR summary in 5–7 bullet points.
Focus on the core ideas only.
"""
    elif mode == "detailed":
        instruction = """
Create detailed, structured notes.
Use headings and bullet points.
Explain ideas clearly as if for exam preparation.
"""
    elif mode == "revision":
        instruction = """
Create crisp revision notes.
Include key ideas, definitions, and short points.
No explanations, only essentials.
"""
    else:
        raise ValueError("Invalid summary mode")

    prompt = f"""
You are a study assistant.
Generate content ONLY from the lecture below.

LECTURE CONTENT:
{combined_text}

TASK:
{instruction}

OUTPUT:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
