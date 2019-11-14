from com.coverfox.config import Config
import com.coverfox.resources.home_pg_locators as locators
from com.coverfox.utilities.ui_actions import UIActions
from com.coverfox.utilities.common_ops import format_locator


class HomePage:
    __home_url = Config.home_url
    _implicit_timeout = Config.implicit_timeout
    _explicit_timeout = Config.explicit_timeout

    def __init__(self, browser=Config.default_browser):
        self.__browser = browser
        self._ui = UIActions(self.__browser, self._implicit_timeout, self._explicit_timeout)

    @property
    def ui(self):
        return self._ui

    def load(self):
        self._ui.open_url(self.__home_url)
        element = self._ui.find_element(locators.btn_view_quotes)
        if element:
            return True
        else:
            return False

    def open_insurance(self, insurance):
        self._ui.move_to(locators.drp_dwn_insurance)
        self._ui.click(format_locator(locators.lnk_insurance, insurance))

