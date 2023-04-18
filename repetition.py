#from dis import instruction
import time

import speech_recognition as sr
import pyttsx3 as p
from timerloader import timer_loader
from web_auto import *
from web_auto1 import *
from web_automation import *
from word import *
from google_search import *
from translation import *
from internet_speed_test import *
from whatsapp import *
from camera import camera
from digital_clock import *
#from repeat import first1
import sys 
from news import *
#from app_loader import *
from timerloader import timer_loader
from timerstopper import timer_stopper
from arduino_car_control import controller 
import keyboard as key
from pynput import keyboard
from winotify import Notification, audio
#from security_camera import *
#from introduce_jarvis import introduction, invention
import website_opener
from AppOpener import open as o
from security_camera import security
import os
import threading


def first():
    while True:
        with keyboard.Events() as events:
            # Block at most one second
            event = events.get(5.0)
            if event is None:
                print('You did not press a key within five second \n')
                pass
            else:
                #ppprint('Received event {}'.format(event))
                value = key.read_key()
                try:
                    if value == 'p':
                        print("activated deep sleep")
                        time.sleep(1)
                        toast = Notification(app_id="PROJECT JARVIS 2.5",
                                            title="DEEP SLEEP ACTIVATED",
                                            msg="Jarvis will come back in 10 minutes")
                        toast.set_audio(audio.Mail, loop=False)
                        toast.show()
                        time.sleep(600)
                        toast = Notification(app_id="PROJECT JARVIS 2.5",
                                            title="BACK ONLINE",
                                            msg="Jarvis is ready for commands")
                        toast.set_audio(audio.Reminder, loop=False)
                        toast.show()
                    if value =='d':
                        print("activated super deep sleep")
                        toast = Notification(app_id="PROJECT JARVIS 2.5",
                                            title="SUPER DEEP SLEEP ACTIVATED",
                                            msg="Jarvis will come back in 20 minutes")
                        toast.set_audio(audio.Mail, loop=False)
                        toast.show()
                        time.sleep(1200)
                        toast = Notification(app_id="PROJECT JARVIS 2.5",
                                            title="BACK ONLINE",
                                            msg="Jarvis is ready for commands")
                        toast.set_audio(audio.Reminder, loop=False)
                        toast.show()
                    else:
                        pass
                except:
                    pass
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...\n")
            r.adjust_for_ambient_noise(source)
            audio0 = r.listen(source)
            try:
                file1 = open("Text_Files/caching_data.txt", "a")
                text = r.recognize_google(audio0, language="en-in")
                text = text.lower()
                file1.write(text + "\n")
                file1.close()
                print(text)
            except sr.UnknownValueError as e:
                print("err1")
                first()
            except sr.RequestError as e:
                print("err2")
                first()
            except Exception as e:
                print("err3")
                first()
        if "jarvis" in text:
            jarvis_hotkey = text.replace("jarvis", "")
            print(jarvis_hotkey)

            if "hello" in jarvis_hotkey:
                print("Hello :) \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Hello Sir!")
                engine.runAndWait()
            
            if "how is everything going" in jarvis_hotkey:
                print("Going Good :)\n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Going good sir!")
                engine.runAndWait()
            
            if "how are you today" in jarvis_hotkey:
                print("I am good sir, thank you for asking, how are you ? \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("I am good sir, thank you for asking, how are you ?")
                engine.runAndWait()
                
            if "are you awake" in jarvis_hotkey:
                print("yes sir I am, ready for commands \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Yes sir I am, ready for commands")
                engine.runAndWait()
            
            if "i am good" in jarvis_hotkey:
                print("Good to hear it sir ! \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Good to hear it sir !")
                engine.runAndWait()
                
            if "good morning" in jarvis_hotkey:
                time_data_time = int(time.strftime("%H"))
                time_data = time.strftime("%p")
                print(time_data_time, time_data)
                if "AM" in time_data:
                    print("Good Morning! \n")
                    engine = p.init()
                    engine.setProperty("rate", 140)
                    engine.say("Good Morning sir !")
                    engine.runAndWait()
                if "PM" in time_data:
                    if time_data_time in list(range(12, 16)):
                        print("Its Good Afternoon \n")
                        engine = p.init()
                        engine.setProperty("rate", 140)
                        engine.say("Its Good Afternoon sir!")
                        engine.runAndWait()
                    if time_data_time >= 16:
                        print("Its Good Evening \n")
                        engine = p.init()
                        engine.setProperty("rate", 140)
                        engine.say("Its Good Evening sir !")
                        engine.runAndWait()

            if "good afternoon" in jarvis_hotkey:
                time_data_time = int(time.strftime("%H"))
                time_data = time.strftime("%p")
                print(time_data_time, time_data)
                if "AM" in time_data:
                    print("Its Good Morning \n")
                    engine = p.init()
                    engine.setProperty("rate", 140)
                    engine.say("Its Good Morning sir !")
                    engine.runAndWait()
                if "PM" in time_data:
                    if time_data_time in list(range(12, 16)):
                        print("Good Afternoon \n")
                        engine = p.init()
                        engine.setProperty("rate", 140)
                        engine.say("Good Afternoon sir !")
                        engine.runAndWait()
                    if time_data_time >= 16:
                        print("Its Good Evening \n")
                        engine = p.init()
                        engine.setProperty("rate", 140)
                        engine.say("Its Good Evening sir !")
                        engine.runAndWait()

            if "good evening" in jarvis_hotkey:
                time_data_time = int(time.strftime("%H"))
                time_data = time.strftime("%p")
                print(time_data_time, time_data)
                if "AM" in time_data:
                    print("Its Good Morning \n")
                    engine = p.init()
                    engine.setProperty("rate", 140)
                    engine.say("Its Good Morning sir !")
                    engine.runAndWait()
                if "PM" in time_data:
                    if time_data_time in list(range(12, 16)):
                        print("Its Good Afternoon \n")
                        engine = p.init()
                        engine.setProperty("rate", 140)
                        engine.say("Its Good Afternoon sir !")
                        engine.runAndWait()
                    if time_data_time >= 16:
                        print("Good Evening \n")
                        engine = p.init()
                        engine.setProperty("rate", 140)
                        engine.say("Good Evening sir !")
                        engine.runAndWait()

            if "sorry" in jarvis_hotkey:
                print("Its ok sir, everybody makes mistakes \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Its ok sir, everybody makes mistakes !")
                engine.runAndWait()

            if "thank you" in jarvis_hotkey:
                print("You are welcome sir ! \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("You are welcome sir !")
                engine.runAndWait()


            if "information" in jarvis_hotkey:
                information = jarvis_hotkey.replace("get information on", "")
                print(information + "\n")
                bot1 = info()
                bot1.get_info(information)

            
            if "review" in jarvis_hotkey:
                review = jarvis_hotkey.replace("get movie review on", "")
                print(review + "\n")
                bot2 = Movie()
                bot2.movie_review(review)
            if "reviews" in jarvis_hotkey:
                review = jarvis_hotkey.replace("get movie reviews on", "")
                print(review + "\n")
                bot2_1 = Movie()
                bot2_1.movie_review(review)

            if "music" or "song" in jarvis_hotkey:
                #music = jarvis_hotkey.replace("play the music of" or "play the song", "" ) #or jarvis_hotkey.replace("play music", "") or jarvis_hotkey.replace("play the song", "") or jarvis_hotkey.replace("play the song of", "")
                if "play the music of" in jarvis_hotkey:
                    music = jarvis_hotkey.replace("play the music of ", "")
                    print(music + "\n")
                    bot3_1 = Music()
                    bot3_1.play(music)
                if "play the music" in jarvis_hotkey:
                    music = jarvis_hotkey.replace("play the music", "")
                    print(music +"\n")
                    bot3_2 = Music()
                    bot3_2.play(music)
                if "play the song" in jarvis_hotkey:
                    music = jarvis_hotkey.replace("play the song", "")
                    print(music + "\n")
                    bot3_3 = Music()
                    bot3_3.play(music)
                if "play the song of" in jarvis_hotkey:
                    music = jarvis_hotkey.replace("play the music of", "")
                    print(music +"\n")
                    bot3_4 = Music()
                    bot3_4.play(music)

            if "video" in jarvis_hotkey:
                video = jarvis_hotkey.replace("play the video of", "")
                print(video +"\n")
                bot4 = Music()
                bot4.play(video)

            if "meaning" in jarvis_hotkey:
                meaning = jarvis_hotkey.replace("what is the meaning of", "")
                print(meaning + "\n")
                bot5 = Meaning()
                bot5.word_meaning(meaning)

            if "google" in jarvis_hotkey:
                google = jarvis_hotkey.replace("google search on", "")
                print(google + "\n")
                bot6 = Google()
                bot6.google_search(google)

            if "translate" in jarvis_hotkey:
                translate = jarvis_hotkey.replace("translate the word", "")
                print(translate + "\n")
                bot7 = Translation()
                bot7.translate_word(translate)

            if "internet speed" in jarvis_hotkey:
                print("checking internet speed... \n")
                bot8 = internet()
                bot8.speed("speed")

            if "whatsapp" in jarvis_hotkey:
                print("Setting up Whatsapp \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Setting up WhatsApp")
                engine.runAndWait()
                whatsapp_chat()

            if "introduce" in jarvis_hotkey:
                print("\n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Hello, I am your personal AI assistant JARVIS. I am a famous character in marvel studios 'Iron Man' movies where i am a assistant for tony stark.")
                print("Hello, I am your personal AI assistant JARVIS. I am a famous character in marvel studios 'Iron Man' movies where i am a assistant for tony stark.")
                engine.say("I can take your commands and do whatever you want.")
                print("I can take your commands and do whatever you want.")
                engine.say("For example, I can search content in wikipedia and in  google, I can send whatsapp messages, translate words, search meanings of words, play music on youtube, read news for you, check the internet speed and search for movie reviews.")
                print("""For example, I can search content in wikipedia and in  google, I can send whatsapp messages, translate words,
                        read news for you, search meanings of words, play music on youtube, check the internet speed and search for movie reviews.""")
                engine.runAndWait()
                time.sleep(3)
                first()

            if "photo" in jarvis_hotkey:
                print("Setting up Camera \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Setting up Camera")
                engine.runAndWait()
                def ca():
                    camera()
                z = threading.Thread(target=ca)
                z.start()

            if "weather" in jarvis_hotkey:
                print("Setting up Weather App \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Setting up Weather App")
                engine.runAndWait()
                def wea():
                    os.system("Weather_App_V2.exe")
                x=threading.Thread(target=wea)
                x.start()

            if "what is the time" in jarvis_hotkey:
                print("Setting up Clock \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Setting up Clock")
                engine.runAndWait()
                def cl():
                    clock()
                y = threading.Thread(target=cl)
                y.start()

            if "news" in jarvis_hotkey:
                print("Loading TIMES OF INDIA \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Loading TIMES OF INDIA")
                engine.runAndWait()
                bot0 = News()
                bot0.headlines("check")

            if "open" in jarvis_hotkey:
                open_data  = jarvis_hotkey.replace("open", "")
                if "app" in open_data:
                    app_data = open_data.replace("app", "")
                    o(app_data, match_closest=True, output=True)
                    first()
                if "website" in open_data:
                    website_data = open_data.replace("website", "")
                    print(website_data + "\n")
                    website_data = website_data.upper()
                    print(website_data)
                    website_opener.website(name=website_data)


            if "set a timer" in jarvis_hotkey:
                print("How many minutes would you like to set the Timer sir? \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("How many minutes would you like to set the Timer sir?")
                engine.runAndWait()
                timer_loader()

            if "stop the timer" in jarvis_hotkey:
                print("Stopping the Timer \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Ok sir, stopping the Timer")
                engine.runAndWait()
                timer_stopper()

            if "activate bluetooth controller" in jarvis_hotkey:
                print("Activating Controller \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Ok sir, Activating Controller")
                engine.runAndWait()
                controller()
            
            if "wait for me" in jarvis_hotkey:
                print("Activating System Security \n")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("Ok sir, turning on security mode in")
                engine.say("5")
                time.sleep(1)
                engine.say("4")
                time.sleep(1)
                engine.say("3")
                time.sleep(1)
                engine.say("2")
                time.sleep(1)
                engine.say("1")
                time.sleep(1)
                engine.runAndWait()
                security()

            if "shutdown" in jarvis_hotkey:
                print("Shutting Down....")
                engine = p.init()
                engine.setProperty("rate", 140)
                engine.say("shutting down")
                engine.runAndWait()
                time_yo_data = time.strftime("%I:%M:%S %p")
                time_yo_date = time.strftime("%d-%m-%Y")
                file1 = open("Text_Files/caching_data.txt", "a")
                file1.write("Program ended at " +  time_yo_data + " | " + time_yo_date + "\n")
                print("Closing Program")
                file1.close()
                sys.exit()

        else:
            print(":/ \n")
