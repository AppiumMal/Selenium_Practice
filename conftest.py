
import pytest
from utils.webdriver_singleton import WebDriverSingleton
from utils.config import Config

@pytest.fixture(scope="session")
def driver():
    driver = WebDriverSingleton.get_driver()
    driver.get(Config.BASE_URL)
    yield driver
    WebDriverSingleton.quit_driver()

    