from selenium import webdriver

import speech_recognition as sr

import pyttsx3 as p

import time

class News():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'selenium/chromedriver.exe')

    def headlines(self ,query):
        self.headlines = query
        self.driver.get(url="https://timesofindia.indiatimes.com/briefs")
        try:
            headline_1 = self.driver.find_element("xpath", '//*[@id="content"]/div/div/div[1]/h2/a')
            headline_2 = self.driver.find_element("xpath", '//*[@id="content"]/div/div/div[2]/h2/a')
            headline_3 = self.driver.find_element("xpath", '//*[@id="content"]/div/div/div[3]/h2/a')
            headline_4 = self.driver.find_element("xpath", '//*[@id="content"]/div/div/div[4]/h2/a')
            #headline_5 = self.driver.find_element_by_xpath('//*[@id="adsdivLyr"]/div/a/h3')
            headline_6 = self.driver.find_element("xpath", '//*[@id="content"]/div/div/div[6]/h2/a')
        except:
            pass

        readable_text1 = headline_1.text
        readable_text2 = headline_2.text
        readable_text3 = headline_3.text
        readable_text4 = headline_4.text
        #readable_text5 = headline_5.text
        readable_text6 = headline_6.text
        engine = p.init()
        engine.setProperty("rate", 140)
        engine.say("top 5 headlines in TIMES OF INDIA are " + readable_text1)
        time.sleep(2)
        engine.say(readable_text2)
        time.sleep(2)
        engine.say(readable_text3)
        time.sleep(2)
        engine.say(readable_text4)
        time.sleep(2)
        engine.say(readable_text6)
        time.sleep(2)
        engine.runAndWait()
        time.sleep(10)
        from repetition import first
        first()

# bot = News()
# bot.headlines()