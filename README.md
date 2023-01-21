# <b>SUM-IT</b>: Video Summarizing AI Tool
## <b>Winning Hackathon Solution - ICamp</b>
## <b>Table of contents</b>
- A brief introduction
- Components
- How does it works?

## <b>A brief introduction</b>
There are innumerable videos on YouTube that are too long for us to watch and process fully. Most of us do not have the time nor the attention span to absorb information from the videos we watch. To solve this problem, we have built a video summarizing application using Streamlit and Whisper-OpenAI and implemented it using ChatGPT’s API. This tool provides a short summary of videos that have a very long duration to make it easy for us to learn. 

## <b>Components</b>
- <b>Whisper</b> : 
Whisper is a feature of the OpenAI GPT-3 language model that allows for the generation of more subtle and nuanced language. Whisper was trained on 680,000 hours of multilingual and multitask supervised data collected from the web. One of the important characteristics of Whisper is the diversity of data used to train it.  A third of the training data is composed of non-English audio examples. Whisper can robustly transcribe English speech and perform at a state-of-the-art level with approximately 10 languages – as well as translation from those languages into English. It enables transcription in multiple languages, as well as translation from those languages into English. 

- <b>ChatGPT</b> :
Conversational AI is a central sub-field of Natural Language Processing that makes it possible for a human to have a conversation with a machine. Every time the human says or asks something to the AI, the whole conversation history is sent too, so the AI can have the context in memory and make relevant responses. Modern chatbots leverage conversational AI and can do more than simply having a conversation. For example, they can detect customer intents, search documents, understand the customer tone and adapt their own tone (anger, joy, sarcasm...). 
Until recently, chatbots have been very limited. But with the creation of huge modern models like GPT-3, GPT-J, and GPT-NeoX, it is now possible to easily create advanced chatbots that are both fluent and relevant

- <b> gTTS</b> : 
gTTS (Google Text-to-Speech) is a Python library and CLI tool to interface with Google Translate text-to-speech API.  There are several APIs available to convert text to speech in Python. One of such APIs is the Google Text to Speech API commonly known as the gTTS API. gTTS is a very easy to use tool which converts the text entered into audio which can be saved as an mp3 file. The gTTS API supports several languages including English, Hindi, Tamil, French, German and many more. The speech can be delivered in any one of the two available audio speeds, fast or slow.


## <b>How does it works?</b>
The Whisper architecture is a simple end-to-end approach, implemented as an encoder-decoder Transformer. Input audio is split into 30-second chunks, converted into a log-Mel spectrogram, and then passed into an encoder. A decoder is trained to predict the corresponding text caption, intermixed with special tokens that direct the single model to perform tasks such as language identification, phrase-level timestamps, multilingual speech transcription, and to-English speech translation. 

<img width="315" alt="workflow" src="https://user-images.githubusercontent.com/108980831/213866692-559b5d8c-66f4-460f-ab71-26ec6f9a6550.png">

