
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config import Config


class DriverFactory:
    @staticmethod
    def create_driver(B):
         config = Config()
         if Config.BROWSER == "CHROME":
            options = Options()
            options.add_argument("--start-maximized")
            #options.add_argument("--headless")  # Uncomment for headless mode
            return webdriver.Chrome(options=options)
         elif Config.BROWSER  == "FIREFOX":
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            #options.add_argument("--headless")  # Uncomment for headless mode
            return webdriver.Firefox(options=options)
         else:
            raise ValueError(f"Unsupported browser: {config.BROWSER}")