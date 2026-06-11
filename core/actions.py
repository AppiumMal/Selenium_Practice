from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from core.wait_helpers import WaitHelpers


class Actions:
    def __init__(self, driver: WebDriver, wait_helpers: WaitHelpers) -> None: #dependency injection of driver and wait_helpers
        self.driver: WebDriver = driver
        self.wait: WaitHelpers = wait_helpers

    def click(self, locator) -> WebElement:  #click on an element located by the given locator
        element = self.wait.wait_for_clickable(locator)
        element.click()
        return element

    def type(self, locator, text) -> WebElement: #type text into an element located by the given locator
        element = self.wait.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator) -> str: #get the text of an element located by the given locator
        element = self.wait.wait_for_visible(locator)
        return element.text