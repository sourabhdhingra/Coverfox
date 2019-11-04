from selenium.webdriver.common.by import By


def get_locator_strategy(locator):
    """

    :param locator: locator (key, value) pair for finding the element e.g id=john123
    :return: a tuple (strategy, locator) e.g strategy=xpath and locator=//div[@class='purchase']/li[0]
    """
    if len(locator) == 1:
        strategy = list(locator.keys()).pop()
        locator = list(locator.values()).pop()
        return get_by_strategy(strategy), locator


def get_by_strategy(strategy):
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