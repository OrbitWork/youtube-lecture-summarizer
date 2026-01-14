import yt_dlp
import whisper
import os
import json

TRANSCRIPT_DIR = "backend/data/transcripts"
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

def download_audio(youtube_url, output_path="audio.mp3"):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "quiet": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["segments"]

def save_transcript(segments, video_id):
    file_path = os.path.join(TRANSCRIPT_DIR, f"{video_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(segments, f, indent=2)
    return file_path

def generate_transcript(youtube_url, video_id):
    audio_path = f"{video_id}.mp3"
    download_audio(youtube_url, audio_path)
    segments = transcribe_audio(audio_path)
    os.remove(audio_path)
    return save_transcript(segments, video_id)
