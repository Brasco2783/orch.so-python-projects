# Select category, add item to shopping cart and verify price from item page is equal to item subtotal at checkout

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

  def test_google_maps_directions(self):
        # navigate to webpage
        self.browser.get('https://nextadventure.net/')
        
        # google map to main PDX store
        wait_for_element(self.browser, By.XPATH, "//a[text()='Locations']").click()
        wait_for_element(self.browser, By.XPATH, "//a[@class='sc-brPMkR hVSHHp pf-18_ pf-button-4']").click()
        time.sleep(10)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        expected_url = "https://www.google.com/maps/place/Next+Adventure+Portland+Outdoor+Store/"
        actual_url = self.browser.current_url
        assert expected_url in actual_url

        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

        # google map to PDX paddle sports
        wait_for_element(self.browser, By.XPATH, "//a[@class='sc-brPMkR hVSHHp pf-26_ pf-button-4']").click()
        time.sleep(10)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        expected_url = "https://www.google.com/maps/place/Next+Adventure+Portland+Paddle+Sports+Center/"
        actual_url = self.browser.current_url
        assert expected_url in actual_url

        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

        # google map to Scappoose paddle sports
        wait_for_element(self.browser, By.XPATH, "//a[@class='sc-brPMkR hVSHHp pf-34_ pf-button-4']").click()
        time.sleep(10)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        expected_url = "https://www.google.com/maps/place/Next+Adventure+Scappoose+Bay+Paddle+Sports+Center/"
        actual_url = self.browser.current_url
        assert expected_url in actual_url

        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

        # google map to Sandy store
        wait_for_element(self.browser, By.XPATH, "//a[@class='sc-brPMkR hVSHHp pf-42_ pf-button-4']").click()
        time.sleep(10)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        expected_url = "https://www.google.com/maps/place/Next+Adventure+Sandy+Outdoor+Store/"
        actual_url = self.browser.current_url
        assert expected_url in actual_url

        self.browser.quit()
