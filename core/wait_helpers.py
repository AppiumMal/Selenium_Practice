from typing import Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from utils.config import Config
from selenium.common.exceptions import TimeoutException
from core.exceptions import ElementNotFoundException


Locator = Tuple[str, str]


class WaitHelpers:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def wait_for_presence(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator: Locator,error_message=None) -> WebElement:
          try:
            return self.wait.until(EC.visibility_of_element_located(locator))
          except TimeoutException as e:                                 # e is used for original seleniu stack trace
              message = error_message or f"{locator} not visible after {Config.TIMEOUT}s | Locator: {locator}" # logging message customisation with timeout displayed along with the locator name
              raise ElementNotFoundException(message) from e    

    def wait_for_clickable(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_invisible(self, locator: Locator) -> bool:
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    from selenium.webdriver.support.ui import WebDriverWait

    def wait_for_condition(self, condition, timeout=None):
       
          if timeout:
               return WebDriverWait(self.driver, timeout).until(condition)
          return self.wait.until(condition)

