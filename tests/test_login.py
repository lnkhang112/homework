from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(5)
    username = driver.find_element(By.XPATH,"//input[@name='username']")
    password = driver.find_element(By.XPATH,"//input[@name='password']")
    sleep(5)
    username.send_keys("Admin")
    password.send_keys("admin123")
    driver.quit()
        