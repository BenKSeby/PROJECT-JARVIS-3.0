import time
import pyautogui as py
import pyttsx3 as p

def timer_stopper():
    py.hotkey('winleft', 's')
    time.sleep(3)
    py.typewrite('alarm')
    py.press('right')
    py.press('enter')
    time.sleep(5)
    py.moveTo(363, 365)
    py.click()
    time.sleep(2)
    py.hotkey('altleft', 'tab')
    time.sleep(3)
    engine = p.init()
    engine.say("the timer has been stopped")
    engine.runAndWait()
    from repetition import first
    first() 