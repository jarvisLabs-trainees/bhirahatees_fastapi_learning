from gtts import gTTS;
import os;

def text_to_speech(sentence:str):
    tts = gTTS(text=sentence, lang='en',tld="com.br")
    tts.save("output.mp3")
    os.system("open output.mp3");
  

text_to_speech("hello world");
  