import logging
import os
from datetime import datetime

#factor function takes care of creating and returning the logger and setting up the file handler and console handler
def setup_logger():
    # Create a logger
    logger = logging.getLogger("selenium_tests")
    logger.setLevel(logging.DEBUG)

#Helps to avoid duplicate log entries by clearing existing handlers before adding new ones
    if logger.hasHandlers():
        logger.handlers.clear()

    #create file handler to log messages to a file
    fileHandler = logging.FileHandler("selenium_tests.log")
    #sends the log to console
    console_handler = logging.StreamHandler()


    # Create formatter applies the format to the log messages. The format includes the timestamp, logger name, log level and the message
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   
    # Add formatter to console_handler
    fileHandler.setFormatter(formatter) 
    console_handler.setFormatter(formatter)

    # Add console to logger
    logger.addHandler(fileHandler)
    logger.addHandler(console_handler)
    return logger