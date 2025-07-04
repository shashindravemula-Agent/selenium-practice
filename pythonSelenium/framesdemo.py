import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonSelenium.Uicontrols import radiobuttons

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,1500)")
driver.switch_to.frame("courses-iframe")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)
