from selenium import webdriver
import time

class internet():
     def __init__(self):
          self.driver = webdriver.Chrome(executable_path=r'selenium/chromedriver.exe')

     def speed(self, word):
          self.speed = word
          self.driver.get(url="https://fast.com/")
          #result = int(self.driver.find_element_by_xpath('//*[@id="speed-value"]'))
          #result.send_keys(word)
          time.sleep(15)
          
          from repetition import first
          first()


#bot = internet()
#bot.internet_speed("speed")
