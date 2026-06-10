
from utils.webdriver_singleton import WebDriverSingleton 
from utils.config import Config 
from pages.login_page import LoginPage
from utils.logger import setup_logger
import pytest

logger = setup_logger() 

driver = WebDriverSingleton.get_driver()

class TestLoginPractice:
      
      def test_practice1(self,driver):
    
          WebDriverSingleton.get_driver()

          logger.info("Starting test_practice1")
          #open the webpage
          Config.BASE_URL
          logger.info(f"Opened webpage: {Config.BASE_URL }")

    
      @pytest.mark.parametrize("username, password", [("tester", "pytest"), ("admin","admin123"), ("guest","guest123")])
      def test_practice2(self, driver, username, password):
         logger.info("Starting login test_practice2")

         driver.get("file:///C:/Users/malathy.ranganathan/OneDrive%20-%20ZETES%20SA%20NV/AUTOMATION/pytest_fixtures/fixtures_practice.html")

         #Check if the page title is correct
         login_page = LoginPage(driver)#

         assert login_page.get_page_title() == "Pytest Fixtures Practice Page", f"Expected page title to be 'Practice Page' but got '{login_page.get_page_title()}'"

        #Enter username and password and click login
         login_page.login(username, password)
         logger.debug("Entered username and password")
 

        # Verify dashboard visible
         assert login_page.get_success_message() == "Welcome! You are logged in."
         logger.info("Login successful, dashboard is visible") 

         #Logout after successful login
         login_page.logout()