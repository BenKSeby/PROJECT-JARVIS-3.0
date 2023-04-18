from selenium import webdriver
import pyttsx3 as p
import time
import pyautogui as auto

class Meaning():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'selenium/chromedriver.exe')

    def word_meaning(self, word):
        self.word = word
        self.driver.get(url="https://www.google.com/search?q=define+" + word)
        #time.sleep(20)
        # search2 = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        # search2.click()
        # search2.send_keys("define " + word)
        # auto.press("enter")
        time.sleep(3)
        try: 
            result1 = self.driver.find_element("xpath", '/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/span/div/div/div[3]/div/div[2]/div/div/ol/li[1]/div/div/div[1]/div[2]/div/div')
            #result11 = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/ol/li/span[1]')
            #result12 = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/ol/li[1]/span[2]')
            # result2 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/ol/li[2]/span[2]')
            readable_text1 = result1.text
        

            result2 = self.driver.find_element("xpath", '/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/span/div/div/div[3]/div/div[2]/div/div/ol/li[2]/div/div/div[1]/div[2]/div/div')
            readable_text2 = result2.text
        
            # readable_text2 = result2.text
            engine = p.init()
            engine.setProperty("rate", 140)
            engine.say("the meaning of " + word + "is that" + readable_text1)
            engine.say("or " + readable_text2)
            engine.runAndWait()
            time.sleep(10)
        
            from repetition import first
            first()
        except:
            print("Unable to process the data to read...")
            from repetition import first
            first() 
#bot = Meaning()
#bot.word_meaning('intelligence')
