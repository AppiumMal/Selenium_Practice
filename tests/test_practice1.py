
from utils.webdriver_singleton import WebDriverSingleton 
from utils.config import Config 
from pages.login_page import LoginPage
from utils.logger import setup_logger
import pytest

logger = setup_logger() 

 

class TestLoginPractice:
      
      def test_practice1(self,driver):
    
        
        logger.info("Starting test_practice1")
        #open the webpage
        
        login_page = LoginPage(driver)

        assert login_page.get_page_title() == "Pytest Fixtures & Page Object Practice", \
        f"Expected 'Pytest Fixtures & Page Object Practice' but got '{login_page.get_page_title()}'"

        logger.info(f"Opened webpage: {Config.BASE_URL }")

    
      @pytest.mark.parametrize("username, password", [("tester", "pytest"), ("admin","admin123"), ("guest","guest123")])


      def test_practice2(self, driver, username, password):
         
         logger.info("Starting login test_practice2")     

         #Check if the page title is correct
          
         login_page = LoginPage(driver)
         

        #Enter username and password and click login
         login_page.login(username, password)
         logger.debug("Entered username and password")
 

        # Verify dashboard visible
         assert login_page.get_success_message() == "Welcome," + " " +username+"!"
         logger.info("Login successful, dashboard is visible") 

         #Logout after successful login
         login_page.logout()