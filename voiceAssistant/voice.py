import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

r = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def handle_command(command):
    if 'hello' in command:
        speak("Hi, how can I help you?")
    elif 'what time is it' in command:
        now = datetime.datetime.now()
        speak("The time is " + now.strftime("%I:%M %p"))
    elif 'wikipedia' in command:
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
    elif 'open code' in command:
        os.startfile("C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
speak("Hi, I'm your voice assistant. How can I help you?")

while True:
    command = listen()
    if command:
        handle_command(command)
  

