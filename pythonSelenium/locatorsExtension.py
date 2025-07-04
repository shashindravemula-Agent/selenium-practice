import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("Happy@gmail.com")
driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("Yes123")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Yes123")
driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()






time.sleep(60)