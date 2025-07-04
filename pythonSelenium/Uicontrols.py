import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.find_element(By.ID, "checkBoxOption1").click()

#if there will be no ID,NAME,TYPE and having only one "value" we can go in this way like in list type.
# using find_elements and also using XPATH.
#and also we dont know that option1 can be in first place or in any other place like secondplace or in third place.
#in than case we use for loop and will write the below condition.

checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

#radiobuttons
#for radiobuttons they won't change it will be in the same place not like the above one.
radiobuttons = driver.find_elements(By.XPATH, "//input[@type = 'radio']")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()






time.sleep(60)