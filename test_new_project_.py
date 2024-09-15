

# Verify 'New Project' text appears once project '+' icon button is clicked




import self
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from Tests.Reusable_Login_Orch import login_to_orchestra






class TestOrchestra:
    def test_login(self):
        browser = login_to_orchestra('user_email', "user_password")

        # Click 'task icon'
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='nav-bar-element navbar-action']"))
        ).click()

        # Click plus icon button
        plus_icon = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-v-754d6337='' and @data-v-c62a3f61='']")
            )
        )
        plus_icon.click()

        # Verify 'New Project' text is shown
        actual_results = (
            browser.find_element(By.XPATH, "//div[@class='or-input-placeholder' and text()='New Project']")
            .text)
        expected_results = 'New Project'
        assert actual_results == expected_results


sleep(15)
