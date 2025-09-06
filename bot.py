from selenium import webdriver
from time import sleep

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')
        sleep(3)
        self.driver.quit()