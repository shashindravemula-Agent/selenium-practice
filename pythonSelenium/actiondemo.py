import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# class name for actions are called ActionChains
action = ActionChains(driver)
action.double_click(driver.find_element(By.ID, "checkBoxOption1")).perform()
#action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
#action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(2)
