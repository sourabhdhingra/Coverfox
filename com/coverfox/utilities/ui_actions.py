from com.coverfox.utilities.ui_driver import UIDriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from com.coverfox.utilities.common_ops import get_locator_strategy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as expect


class UIActions(UIDriver):
    """
    A wrapper over the UIDriver class providing the common page interactions such as select element from dropdown etc
    """
    def __init__(self, browser='chrome', timeout=10, wait=10):
        super().__init__(browser, timeout, wait)
        self.action = ActionChains(self.driver)

    def find_element(self, locator):
        # try:
        #     pass
        # except Exception:
        #     traceback.print_exception()
        strategy, locator = get_locator_strategy(locator)
        element = self.driver.find_element(strategy, locator)
        return element

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
        self.action.move_to_element(to_element).perform()

    def contains_text(self, text):
        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'{}')]".format(text))
        return True if elements else False



