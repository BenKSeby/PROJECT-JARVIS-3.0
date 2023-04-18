import speech_recognition as sr
import pyttsx3 as p
import sys
import time
from web_auto import *
from web_auto1 import *
from web_automation import *
from word import *
from google_search import *
from translation import *
from internet_speed_test import *
from whatsapp import *
from camera import camera
import os
from digital_clock import *
#from repeat import first1
from news import *
#from app_loader import *
from timerloader import timer_loader
from timerstopper import timer_stopper
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUI3 import Ui_MainWindow
from arduino_car_control import controller
import webbrowser
import keyboard as key
from winotify import Notification,audio
from pynput import keyboard
from AppOpener import open as o
import website_opener
from security_camera import security
import threading
#import weather_app_v2

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.bootup()
    
    def bootup(self):
        engine = p.init()
        engine.setProperty("rate", 140)
        engine.say("Welcome back sir !")
        print("Welcome Back Sir !")
        engine.say("How can I help you today ?")
        print("How can I help you today ?") 
        engine.runAndWait()
        self.initial_conversation()

    def initial_conversation(self):
        if __name__ == '__main__':
            time_data = time.strftime("%I:%M:%S %p")
            print(time_data)
            time_date = time.strftime("%d-%m-%Y")
            print(time_date)
            #return time_data and time_date
            #data()

            file1 = open("Text_Files/caching_data.txt", "a")
            print("Program started at " + time_data + " | " + time_date)
            file1.write("Program started at " + time_data + " | " + time_date + "\n")
            file1.close()
            while True:
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
                        self.initial_conversation()
                    except sr.RequestError as e:
                        print("err2")
                        self.initial_conversation()
                    except Exception as e:
                        print("err3")
                        self.initial_conversation()
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
                        bot2 = Movie()
                        bot2.movie_review(review)

                    if "music" or "song" in jarvis_hotkey:
                        #music = jarvis_hotkey.replace("play the music of" or "play the song", "" ) #or jarvis_hotkey.replace("play music", "") or jarvis_hotkey.replace("play the song", "") or jarvis_hotkey.replace("play the song of", "")
                        if "play the music of" in jarvis_hotkey:
                            music = jarvis_hotkey.replace("play the music of ", "")
                            print(music + "\n")
                            bot3 = Music()
                            bot3.play(music)
                        if "play the music" in jarvis_hotkey:
                            music = jarvis_hotkey.replace("play the music", "")
                            print(music +"\n")
                            bot3 = Music()
                            bot3.play(music)
                        if "play the song" in jarvis_hotkey:
                            music = jarvis_hotkey.replace("play the song", "")
                            print(music + "\n")
                            bot3 = Music()
                            bot3.play(music)
                        if "play the song of" in jarvis_hotkey:
                            music = jarvis_hotkey.replace("play the music of", "")
                            print(music +"\n")
                            bot3 = Music()
                            bot3.play(music)

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
                        self.initial_conversation()

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
                            app_data = app_data.upper()
                            #print("Opening" + app_data + "\n")
                            o(app_data, match_closest=True, output=True)
                            self.initial_conversation()
                        if "website" in open_data:
                            website_data = open_data.replace("website", "")
                            print(website_data)
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

startExecution = MainThread()

class Main1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.connect(self.startTask)
        self.ui.exit_button.clicked.connect(self.end)
        self.ui.home_button.clicked.connect(self.home_page)
        self.ui.more_button.clicked.connect(self.more_page)
        self.ui.about_button.clicked.connect(self.about_page)
        self.ui.github.clicked.connect(self.open1)

        self.ui.pdf_button.clicked.connect(self.pdfopen2)
        self.ui.website_index_button.clicked.connect(self.web_ind)
        self.ui.weather_button.clicked.connect(self.weather_func)
        self.ui.selenium_button.clicked.connect(self.selenium_func)
        #self.ui.menu_button.clicked.connect(self.menu_page)
        

    #     #############################
    #     self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #     #############################
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    #     ############################
    #     self.setWindowIcon(QtGui.QIcon("github.png"))
    #     self.setWindowTitle("MODERN UI")
    #     #############################
    #     self.ui.minimize.clicked.connect(lambda: self.showMinimized())
    #     self.ui.close.clicked.connect(lambda: self.close())
    #     self.ui.restore_and_maximize.setIcon(QtGui.QIcon("maximize.jpg"))
    #     self.ui.restore_and_maximize.clicked.connect(lambda: self.restore_or_maximize_window())
    #     self.ui.controlpanel.mouseMoveEvent = self.moveWindow

    # def restore_or_maximize_window(self):
    #     if self.isMaximized():
    #         self.showNormal()
    #         self.ui.restore_and_maximize.setIcon(QtGui.QIcon("maximize.jpg"))

    #     else:
    #         self.showMaximized()
    #         self.ui.restore_and_maximize.setIcon(QtGui.QIcon("restore.png"))

    # def moveWindow(self, e):
    #     if self.isMaximized() == False:
    #         if e.buttons() == Qt.LeftButton:
    #             self.move(self.pos() + e.globalPos() - self.clickPosition)
    #             self.clickposition = e.globalPos()
    #             e.accept()

    # def mousePressEvent(self, event):
    #     self.clickPosition = event.globalPos()
    # def menu_page(self):
    #     width = self.ui.leftside.width()
    #     if width == 221:
    #         newWidth = 60
    #     else: 
    #         newWidth = 221

    #     self.animation = QPropertyAnimation(self.ui.leftside, b"maximumWidth")
    #     self.animation.setDuration(250)
    #     self.animation.setStartValue(width)
    #     self.animation.setEndValue(newWidth)
    #     self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    #     self.animation.start()

    def home_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
    def more_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.more)
    def about_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.about)

    def open1(self):
        webbrowser.open("https://www.github.com/BenKSeby")


    def pdfopen2(self):
        def B1():
            os.system("PDF_Reader.exe")
        a = threading.Thread(target=B1)
        a.start()
    def web_ind(self):
        def B2():
            os.system("Website_Indexer.exe")
        a = threading.Thread(target=B2)
        a.start()
    def weather_func(self):
        def B3():
            os.system("Weather_App_V2.exe")
        a = threading.Thread(target=B3)
        a.start()
    def selenium_func(self):
        def B4():
            os.system("Selenium_Driver_Updater.exe")
        a = threading.Thread(target=B4)
        a.start()


    def end(self):
        self.close()
        sys.exit()
            
    def startTask(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.movie1 = QtGui.QMovie("Icons/original.gif")
        self.ui.movie2 = QtGui.QMovie("Icons/initialize.gif")
        self.ui.movie3 = QtGui.QMovie("Icons/jarvis1.gif")

        self.ui.jarvis.setMovie(self.ui.movie1)
        self.ui.initialize.setMovie(self.ui.movie2)
        self.ui.ironman.setMovie(self.ui.movie3)

        self.ui.movie1.start()
        self.ui.movie2.start()
        self.ui.movie3.start()

        timer= QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()


    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('h:mm:ss AP')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main1()
jarvis.show()
sys.exit(app.exec_())
