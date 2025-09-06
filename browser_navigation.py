import pytest
from selenium import webdriver
from time import sleep
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self,request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        request.cls.driver = self.driver
        yield
        self.driver.quit()