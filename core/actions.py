from selenium.common.exceptions import TimeoutException
from core.exceptions import UIActionException
from core.wait_helpers import wait


def click(locator, description, timeout=Timeout.STANDARD):
    try:
        element = wait.until_visible(locator, timeout)
        element.click()

    except TimeoutException as e:
        message = build_failure_message(
            description,
            "click",
            f"element not visible after {timeout}s"
        )
        raise UIActionException(message, e)