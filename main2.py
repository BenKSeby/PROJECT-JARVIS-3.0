
import time
import getpass
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from loginUI import Ui_LOGIN
import sys
import os
import pickle
#USER = input("Please type your username: ")
#USER.lower
#password = input("please type in your passwod: ")
#password = getpass.getpass(prompt="please type in your password: ")


# if USER == "ben" or "shaun" or "aaron" or "steve" or "jesus":
#     password
# else:
#     print("wrong username")
#     exit()
    
# if password == "jarvis":
#     time.sleep(3)
#     print("hello " + USER + ",welcome to jarvis your personal AI assistant")
#     time.sleep(5)
#     print("Intializing JARVIS....")
#     time.sleep(7)
#     from jarvis import initial_conversation
#     initial_conversation()
# else:
#     print("wrong password")
#     exit() 

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
                    os.system('python jarvis.py')
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
sys.exit(login.exec_())
            
