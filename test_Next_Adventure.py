from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Tests.Wait_for_element import wait_for_element
from time import sleep


class TestNA:
    browser = None

    def setup_method(self, method):
        # Install and start browser
        driver_path = ChromeDriverManager().install()
        self.browser = webdriver.Chrome(service=Service(driver_path))

    def test_add_to_cart(self, element=None):
        # navigate to webpage
        self.browser.get('https://nextadventure.net/')
        # select category
        wait_for_element(self.browser, By.XPATH, '//*[@id="site-header-nav"]/nav/ul/li[7]/details/summary').click()
        wait_for_element(self.browser, By.XPATH, "//li[@class='navmenu-item          navmenu-item-parent          "
                                                 "navmenu-id-camp-kitchen          navmenu-meganav-standard__item']//a["
                                                 "contains(@data-uw-original-href,'collections/camp-kitchen')]").click()
        # select item and add to cart
        wait_for_element(self.browser, By.ID, '9062671089978').click()
        wait_for_element(self.browser, By.XPATH, "//span[@class='atc-button--text']").click()
        # check out cart
        wait_for_element(self.browser, By.XPATH, "//div[@class='upcart-checkout-button-container styles_Button__-qauK "
                                                 "']").click()
        # Verify Subtotal 
        expected_results = '$365.00'
        actual_results = wait_for_element(self.browser, By.XPATH, "//span[text()='$365.00']").text

        assert actual_results == expected_results
        sleep(10)
