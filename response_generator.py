from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='ur')
    tts.save("response.mp3")
    os.system("start response.mp3")
