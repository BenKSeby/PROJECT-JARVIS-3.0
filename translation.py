from selenium import webdriver

import speech_recognition as sr

import pyttsx3 as p

import time

class Translation():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'selenium/chromedriver.exe')

    def translate_word(self, word):
        global language
        self.driver.get(url="https://translate.google.co.in/")
        search1 = self.driver.find_element("xpath", '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
        search1.click()
        search1.send_keys(word)

        language_option = self.driver.find_element("xpath", '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]')
        language_option.click()

        r = sr.Recognizer()
        engine = p.init()
        engine.say("which language would you like it to be translated?")
        engine.runAndWait()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Which language?")
            audio = r.listen(source)
        try:
            language = r.recognize_google(audio)
            print(language)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")
        try:
            if "Hindi" in language:
                language1 = self.driver.find_element("xpath", '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[47]/div[2]')
                language1.click()

            if "Malayalam" in language:
                language2 = self.driver.find_element("xpath", '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[79]/div[2]')
                language2.click()

            if "English" in language:
                language3 = self.driver.find_element("xpath", '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[29]/div[2]')
                language3.click()

            time.sleep(3)
            translated = self.driver.find_element("xpath", '//*[@id="ow416"]/div[1]/span[1]/span/span')
            readable_text = translated.text
            engine = p.init()
            engine.setProperty("rate", 140)
            engine.say("the translation of" + word + "in" + language + "is that" + readable_text)
            engine.runAndWait()
        except Exception as e:
            print("err -- wasn't able to read the data")
        from repetition import first
        first()

# bot = Translation()
# bot.translate_word("encyclopedia")
