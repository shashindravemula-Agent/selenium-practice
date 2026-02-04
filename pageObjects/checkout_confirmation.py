from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserUtils import BrowserUtils


class Checkout_Confiramtion(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_btn = (By.XPATH, "//button[@class = 'btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox_click = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
        self.submit_btn = (By.XPATH, "//input[@type='submit']")
        self.success_message = (By.CSS_SELECTOR, "div[class*='alert-success']")



    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

    def delivery_address(self,countryName):
        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.country_option)))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox_click).click()
        self.driver.find_element(*self.submit_btn).click()

    def validation(self):
        SuccessText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in SuccessText