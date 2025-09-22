import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)


driver.get("https://expired.badssl.com/")
#driver.find_element(By.XPATH, "//button[text() = 'Back to safety']").click()
time.sleep(2)