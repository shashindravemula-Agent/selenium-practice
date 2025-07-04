import time

from selenium import webdriver
from selenium.webdriver.common.by import By

BrowserSortedVeggies = []

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#Click on column header
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
#collect all the veggie names -> BrowserSortedVeggiesList
VeggieWebElements  = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in VeggieWebElements:
    BrowserSortedVeggies.append(ele.text)
OriginalBrowserSortedList = BrowserSortedVeggies.copy()

#Sort this BrowserSortedVeggieList ==> newSortedVeggieList
BrowserSortedVeggies.sort()

#veggieList == newSortedVeggieList
assert OriginalBrowserSortedList == BrowserSortedVeggies

time.sleep(5)

