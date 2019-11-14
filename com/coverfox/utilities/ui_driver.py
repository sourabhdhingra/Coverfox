from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxProfile
from com.coverfox.config import Config


class UIDriver:
    """
    A wrapper for driver class
        - return instances based on the parameter browser
        - sets implicit timeout values
        - wrapper functions for element interactions
    """
    def __init__(self, browser=Config.default_browser, timeout=10, wait=10):
        self.__driver = Config.get_browser(browser)
        self._timeout = timeout
        self._wait = WebDriverWait(self.__driver, wait)
        self.__driver.implicitly_wait(self._timeout)

    @property
    def driver(self):
        return self.__driver

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout
        self.__driver.implicitly_wait(self._timeout)

    @property
    def wait(self):
        return self._wait

    @wait.setter
    def wait(self, wait):
        self._wait = wait
        self._wait = WebDriverWait(self.__driver, wait)

