from selenium.webdriver.common.by import By
from core.actions import Actions
from typing import Tuple
Locator = Tuple[str,str]
from core.wait_helpers import WaitHelpers

class SearchPage:
    
    #Locators for the search page elements
    PAGE_TITLE :Locator =(By.XPATH, "//h3[text()='Search Users']")
    SEARCH_INPUT:Locator=(By.ID,"search-box")
    SEARCH_LIST:Locator=(By.ID,"user-list")
    USER_ITEMS: Locator = (By.CSS_SELECTOR, "#user-list li")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelpers(driver)
        self.actions = Actions(driver, self.wait)

    #get the text 
    def get_text(self, locator: Locator) -> str:
          
          return self.actions.get_text(locator)
    
    #Type the text in the search field
    
    def search_enter_text(self,search_input:str):
         
         #search text
         self.actions.type(self.SEARCH_INPUT,search_input)

    #Method to validate the sreach text
    def is_user_present(self, search_input: str) -> bool:
     elements = self.actions.find_elements(self.USER_ITEMS)

     for el in elements:
        if el.text.strip().lower() == search_input.lower():
            return True

     return False
    
    def get_filtered_roles(self, search_input: str):
       # ✅ Wait until at least one visible result OR empty state stabilises
        self.wait.wait_for_condition(
        lambda d: len(d.find_elements(*self.USER_ITEMS)) >= 0
       )

        elements = self.actions.find_elements(self.USER_ITEMS)

        texts = [
        el.text.strip().lower()
        for el in elements
        if el.is_displayed() and el.text.strip()
        ]
        return [t for t in texts if search_input.lower() in t]


 