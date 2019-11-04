import pytest
from com.coverfox.pages.home_page import HomePage

# create an instance of home page
home_page = HomePage()


@pytest.mark.order1
def test_home_page_url_loads_successfully():
    assert home_page.load()


@pytest.mark.order2
def test_two_wheelers_insurance_opens_successfully():
    home_page.open_two_wheelers_insurance()
    assert home_page.ui.contains_text('Buying two-wheeler insurance from Coverfox is simple')
