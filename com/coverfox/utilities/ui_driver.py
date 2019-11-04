from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions
from com.coverfox.config import *


class UIDriver:
    """
    A wrapper for driver class
        - return instances based on the parameter browser
        - sets implicit timeout values
        - wrapper functions for element interactions
    """
    def __init__(self, browser='chrome', timeout=10, wait=10):
        self.__driver = None
        if browser.lower() == 'chrome':
            print(chrome_driver_path)
            # temporary setting
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # ---------------------
            self.__driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
        elif browser.lower() == 'firefox':
            self.__driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            self.__driver = webdriver.Edge()
        else:
            raise ValueError('Unsupported Browser or Browser not set', browser)
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

