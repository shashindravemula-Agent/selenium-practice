import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("traverse_myself")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("Sansun@2438")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()


time.sleep(60)