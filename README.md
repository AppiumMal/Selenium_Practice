
Framework Structure Explanation:
********************************
Hybrid Layered Selenium Framework with using the Page Object Model pattern, with a dedicated core abstraction layer for actions, waits, and exception handling. The framework separates concerns into core, utilities, and test layers, and uses PyTest fixtures for driver lifecycle management and test orchestration.”

Design Principles:
1.Separation of Concerns  Actions ≠ waits ≠ config ≠ tests

2. Dependency Injection -WaitHelpers receiving dependencies instead of creating them

3. Abstraction - Tests don’t directly use Selenium

4. Reusability - Core methods reused across tests

5.Maintainability - Single place to update behaviour

Test → Page → Actions → WaitHelper → WebDriver
Tests
   ↓
Pages (implicit from your mention)
   ↓
Core Layer (actions, waits, exceptions)
   ↓
Utils Layer (driver, config, logging)
   ↓
Selenium WebDriver

********************************
Automation Engine Layer: Core folder (encapsulates Selenium operations, Hnadle retries/waits , wrap exceptions, provide clean APIs to tests/pages)
*************************************************************************************************************************************************
Core /__init__.py --> file is a special Python file used to mark a directory as a regular Python package. It tells the Python interpreter that the folder contains modules and sub-packages that can be imported.

core/wait_helpers.py
---centralised waits
---contains waits used in the framework.The wait class uses dependency injection to pass what the class needs instead of creating it inside the class.Annotations for clarity and readability to indicate the type of data.
---Technical(selenium) Failures exceptions are Handled in WaitHelpers (element not found).By wrapping selenium TimeoutExceptions with custom exceptions and log the original selenium stack in the logs.
 

core/actions.py 
--- Action class holds the actions methods used throughout the framework like click , enter text and get text
--- Business test failures exceptions are handles in actions (click, type)
-- Test validations/assertion failures are handled in actions (text mismatch)


core/exception.py
---This is custom exception library used in the framework

******************************************************************************************************************************************************************************
Utils layer -Infrastructure Layer (Environment + execution controls)
*********************************************************************************************************************************************************************************

utils (environment/setup/config)

utils/config.py 
--- holds the Base URL value, timeout definition and browser value used for execution

utils/driver_factory.py 
--- holds the Webdriver object, it imports the 'Config' value of the browser and creates it.

utils/webdriver_singleton.py
--- driver lifecycle setup and tear down 

Reporting:
**********

utils/logger.py
--- formats and how the logging is done and saved in separate selenium_tests.log file

******************************************************************************************
Test Orchestration Layer
****************************************************************************************

conftest.py 
--- holds the fixtures(reusable methods with defined scope) used in the framework like calling the base url browser and webdriver setup and quiting in session scope.

**************************************

Page layer
******************************************************************
Each page object represents a specific UI page, where I define locators and encapsulate user interactions as methods. These methods use the actions layer, allowing tests to call high-level business operations without directly interacting with Selenium.”
********************************************************************************************

layer to add Core/assertions.py