from audioop import add
from email.mime import audio
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os
def sptext():
    recogniszer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recogniszer.adjust_for_ambient_noise(source)
        audio =recogniszer.listen(source)
        try:
            print("recognizing....")
            data = recogniszer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not Understanding")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()


if __name__=="__main__":

    #if sptext().lower() =="jarvis":
        data1 = sptext().lower()
        if  "your name" in data1:
            name = " my name is kalyug"
            speechtx(name)
        elif " old are you" in data1:
            age = " i am human i am program avanish mishra is my genretor "
            speechtx(age)

        elif " phone" in data1:
            phone = " you have two number first is 6306844234 and second one 6306971011 but its currently in not working"
            speechtx(phone)

        elif "gmail" in data1:
            gmail = " you  have 3 gmail is avanishm141@gmail.com , mishraavanish708@gmail.com"
            speechtx(gmail)

        elif "bag" in data1:
            bag = " you were keep your bag on the table last night pleace check it once"
            speechtx(bag)

        elif "tell me " in data1:
            tell = " i am a program which is written by avanish mishra i am assistent of avanish mishra"
            speechtx(tell)

        elif "time" in data1:
            time= datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)

        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")

        elif "link" in data1:
            webbrowser.open("https://www.linkedin.com/in/avanish-mishra-08744a240")
            
        elif "facebook" in data1:
            webbrowser.open("https://www.facebook.com/profile.php?id=100068779033489")  


        elif "google" in data1:
            webbrowser.open("http://www.google.com")

        elif " youtube video" in data1:
            webbrowser.open("https://www.youtube.com/watch?v=uubofzOBWkQ")
            
        
            
    #else:
     #   print("thanks")
