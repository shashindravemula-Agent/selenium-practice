import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pythonSelenium.Explicitwaitdemo import TotalAmount

# implicitly_wait is a global wait that will work in everytime when page loads for 5 sec.
# if the page loads in 2 sec then the remaining 3 sec will be saved for us. but not with using time.sleep()


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

#Assignment [1]
expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []

products = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
for product in products:
    actualList.append(product.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH, "div/button").click()

print(actualList)
assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//div[@class = 'action-block']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text() = 'Apply']").click()

#explicitDemo
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

TotalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(TotalAfterDiscount)

assert TotalAmount > TotalAfterDiscount

#sum of the products

prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

TotalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == TotalAmount







