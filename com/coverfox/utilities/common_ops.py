from selenium.webdriver.common.by import By
import csv
# from pathlib import Path
# import os


def get_locator_strategy(locator):
    """

    :param locator: locator (key, value) pair for finding the element e.g id=john123
    :return: a tuple (strategy, locator) e.g strategy=xpath and locator=//div[@class='purchase']/li[0]
    """
    if len(locator) == 1:
        strategy = list(locator.keys()).pop()
        locator = list(locator.values()).pop()
        return get_by_strategy(strategy), locator


def format_locator(locator, *args):
    """

    :param locator: locator (key, value) pair for finding the element e.g id=john123
    :param args: list of values to replaced in locator e.g xpath=//div[@id='{}']/li[text()='{}'], values will replace
    the respective blocks
    :return: a dict with strategy as key, and locator as its value
    """
    if len(locator) == 1:
        strategy = list(locator.keys()).pop()
        locator = list(locator.values()).pop()
        locator = locator.format(*args)
        locator = {strategy: locator}
        return locator


def get_by_strategy(strategy):
    """

    :param strategy: one of the element locator strategy such as xpath, link text , id etc..
    :return: corresponding By element strategy
    """
    if strategy.upper() == 'ID':
        return By.ID
    elif strategy.upper() == 'XPATH':
        return By.XPATH
    elif strategy.upper() == 'LINK_TEXT':
        return By.LINK_TEXT
    elif strategy.upper() == 'PARTIAL_LINK_TEXT':
        return By.PARTIAL_LINK_TEXT
    elif strategy.upper() == 'NAME':
        return By.PARTIAL_LINK_TEXT
    elif strategy.upper() == 'TAG_NAME':
        return By.TAG_NAME
    elif strategy.upper() == 'CLASS_NAME':
        return By.CLASS_NAME
    elif strategy.upper() == 'CSS_SELECTOR':
        return By.CSS_SELECTOR
    else:
        raise ValueError('Invalid strategy/Strategy not found.', strategy)


def load_test_data(data_id):
    # file_path = os.path.abspath(path=os.curdir) + str(Path("/resources/test_data/test_data.csv"))
    # file_path = Path('\\resources\\test_data\\test_data.csv')
    file_path = r"C:\Users\sourabh.dhingra\PycharmProjects\Coverfox\com\coverfox\\resources\\test_data\\test_data.csv"
    with open(file_path) as file:
        data = list(csv.reader(file))
        for row in data:
            if row[0].lower() == data_id:
                return row[1::]
