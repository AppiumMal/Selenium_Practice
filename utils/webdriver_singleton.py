from utils.driver_factory import DriverFactory
from utils.config import Config


#the purpose of this WebDriverSingleton.py is implement 'Singleton' design pattern for WebDriver instance, so that we can reuse the same instance across multiple tests without creating a new one each time.

class WebDriverSingleton: 
   _driver = None

#Singleton for chrome driver instance
   @classmethod

   def get_driver(cls):
       if cls._driver is None:
          cls._driver = DriverFactory.create_driver(Config.get_browser())
       return cls._driver
   


#Method to quit the driver instance, can be called at the end of the test session to clean up resources.
   @classmethod
   def quit_driver(cls):
        if cls._driver is not None:
              cls._driver.quit()
        cls._driver = None

class WebDriverWaitConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.timeout = 10
        return cls._instance                         