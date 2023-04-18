import serial
import speech_recognition as sr
import pyttsx3 as p
import sys
import time


# def retriveData():
#     ser.write(b'1')
#     data = ser.readline().decode('ascii')
#     return data

# def initial_conversation(self):
#         rl = sr.Recognizer()
#         engine = p.init()
#         engine.setProperty("rate", 140)
#         engine.say("Welcome back sir")
#         engine.say("how are you today?")
#         engine.runAndWait()
#         with sr.Microphone() as source:
#                     rl.adjust_for_ambient_noise(source)
#                     print("how are you today?")
#                     audio = rl.listen(source)
#                     try:
#                         self.text = rl.recognize_google(audio)
#                         print(self.text)
#                     except sr.UnknownValueError:
#                         print("err1 -- please say it again")
#                         self.initial_conversation()
#                     except sr.RequestError as e:
#                         print("err2")
#                         self.initial_conversation()
#                     except Exception as e:
#                         print("err3 -- please say it again")
#      
#                    self.initial_conversation()
    
def controller():
    try:
        time.sleep(2)
        ser = serial.Serial("COM5", 9600, timeout = 0)
        pass
    except Exception as e:
        engine = p.init()
        engine.setProperty("rate", 140)
        #engine.say("Welcome back sir")
        engine.say("connection unsuccessful")
        engine.say("falling back")
        engine.runAndWait()
        from repetition import first
        first()
    engine = p.init()
    engine.setProperty("rate", 140)
    #engine.say("Welcome back sir")
    engine.say("controller ready sir")
    engine.runAndWait()
    while (True):
        time.sleep(1)
        rl = sr.Recognizer()
        engine = p.init()
        engine.setProperty("rate", 140)
        #engine.say("Welcome back sir")
        engine.say("please say the command")
        engine.runAndWait()
        with sr.Microphone() as source:
            rl.adjust_for_ambient_noise(source)
            print("please say the command")
            audio = rl.listen(source)
            try:
                uInput = rl.recognize_google(audio, language='en-in')
                print(uInput)
            except sr.UnknownValueError:
                print("err1 -- please say it again")
            except sr.RequestError as e:
                print("err2")
            except Exception as e:
                print("err3 -- please say it again")
        #uInput  = input("reteive data?: ")
        if 'left' in uInput:
            ser.write(b'L')
        elif 'right' in uInput:
            ser.write(b'R')
        elif 'backward' in uInput:
            ser.write(b'B')
        elif 'forward' in uInput:
            ser.write(b'F')
        elif 'stop' in uInput:
            ser.write(b'T')
        elif 'fog light on' in uInput:
            ser.write(b'J')
        elif 'fog light off' in uInput:
            ser.write(b'I')
        elif 'headlight on' in uInput:
            ser.write(b'K')
        elif 'headlight off' in uInput:
            ser.write(b'M')
        elif 'close the controller'in uInput:
            engine = p.init()
            engine.setProperty("rate", 140)
            engine.say("ok sir")
            engine.say("exiting controller")
            engine.runAndWait()
            ser.close()
            from repetition import first
            return first()

#controller()
