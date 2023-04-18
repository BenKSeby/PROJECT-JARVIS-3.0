from multiprocessing.sharedctypes import Value
from selenium import webdriver
import time

# class to play a music video on youtube
class Music():
    def __init__(self):
        self.name = None
        self.driver = webdriver.Chrome(executable_path=r'selenium/chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

    def play(self, name):
        self.name = name
        self.driver.get(url="https://www.youtube.com/results?search_query=" + name)
        # video = self.driver.find_element_by_xpath('//*[@id="video-title"]')
        try:
            video = self.driver.find_element("xpath", '//*[@id="video-title"]')
            video.click()
            time.sleep(10)
        except:
            print("err -- wasn't able to load video")
        from repetition import first
        first()

# calling the music automation class
##    bot = Music()
##    bot.play("karikku")
