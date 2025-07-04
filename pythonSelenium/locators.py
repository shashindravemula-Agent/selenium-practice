import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("Shashi123")
driver.find_element(By.CSS_SELECTOR, ".form-check-input").click()

#Xpath = //tagname[@attribute = 'value'] -> //input[@type= 'submit']
#CSS Selector = tagname[attribute = 'value'] -> input[type = 'submit']

driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys("shashi")

print(message)


driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("hello again")
#driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()

#static dropdown

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")

time.sleep(60)