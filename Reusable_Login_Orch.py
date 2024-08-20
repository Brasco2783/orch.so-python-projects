from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def login_to_orch(email, password):
    # Install and start browser
    driver_path = ChromeDriverManager().install()
    browser = webdriver.Chrome(service=Service(driver_path))

    # navigate to webpage
    browser.get('https://app.orch.so/login?return_url=/')

    # Input Valid email address
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email' and @class='or-input-input']"))
    )
    email_input.send_keys(email)

    # click 'Continue' button
    browser.find_element(By.XPATH, "//div[@class='or-button-content' and text()='Continue']").click()

    # Input valid password
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='or-input-input' and @type='password']"))
    )
    password_input.send_keys(password)

    # Click 'Signin'
    browser.find_element(By.XPATH, "//div[@class='or-button-content' and text()='Sign in']").click()

    return browser


email = "user_email"
password = "user_password"

# login function
browser = login_to_orch(email, password)

# quit the browser
browser.quit()
