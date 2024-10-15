import streamlit as st
import time
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
from gtts import gTTS
from transformers import pipeline
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("turbo")


@st.cache_resource
def load_summarization_pipeline():
    return pipeline("summarization","facebook/bart-large-cnn")


@st.cache_resource
def load_tts_pipeline():
    return pipeline("text-to-speech", model="suno/bark")


summary_pipeline = load_summarization_pipeline()
tts_pipeline = load_tts_pipeline()

st.title("Sum-IT")

url = st.text_area("Enter YouTube Link")

if st.button("Transcribe"):
    # Download YouTube audio
    video = YouTube(url, on_progress_callback = on_progress)
    stream = video.streams.get_audio_only()
    stream.download(filename="audio_english.mp3")

    # Transcribe audio
    st.header("Video Transcription")
    my_bar = st.progress(0)

    model = load_whisper_model()
    result = model.transcribe("audio_english.mp3")
    transcription = result["text"]

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    st.success(transcription)

    # Summarize transcription
    st.header("Transcription Summary")
    summary = summary_pipeline(transcription)[0]["summary_text"]
    st.success(summary)

    # Generate audio summary
    st.header("Audio Summary")
    # speech = tts_pipeline(summary)
    # st.audio(speech['audio'], sample_rate=speech['sampling_rate'])
    tts = gTTS(text = summary, lang = 'en')
    tts.save("output.mp3")
    st.audio("output.mp3")

    # Clean up temporary files
    os.remove("audio_english.mp3")
    os.remove("output.mp3")
    # Uncomment the following line to add a download button for the summary
    # st.download_button('Download Summary', summary)