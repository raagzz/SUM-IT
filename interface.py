#importing Packages
import openai
import streamlit as st
import whisper
import time
import os
from pytube import YouTube
from gtts import gTTS


#dependices
model = whisper.load_model("base")
openai.api_key="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" #API key

st.title("Sum-IT")
#create text area widgets
url = st.text_area("Enter YouTube Link")

if st.button("Transcribe"):
    #youtube video to text
    video = YouTube(url)

    stream = video.streams.filter(only_audio=True)[0]
    stream.download(filename="audio_english.mp3")

    result = model.transcribe("audio_english.mp3")
    sum_text = result["text"]
    st.header("Video Transcription")
    
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    
    st.success(sum_text)
    
    #creating a button and generating output
    #GPT3 - To Generate the summary
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = "Please Summarise this paragraph for me in the few sentences: "+sum_text,
        max_tokens = 512,
        temperature = 0.8)

    result = response["choices"][0]["text"]
    st.header("Transcription Summary")
    st.success(result)
    
    st.header("Audio Summary")
    tts = gTTS(text = result, lang = 'en')
    tts.save("output.mp3")
    st.audio("output.mp3")

    
#Give user the options to download the summarized file
#t.download_button('Download-Result',result)