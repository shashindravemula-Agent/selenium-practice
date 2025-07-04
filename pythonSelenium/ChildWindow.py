import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])

print(driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.window(WindowsOpened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)