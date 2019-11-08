import pytest
from com.coverfox.pages.home_page import HomePage
from com.coverfox.utilities.common_ops import load_test_data
from pytest import mark
import com.coverfox.resources.test_data


@pytest.fixture(scope="session")
def page_object():
    home_page = HomePage()
    yield home_page
    home_page.ui.driver.quit()


@pytest.fixture(scope="function")
def load_home_page(page_object):
    page_object.load()


@pytest.mark.skip
def test_home_page_url_loads_successfully_using_params(page_object):
    assert page_object.load()


@pytest.mark.skip(reason='need to demo the one without parameterize')
@pytest.mark.parametrize('data', load_test_data('insurance_categories'))
def test_insurance_pages_open_successfully_using_fixtures(page_object, data):
    page_object.open_insurance(data)
    assert page_object.ui.contains_text('Buying two-wheeler insurance from Coverfox is simple')


def test_insurance_pages_open_successfully(page_object, load_home_page, insurance_data):
    page_object.open_insurance(insurance_data)
    assert page_object.ui.contains_text('Buying two-wheeler insurance from Coverfox is simple')
