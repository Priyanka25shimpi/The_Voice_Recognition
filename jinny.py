from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    
    speak("Hello, I am Jinny, your assistant. how may I help you!")

def takeCommand():
    #it takes microphone input from user and returns as a string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        
        
        print("say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    while True:         #this step will lead your code to run infinitely, so don't operate likewise.
    # if 1:
        query = takeCommand().lower()
        
        #Logic of executing tasks based on query
        if 'wikipedia' in query:
            print("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'e:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)