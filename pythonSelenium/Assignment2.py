import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
#message = driver.find_element(By.CSS_SELECTOR, ".red").text
email_str = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
email = email_str[18:48].strip()

#var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(WindowsOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
print(driver.find_element(By.CSS_SELECTOR, ".alert").text)

time.sleep(10)
