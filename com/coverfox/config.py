import os
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium import webdriver

'''
    config variables - variables to configure the framework
'''


class Config:
    # config variables - variables to configure the framework
    home_url = "https://www.coverfox.com/"
    run_on_browsers = ['chrome', 'firefox']
    default_browser = 'chrome'
    supported_browsers = ['chrome', 'firefox']  # for Edge the latest release for OS 10 is not available OS Build Issue
    implicit_timeout = 10
    explicit_timeout = 10
    abs_path = os.path.abspath(path=os.curdir)
    chrome_driver_path = (abs_path + "\\coverfox\\bin\chromedriver.exe")
    firefox_driver_path = (abs_path + "\\coverfox\\bin\geckodriver.exe")
    edge_driver_path = (abs_path + "\\coverfox\\bin\MicrosoftWebDriver.exe")

    '''
    config methods - methods to get the desired config
    '''
    @classmethod
    def get_browser(cls, browser):
        options = None
        if browser.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            return webdriver.Chrome(executable_path=Config.chrome_driver_path, chrome_options=options)
        elif browser.lower() == 'firefox':
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            return webdriver.Firefox(executable_path=Config.firefox_driver_path, firefox_options=options)
        elif browser.lower() == 'edge':
            options = webdriver.DesiredCapabilities.EDGE.copy()
            options['os'] = "Windows"
            options['acceptSslCerts'] = True
            return webdriver.Edge(executable_path=Config.edge_driver_path, capabilities=options)
        else:
            raise ValueError('Unsupported Browser or Browser not set', browser)

