import self
from selenium import webdriver  # This line imports the webdriver module
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


class TestGettop:
    browser = None

    def setup_method(self, method):
        # Install and start browser
        driver_path = ChromeDriverManager().install()
        self.browser = webdriver.Chrome(service=Service(driver_path))

    def test_email_password_signin(self):
        # navigate to webpage
        self.browser.get('https://app.orch.so/login?return_url=/')

        # Input Valid email address
        email_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email' and @class='or-input-input']"))
        )
        email_input.send_keys("Dean75@pretreer.com")

        entered_text = email_input.get_attribute('value')
        print(f"Entered email: {entered_text}")

        # click 'Continue' button
        self.browser.find_element(By.XPATH, "//div[@class='or-button-content' and text()='Continue']").click()

        # Input valid password
        password_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='or-input-input' and @type='password']"))
        )
        password_input.send_keys('4xlOI4vb_cB0h8kY99sV')

        # Click 'Signin
        self.browser.find_element(By.XPATH,"//div[@class='or-button-content' and text()='Sign in']").click()

        # Verify Header is John Oates
        expected_result = 'John_Oates'
        actual_result = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='header-name']"))
        ).text
        assert actual_result == expected_result

        sleep(5)

        self.browser.quit()

