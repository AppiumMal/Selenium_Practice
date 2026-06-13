
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from core.wait_helpers import WaitHelpers
from core.exceptions import TextNotFoundException
from core.assertions import Assertions


class Actions:
    def __init__(self, driver: WebDriver, wait_helpers: WaitHelpers) -> None: #dependency injection of driver and wait_helpers
        self.driver: WebDriver = driver
        self.wait: WaitHelpers = wait_helpers
        self.assertions = Assertions()


    #Validate if element visible on the screen       
    def validate_visible(self, locator) -> None:
       
       element = self.wait.wait_for_visible(locator)

       self.assertions.assert_element_visible(element)   # ✅ assertion here


        #Click on element

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
    
    #find elements
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    #get visible texts
    def get_visible_texts(self, locator):
        elements = self.driver.find_elements(*locator)
        return self.wait.wait_for_visible(lambda d: [el for el in d.find_elements(*locator) if el.is_displayed()])
    
    
def assert_text(self, locator, expected_text):
    actual = self.get_text(locator)
    if actual != expected_text:
        raise TextNotFoundException(
            f"Expected '{expected_text}', but got '{actual}'"
        )
