import pytest
from com.coverfox.utilities.common_ops import load_test_data
from com.coverfox.config import Config


@pytest.fixture(params=load_test_data("insurance_categories"))
def insurance_data(request):
    data = request.param
    return data


@pytest.fixture(params=Config.run_on_browsers, scope="function")
def browser(request):
    data = request.param
    if data.lower() not in list(map(str.lower, Config.supported_browsers)):
        raise ValueError('Browser not supported', data)
    return data


