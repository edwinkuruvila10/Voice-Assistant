import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print("voices[1].id")
engine.setProperty("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon")  

    else:
        speak("Good evening")

    speak("i am Don sir. please tell me how can i help you") 

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
          
        print("Say that again please...")
        return "None"  
    return query  
            
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password-here")
    server.sendmail("youremail@gmail.com", to, content)
    server.close() 



if __name__  == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")    

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = "D:\\Non Critical\\songs\\Favorite Songs2"
            songs = os.listdr(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir, the time is (strtime)")

        elif "Email to edwin" in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "edwinkuruvila089@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent") 
            except Exception as e:
                print(e)
                speak("sorry my friend edwin. i am not able to snd this email")     



