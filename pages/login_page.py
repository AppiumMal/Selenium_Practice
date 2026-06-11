from selenium.webdriver.common.by import By
from core.actions import Actions
from typing import Tuple
Locator = Tuple[str,str]
from core.wait_helpers import WaitHelpers

class LoginPage:


  #Locators for the login page elements
    USERNAME :Locator =(By.ID, "username")
    PASSWORD :Locator =(By.ID, "password")
    LOGIN_BUTTON :Locator =(By.CSS_SELECTOR, "button[onclick='login()']")
    DASHBOARD :Locator =(By.ID, "dashboard")
    PAGE_TITLE :Locator =(By.TAG_NAME, "h1")
    LOGOUT_BUTTON :Locator =(By.CSS_SELECTOR, "button[onclick='logout()']")
    SUCESS_MESSAGE :Locator =(By.CLASS_NAME, "message")

   
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelpers(driver)
        self.actions = Actions(driver, self.wait)


    def get_text(self, locator: Locator) -> str:
          
          return self.actions.get_text(locator)

    def login(self, username:str, password:str):
    
         # username
       self.actions.type(self.USERNAME,username)

        # password
       self.actions.type(self.PASSWORD,password)

        # click login

       self.actions.click(self.LOGIN_BUTTON)
  

    def get_page_title(self) -> str:
       return self.actions.get_text(self.PAGE_TITLE)

    def get_success_message(self) -> str:
       return self.actions.get_text(self.SUCESS_MESSAGE)


    
    def logout(self):
        self.actions.click(self.LOGOUT_BUTTON)


   