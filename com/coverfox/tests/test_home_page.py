import pytest
from com.coverfox.pages.home_page import HomePage
from com.coverfox.utilities.common_ops import load_test_data

count = 0


@pytest.mark.usefixtures('browser')
class HomePageTests:

    @pytest.fixture(scope="function")
    def page_object(self, browser):
        home_page = HomePage(browser)
        yield home_page
        home_page.ui.driver.quit()

    @pytest.fixture(scope="function")
    def load_home_page(self, page_object):
        page_object.load()
        global count
        count = count + 1
        print('page loaded {} times till now'.format(count))

    def test_home_page_url_loads_successfully(self, page_object):
        assert page_object.load()

    # approach 1 to make data driven test cases
    @pytest.mark.skip(reason='need to demo the one without parameterize')
    @pytest.mark.parametrize('data', load_test_data('insurance_categories'))
    def test_insurance_pages_open_successfully_using_parameterize(self, page_object, data):
        page_object.open_insurance(data)
        assert page_object.ui.contains_text('Buying two-wheeler insurance from Coverfox is simple')

    # approach 2 to make data driven test cases
    @pytest.mark.insurance_links
    def test_insurance_pages_open_successfully_using_fixtures(self, page_object, load_home_page, insurance_data):
        page_object.open_insurance(insurance_data)
        assert page_object.ui.page_contains_text('Buying two-wheeler insurance from Coverfox is simple')


