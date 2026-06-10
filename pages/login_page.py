from selenium.webdriver.common.by import By
from core.wait_helpers import( wait_for_element_present, wait_for_element_visible_and_enter_text, wait_for_element_visible_clickable)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

  #Locators for the login page elements
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[onclick='login()']")
    dashboard = (By.ID, "dashboard")
    page_title = (By.TAG_NAME, "h1")
    logout_button = (By.CSS_SELECTOR, "button[onclick='logout()']")
    success_message = (By.CLASS_NAME, "message")


        
    def get_page_title(self):
          by, value = self.page_title
          return wait_for_element_present(self.driver, by, value).get_attribute("textContent")

    def login(self, username, password):
    
         # username
        by, value = self.username_input
        wait_for_element_visible_and_enter_text(self.driver, by, value, username)

        # password
        by, value = self.password_input
        wait_for_element_visible_and_enter_text(self.driver, by, value, password)

        # click login
        by, value = self.login_button
        wait_for_element_visible_clickable(self.driver, by, value)

    def is_dashboard_visible(self):
        by, value = self.dashboard
        dashboard_element = wait_for_element_present(self.driver, by,value)
        return dashboard_element.is_displayed()    
    
    def logout(self):
        wait_for_element_visible_clickable(self.driver, self.logout_button)

    def get_success_message(self):
        by, value = self.success_message
        element = wait_for_element_present(self.driver, by, value)
        return element.text
   