from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Step 1: Click on the "Price" header to sort
driver.find_element(By.XPATH, "//tr/th[2]").click()

# Step 2: Capture all the price elements from the column
prices = driver.find_elements(By.XPATH, "//tr/td[2]")

# Step 3: Convert web elements text to integer list
price_list = [int(price.text) for price in prices]

# Step 4: Copy list & sort it
sorted_list = sorted(price_list)

# Step 5: Compare UI sorted vs programmatically sorted
assert price_list == sorted_list, "Sorting not working correctly"

print("✅ Sorting by price works as expected!")

driver.quit()
