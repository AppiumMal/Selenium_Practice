#This file contains helper functions for waiting for elements to be present, visible, or clickable on the page. These functions can be used in the test files to ensure that the tests wait for the necessary conditions before interacting with the elements.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Wait for an element to be present on the page
def wait_for_element_present(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value))) 

# Wait for an element to be visible and clickable on the page
def wait_for_element_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value))) 

# Wait for an element to be visible on the page and enter text into it
def wait_for_element_visible_and_enter_text(driver, by, value, text, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    element.send_keys(text)
    return element

#wait for an element to be visible on the page and click on it    
def wait_for_element_visible_clickable(driver,by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element