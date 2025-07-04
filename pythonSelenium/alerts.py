import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "name").send_keys("shashi")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert "shashi" in alertText
alert.accept()





time.sleep(60)