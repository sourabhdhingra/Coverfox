import pytest
from com.coverfox.pages.home_page import HomePage

# create an instance of home page


@pytest.fixture(scope="module")
def page_object():
    return HomePage()


@pytest.mark.order1
def test_home_page_url_loads_successfully(page_object):
    assert page_object.load()


@pytest.mark.order2
def test_two_wheelers_insurance_opens_successfully(page_object):
    page_object.open_two_wheelers_insurance()
    assert page_object.ui.contains_text('Buying two-wheeler insurance from Coverfox is simple')
