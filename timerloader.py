import pyautogui as py
import time
import speech_recognition as sr
# import pyttsx3 as p

def timer_loader():
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source)
        audio = r2.listen(source)
        try:
            instruction = r2.recognize_google(audio)
            print(instruction)
        except sr.UnknownValueError:
            print("err1 -- please say it again")
            timer_loader()
        except sr.RequestError as e:
            print("err2")
            timer_loader()
        except Exception as e:
            print("err3 -- please say it again")
            timer_loader()

    py.hotkey('winleft', 's')
    time.sleep(3)
    py.typewrite('alarm')
    py.press('right')
    py.press('enter')
    time.sleep(5)
    #py.press('tab')
    py.moveTo(380, 270)
    py.click()
    time.sleep(1)
    py.moveTo(690, 300)
    py.click()
    py.typewrite(instruction)
    time.sleep(2)
    py.moveTo(605, 490)
    py.click()
    time.sleep(1)
    py.moveTo(363, 365)
    py.click()
    time.sleep(2)
    py.hotkey('altleft', 'tab')
    time.sleep(3)
    from repetition import first
    first()
#time.sleep(1)
#py.press('enter')