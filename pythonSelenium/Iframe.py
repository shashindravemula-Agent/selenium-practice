import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

# switch to iframe
driver.switch_to.frame("mce_0_ifr")

# locate the editor
editor = driver.find_element(By.ID, "tinymce")

# clear existing text (CTRL + A then BACKSPACE)
editor.send_keys(Keys.CONTROL + "a")
editor.send_keys(Keys.BACKSPACE)

# type new text
editor.send_keys("shashindra sai is currently learning iframes.")

time.sleep(3)
driver.quit()
