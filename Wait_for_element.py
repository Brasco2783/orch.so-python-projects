
# WebDdriverWait reusable // allows to reuse the explicit wait in multiple places without writing it out each time. 

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_element(browser, by, value, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((by, value))
    )
