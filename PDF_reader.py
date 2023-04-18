# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
import os
# import filedialog module
from tkinter import filedialog
import pyttsx3
from PyPDF2 import PdfReader
import threading
import sys
filename = ''
from pynput import keyboard
import keyboard as key
import threading
# Function for opening the
# file explorer window

def browseFiles():
    #global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File", filetypes = (("Text files", "*.pdf*"), ("all files", "*.*")))
    file_loc = os.path.basename(filename)
    label_file_explorer.configure(text="File Opened: "+ file_loc)
    print(file_loc + " is going to be read now!")	
    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)
    print("Number of pages: ", number_of_pages)
    print("\n1. Press 'START' to start reading\n2. Press 'CUSTOM' to choose a specific page\n3. Press 'EXIT' to exit\n")
    user_prefer = input("Preference: ")
    user_prefer = user_prefer.upper()
    if user_prefer == "START":
        #for i in range(number_of_pages):
        def start():
            i = 0
            while True:
                page = reader.pages[i]
                i = i + 1
                speaker = pyttsx3.init()
            # page = pdfReader.getPage(num)
                speaker.setProperty("rate", 200)
                text = page.extract_text()
                speaker.say(text)
                speaker.runAndWait()
                if i >= number_of_pages:
                    print("END OF PDF")
                    sys.exit()
        x = threading.Thread(target=start)
        print("Thread started")
        x.start()
    if user_prefer == "CUSTOM":
        print("type natural numbers!")
        numberof = int(input("pageno: "))
        numberof = numberof - 1 
        page = reader.pages[numberof]
        i = numberof
        while True:
                    page = reader.pages[i]
                    i = i + 1
                    speaker = pyttsx3.init()
                # page = pdfReader.getPage(num)
                    speaker.setProperty("rate", 200)
                    text = page.extract_text()
                    speaker.say(text)
                    speaker.runAndWait()
                    if i >= number_of_pages:
                        print("END OF PDF")
                        sys.exit()
                    

        # speaker = pyttsx3.init()
        # # page = pdfReader.getPage(num)
        # speaker.setProperty("rate", 160)
        # text = page.extract_text()
        # speaker.say(text)
        # speaker.runAndWait()
    if user_prefer == "EXIT":
        sys.exit()
    # Change label contents
    

                
    #	return filename

#file_name = input("enter file name/ name of pdf: ")

def Exit():
    sys.exit()																								
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("365x200")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 30, height = 4, 
                            fg = "blue", justify="center", font=("Helvetica", "14","bold"))

    
button_explore = Button(window,
                        text = "Browse and select file to read",
                        command = browseFiles, justify="center", borderwidth=0, background="aqua", font=("Helvetica", "12", "bold"))



button_exit = Button(window,
                    text = "Exit",
                    command = Exit, borderwidth="0", background="red", fg="black", font=("Helvetica", "12", "bold"))


# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)



# Let the window wait for any events
window.mainloop()
