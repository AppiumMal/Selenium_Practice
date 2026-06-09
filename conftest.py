
import pytest
from utils.webdriver_singleton import WebDriverSingleton

@pytest.fixture(scope="session")
def driver():
    driver = WebDriverSingleton.get_driver()
    yield driver
    WebDriverSingleton.quit_driver()