import winsound
import speech_recognition as sr 
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()
def record(ask=False):
    if ask:
        alexis_speech(ask)

    with sr.Microphone() as source:
        
        #listening from microphone
        audio = r.listen(source)
        #recognizing the audio
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            alexis_speech('sorry cant recognize')
        except sr.RequestError:
            alexis_speech('sorry my speech is down')
    return voice_data
def alexis_speech(audio_string):
    tts = gTTS(text=audio_string,lang='en',slow=False)
    r = random.randint(1,10000)
    audio_file = 'audio-'+ str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def response(voice_data):
    if 'what is your name' in voice_data:
        alexis_speech('my name is alexa')
    if 'what is the time' in voice_data:
        alexis_speech(ctime())
    if 'search' in voice_data:
        search = record('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speech('here  is what i found for ' + search)
    if 'find location' in voice_data:
        location = record('which location do you want?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speech('here  is the location for' + location)
    if 'exit' in voice_data:
        record('It is nice talking to you...')
        exit()
alexis_speech('how can i help you...')
while True:
    audio = record()
    response(audio)