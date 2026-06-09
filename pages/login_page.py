from selenium.webdriver.common.by import By
from utils.wait_helpers import( wait_for_element_present, wait_for_element_visible_and_enter_text, wait_for_element_visible_clickable)

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

    def get_page_title(self):
        return wait_for_element_present(self.driver, *self.page_title).text

    def login(self, username, password):
        wait_for_element_visible_and_enter_text(self.driver, self.username_input,username)
        wait_for_element_visible_and_enter_text(self.driver, self.password_input,password)
        wait_for_element_visible_clickable(self.driver, self.login_button)

    def is_dashboard_visible(self):
        dashboard_element = wait_for_element_present(self.driver, self.dashboard)
        return dashboard_element.is_displayed()    
    
    def logout(self):
        wait_for_element_visible_clickable(self.driver, self.logout_button)