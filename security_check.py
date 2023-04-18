import sys
# import face_recognition as fr
import pickle
import cv2
import os
import pyttsx3 as p
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from loginUI import Ui_LOGIN
import time


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LOGIN()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.task)
        #from jarvis import Main1
        #self.dialog = Main1(self)

    def task(self):
        file = open("User_Data/user_credentials.dat", "rb")
        found = 0
        USERNAME = self.ui.USERNAME.text()
        USERNAME = USERNAME.upper()
        try:
            while True:
                rec = pickle.load(file)
                if(self.ui.USERID.text() == rec[0] and USERNAME == rec[1] and self.ui.PASSWORD.text() == rec[2]):
                    found = 1
                    time.sleep(1)
                    print("\nwelcome\n")
                    self.close()
                    from repetition import first
                    first()
                    
            #self.dialog.show()
        except:
            pass
        if(found == 0):
            time.sleep(1)
            print("\nWRONG DETAILS !!!\n")
            print("please re-enter the details\n")
        
login = QApplication(sys.argv)
start = Main()
start.show()
exit(login.exec_())
# def locked():
#     engine = p.init()
#     video_capture = cv2.VideoCapture(0)
#     face_is_match = False
#     face_encodings = []
#     known_face_encodings = pickle.load(open('encode.pickle','rb'))
        
#     while True:
#             ret, frame = video_capture.read()
#             face_locations = fr.face_locations(frame, model="hog")
#             face_encodings = fr.face_encodings(frame, face_locations)
        
#             face_names = []
#             name = "Unknown"
#             for face_encoding in face_encodings:
#                     matches = fr.compare_faces(known_face_encodings, face_encoding, 0.4)
                
#                     #find first match
#                     if True in matches:
#                         first_known_face = matches.index(True)
#                         face_is_match = True
#                         print("welcome back sir !")
#                         video_capture.release()
#                         engine.setProperty("rate", 140)
#                         engine.say("welcome back sir !")
#                         engine.runAndWait()
#                         from repetition import first
#                         return first()
#                         #os.system('python repetition.py')
#                         #sys.exit(0)
#                     else:
#                         print("Access Denied")
#                         quit()
