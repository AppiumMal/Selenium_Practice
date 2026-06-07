from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import driver
from utils.wait_helpers import wait_for_element_present, wait_for_element_visible_and_enter_text, wait_for_element_visible_clickable
from utils.logger import setup_logger
import pytest

logger = setup_logger() 

@pytest.mark.parametrize("username, password", [("tester", "pytest"), ("admin","admin123"), ("guest","guest123")])
class LoginPracticeTests:
      
      def test_practice1(driver):
    
       url =  r"file:///C:/Users/Malathy.Ranganathan/OneDrive - ZETES SA NV/AUTOMATION/pytest_fixtures/fixtures_practice.html"

       logger.info("Starting test_practice1")
       #open the webpage
       driver.get(url)
       logger.info(f"Opened webpage: {url}")

    

      def test_practice2(driver,username, password):
         logger.info("Starting login test_practice2")

         #Check if the page title is correct
         page_title = wait_for_element_present(driver, By.TAG_NAME, "h1").text
         logger.debug(f"Page title found: {page_title}")

         assert page_title == "Pytest Fixtures Practice Page", f"Expected page title to be 'Practice Page' but got '{page_title}'"

        #Enter username and password and click login
         wait_for_element_visible_and_enter_text(driver, By.ID, "username", username)
         wait_for_element_visible_and_enter_text(driver, By.ID, "password", password)
         logger.debug("Entered username and password")
 
         login_button = wait_for_element_visible_clickable(driver, By.CSS_SELECTOR,  "button[onclick='login()']")
         login_button

        # Verify dashboard visible
         dashboard = wait_for_element_present(driver, By.ID, "dashboard")
         assert dashboard.is_displayed(), "Dashboard should be visible after login"
         logger.info(f"Login successful for user: {username}")