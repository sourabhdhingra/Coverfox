from com.coverfox.utilities.ui_driver import UIDriver
from com.coverfox.utilities.common_ops import get_locator_strategy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as expect
from selenium.common.exceptions import StaleElementReferenceException
from com.coverfox.config import Config


class UIActions(UIDriver):
    """
    A wrapper over the UIDriver class providing the common page interactions such as select element from dropdown etc
    """
    def __init__(self, browser=Config.default_browser, timeout=10, wait=10):
        super().__init__(browser, timeout, wait)
        self.action = ActionChains(self.driver)

    def find_element(self, locator):
        element = None
        while True:
            try:
                strategy, locator = get_locator_strategy(locator)
                element = self.driver.find_element(strategy, locator)
                break
            except StaleElementReferenceException:
                print('StaleElementReferenceException')
                continue
            finally:
                return element

    def find_elements(self, locator):
        elements = None
        while True:
            try:
                strategy, locator = get_locator_strategy(locator)
                elements = self.driver.find_elements(strategy, locator)
                break
            except StaleElementReferenceException:
                print('StaleElementReferenceException')
                continue
            finally:
                return elements

    def click(self, locator):
        try:
            element = self.wait.until(expect.element_to_be_clickable(get_locator_strategy(locator)))
            element.click()
        finally:
            pass

    def open_url(self, url):
        self.driver.get(url)

    def move_to(self, locator):
        to_element = self.find_element(locator)
        print("element value", to_element)
        self.action.move_to_element(to_element).perform()

    def page_contains_text(self, text):
        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'{}')]".format(text))
        return True if elements else False



