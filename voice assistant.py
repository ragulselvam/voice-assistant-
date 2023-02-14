

import random
import webbrowser
import pyttsx
import wikipedia
#import pyowm
#import pygame
#from pygame
import calendar
import datetime
import mixer
import PyDictionary
import speech_recognition as sr
import sys
#from PyDictionary import PyDictionary
#import os
from time import sleep
import requests

#from speech_recognition.__main__ import r, audio

engine = pyttsx.init();
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 5.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 10)

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is your name','How are you']
cmd1 = ['open browser', 'open Google','open Chrome']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open YouTube', 'I want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'bye','nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
brow = ['Google']
repfr9 = ['youre welcome', 'glad i could help you']
cmd10=['dictionary','find a meaning','Explanation']
cmd11=['open gmail','open Gmail']

n=sr.Recognizer()
i=sr.Recognizer()
d=sr.Recognizer()
g=sr.Recognizer()
v=sr.Recognizer()
with sr.Microphone() as source:
        print("Name:")
        n.adjust_for_ambient_noise(source)
        audio = n.listen(source)
        try:
            print(n.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('please wait')
        w=n.recognize_google(audio)
while True:
    f = datetime.datetime.now()
    r = sr.Recognizer()
    e = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print(w +" said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('please wait')
            engine.runAndWait()
    q=r.recognize_google(audio)
    if r.recognize_google(audio) in greetings:
           random_greeting = random.choice(greetings)
           print(random_greeting)
           engine.say(random_greeting)
           engine.runAndWait()
    elif r.recognize_google(audio) in question:
                engine.say('I am fine')
                engine.runAndWait()
                print('I am fine')
    elif r.recognize_google(audio) in var1:
                engine.say('I was made by edward')
                engine.runAndWait()
                reply = random.choice(var2)
                print(reply)
    elif r.recognize_google(audio) in cmd9:
                print(random.choice(repfr9))
                engine.say(random.choice(repfr9))
                engine.runAndWait()
    elif r.recognize_google(audio) in cmd7:
                print(random.choice(colrep))
                engine.say(random.choice(colrep))
                engine.runAndWait()
                print('It keeps changing every micro second')
                engine.say('It keeps changing every micro second')
                engine.runAndWait()
    elif r.recognize_google(audio) in cmd8:
                print(random.choice(colrep))
                engine.say(random.choice(colrep))
                engine.runAndWait()
                print('It keeps changing every micro second')
                engine.say('It keeps changing every micro second')
                engine.runAndWait()
    elif r.recognize_google(audio) in cmd2:
                mixer.init()
                mixer.music.load("song.wav")
                mixer.music.play()
    elif r.recognize_google(audio) in var4:
                engine.say('I am a bot, silly')
                engine.runAndWait()
    elif r.recognize_google(audio) in cmd4:
                #webbrowser.open('www.youtube.com')
                engine.say("What do you want to search about")
                with sr.Microphone() as source:
                    print("What do you  want  to search about:")
                    e.adjust_for_ambient_noise(source)
                    audio = e.listen(source)
                    try:
                        print("You said:- " + e.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('please wait')
                    word=e.recognize_google(audio)
                from googlesearch import search 
                query = e.recognize_google(audio)
                for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                    webbrowser.open_new_tab(j)
                    
    elif r.recognize_google(audio) in cmd6:
                print('see you later')
                engine.say('see you later')
                engine.runAndWait()
                sys.exit()
    elif r.recognize_google(audio) in cmd5:
                with sr.Microphone() as source:
                    engine.say("What's your location?")
                    engine.runAndWait()
                    print("What's your location?")   
                   
                    i.adjust_for_ambient_noise(source)
                    audio = i.listen(source)
                    try:
                        print(w +" said:- " + i.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('please wait')
                    t=i.recognize_google(audio)
                    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac33195fc69310433501681fc9729945'.format(t)
                    res=requests.get(url)
                    data=res.json()
                    #print(res)
                   # print(data)
                    if data["cod"] != "404":  
                        y = data["main"] 
                        current_temperature = y["temp"]  
                        current_pressure = y["pressure"] 
                        current_humidity = y["humidity"] 
                        z = data["weather"] 
                        weather_description = z[0]["description"] 
                        temp=current_temperature-273.15
                        print(" Temperature (in celsius) = "+str(temp)) 
                        print(" Pressure= "+str(current_pressure)) 
                        print(' Humidity= '+str(current_humidity)) 
                        print("weather_Description= "+str(weather_description)) 
                        engine.say(temp)
                        engine.runAndWait()
                        engine.say('humidity')
                        engine.runAndWait()
                        engine.say(current_humidity)
                        engine.runAndWait()
                        engine.say('Weather Description')
                        engine.runAndWait()
                        engine.say(weather_description)
                        engine.runAndWait()
                        engine.say('Pressure')
                        engine.runAndWait()
                        engine.say(current_pressure)
                        engine.runAndWait()
                    else: 
                        print(" City Not Found ") 
    elif r.recognize_google(audio) in var3:
                print  str(f)
              #  engine.say(f)
                engine.runAndWait()
    elif r.recognize_google(audio) in cmd1:
                webbrowser.open('www.google.com')
    elif 'alarm' in q:
                #hour1=00
                #minute1=36
                engine.say("When do you want to set alarm")
                engine.runAndWait()
                with sr.Microphone() as source:
                    print("When do you want to set alarm:")
                    e.adjust_for_ambient_noise(source)
                    audio = e.listen(source)
                    try:
                        print(w + "said:- " + e.recognize_google(audio))
                        word=e.recognize_google(audio)
                        if(word=='zero'):
                            word=0
                        word1=int(word)
                        hour1 ="%02d" % word1
                        hour2=str(hour1)
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('Please wait')
                engine.say("When do you want to set alarm")
                with sr.Microphone() as source:
                    print("When do you want to set alarm:")
                    e.adjust_for_ambient_noise(source)
                    audio = e.listen(source)
                    try:
                        print(w + "said:- " + e.recognize_google(audio))
                        word2=e.recognize_google(audio)
                        words=int(word2)
                        minute1 = "%02d" % words
                        #minute1:25
                        minute2=str(minute1)
                        print('Alarm set for: %s:%s' % (hour1,minute1))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                while True:
                    now = datetime.now()
                    hournow = now.hour
                    #print(hournow)
                    minnow = now.minute
                    if int(hournow) == int (hour1) and int(minnow) == int(minute1):
                        print("ALARM!")                                
                        mixer.init()
                        mixer.music.load("F:\movie\movies\videos\video\musics\Dhandiya.mp3")
                        mixer.music.play()
                        sleep(60000)
                    else:
                        break
    elif r.recognize_google(audio) in cmd11:
        
            webbrowser.open('www.google.com/gmail')
    elif r.recognize_google(audio) in cmd3:
                jokrep = random.choice(jokes)
                engine.say(jokrep)
                engine.runAndWait()
    elif 'order food' in q:
            webbrowser.open('www.swiggy.com')
    elif 'Google' in q:
                engine.say("What do you want to search about")
                engine.runAndWait()
                with sr.Microphone() as source:
                    print("What do you  want  to search about:")
                    e.adjust_for_ambient_noise(source)
                    audio = e.listen(source)
                    try:
                        print("You said:- " + e.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                    word=e.recognize_google(audio)
                    url='http://www.google.com/search?btnG=1&q='
                    k=word
                    j=url + word
                    print(k)
                    print(j)
                    webbrowser.open_new_tab(j)
    elif 'top news' in q:
                url='https://www.ndtv.com/top-stories'
                webbrowser.open_new_tab(url)
    elif 'news' in q:
                engine.say("What do you want to search about")
                with sr.Microphone() as source:
                    print("What do you  want  to search about:")
                    e.adjust_for_ambient_noise(source)
                    audio = e.listen(source)
                    try:
                        print("You said:- " + e.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                    word=e.recognize_google(audio)
                    url='https://www.ndtv.com/topic/'+word
                    webbrowser.open_new_tab(url)
    elif d.recognize_google(audio) in cmd10:
                engine.say("What word you want to find?")
                engine.runAndWait()
                with sr.Microphone() as source:
                    print('what word your looking for??')
                    d.adjust_for_ambient_noise(source)
                    audio=d.listen(source)
                    try:
                        print("You said:- " + d.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                    dictionary=PyDictionary()
                    s=d.recognize_google(audio)
                    print (dictionary.meaning(s))
                    engine.say(dictionary.meaning(s))
                    engine.runAndWait()
    elif "calendar" in q:
           with sr.Microphone() as source:
            print("Year:")
            v.adjust_for_ambient_noise(source)
            audio = v.listen(source)
            try:
                print(v.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
                engine.say('please wait')
            yy=int(v.recognize_google(audio))
            print(calendar.calendar(yy))
                    
    else:
                engine.say("please wait")
                engine.runAndWait()
                print(wikipedia.summary(r.recognize_google(audio)))
                engine.say(wikipedia.summary(r.recognize_google(audio)))
                engine.runAndWait()
                
                