import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
from urllib.request import URLopener 
from urllib.request import urlopen

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    # uname = takeCommand()
    speak('Hello. How should i call you ')
    uname = takeCommand()
    speak('Welcome ' +  uname)
    
    columns = shutil.get_terminal_size().columns

    print('##########################'.center(columns))
    print('Welcome ', uname.center(columns))
    print('##########################'.center(columns))
    hour = int(datetime.datetime.now().hour)
    if hour >= 0  and hour <12:
        speak('Good Morning ! ')
        speak(uname)
    elif hour>= 12 and hour<18:
        speak('Good Afternoon !')
        speak(uname)
    else:
        speak('Good Evening !' + uname)
        
    assname =('Lai or in spanish Leea')
    speak('I am your Assistant' + assname)
    speak('How can i help you, ' + uname)


# def username():
#     speak('Hello. How should i call you ')
#     uname = takeCommand()
#     speak('Welcome ' +  uname)
    
#     columns = shutil.get_terminal_size().columns

#     print('##########################'.center(columns))
#     print('Welcome ', uname.center(columns))
#     print('##########################'.center(columns))
    

def takeCommand():

    r = sr.Recognizer()
    while True: 
        try:
            with sr.Microphone() as source:

                print('Listening...')
                time.sleep(0)
                audio = r.listen(source)
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)

                print('Recognizing...')
                query = r.recognize_google(audio, language = 'es-Es' 'en-Gb', show_all=False)
                print(f'User said:{query}\n')
    
        except Exception as e:
            print(e)
            print('Unable to Recognize your voice.')
            speak('Unable to Recognize your voice, could you repeat again, please')
            
            r = sr.Recognizer()
            time.sleep(0)
            continue
        
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('', '')
    server.sendmail('', to, content)
    server.close()


if __name__=='__main__':
    clear = lambda: os.system('clear')
    clear()
    # username()
    wishMe()
    
    while True: 

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            # result=wikipedia.set_lang('es')
            results = wikipedia.summary(query, sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak('Here you go to Youtube\n')
            webbrowser.open('youtube.com')
            
        
