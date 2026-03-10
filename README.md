# 🎬 YouTube Summarizer

> **Instantly summarize any YouTube video using AI — get the key points in seconds, not hours.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![AI Powered](https://img.shields.io/badge/AI-Powered-purple?style=flat-square&logo=openai)

---

## 📌 About

**YouTube Summarizer** is an AI-powered tool that takes any YouTube video URL and generates a clean, concise summary of its content. Whether it's a 3-hour lecture, a podcast, or a tutorial — get the gist in seconds.

No more scrubbing through long videos. Just paste the link and let AI do the work.

---

## ✨ Features

- 🔗 **Paste any YouTube URL** — works with videos of any length
- 🤖 **AI-generated summaries** — powered by LLM (OpenAI / Gemini / custom)
- 📝 **Key points extraction** — highlights the most important takeaways
- ⚡ **Fast & lightweight** — minimal dependencies, quick results
- 🌐 **Transcript-based** — uses YouTube transcripts/captions for accuracy
- 💾 **Export support** — save summaries as `.txt` or `.md`

---

## 🚀 Demo

```
Input:   https://www.youtube.com/watch?v=example123
Output:  📄 Summary generated in 3.2s

         🎯 Key Points:
         • The video covers the basics of machine learning...
         • It explains supervised vs unsupervised learning...
         • Key takeaway: Start with clean data before building models.
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9+ |
| Transcript Fetching | `youtube-transcript-api` |
| AI Summarization | OpenAI GPT / Google Gemini |
| CLI Interface | `argparse` |
| (Optional) Web UI | Streamlit / Flask |

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
# or
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 💻 Usage

### Command Line
```bash
python summarizer.py --url "https://www.youtube.com/watch?v=example"
```

### With options
```bash
# Save output to a file
python summarizer.py --url "https://www.youtube.com/watch?v=example" --output summary.md

# Set summary length (short / medium / detailed)
python summarizer.py --url "https://www.youtube.com/watch?v=example" --length detailed
```

### As a Python module
```python
from summarizer import YouTubeSummarizer

summarizer = YouTubeSummarizer()
result = summarizer.summarize("https://www.youtube.com/watch?v=example")
print(result)
```

---

## 📁 Project Structure

```
youtube-summarizer/
├── summarizer.py        # Main summarizer logic
├── transcript.py        # YouTube transcript fetching
├── ai_model.py          # AI API integration
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── outputs/             # Saved summaries (auto-created)
└── README.md
```

---

## 📦 Requirements

```
youtube-transcript-api
openai
python-dotenv
argparse
```

Install all at once:
```bash
pip install -r requirements.txt
```


---
the project is still in progress,until then stay tuned...
