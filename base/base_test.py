from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(5)
        request.cls.driver = self.driver
        
        yield
        driver.quit()