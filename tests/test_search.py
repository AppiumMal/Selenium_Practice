""" 🔹 A. Search functionality (great for locators)
✅ Test ideas:
•	Type "admin" → only admin visible
•	Type partial "te" → tester appears
•	Type invalid "xyz" → empty list
👉 You’ll practice:
•	find_elements
•	filtering visible elements """


from utils.webdriver_singleton import WebDriverSingleton 
from utils.config import Config 
from pages.search_page import SearchPage
from utils.logger import setup_logger
import pytest

logger = setup_logger() 

class TestSearchPractice:
     
 @pytest.mark.parametrize(
    "search_input, expected",
    [
        ("admin", ["admin"]),
        ("te", ["tester"]),
        ("xyz", [])
    ]
)
 def test_search(self, driver, search_input, expected):


    logger.info("Starting Search functionality tests")
    search_page = SearchPage(driver)

    logger.info(f"Opened webpage: {Config.BASE_URL }")

    #get title of the page
    search_page.get_text(search_page.PAGE_TITLE)

    #enter text in the seach field
    search_page.search_enter_text(search_input)
    
    # perform search
    
    result = search_page.get_filtered_roles(search_input)

    assert result == expected
