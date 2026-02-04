from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.CLASS_NAME,"btn1").click()
driver.find_element(By.ID, "firstName").send_keys("shashindra")
driver.find_element(By.ID, "lastName").send_keys("vemula")
driver.find_element(By.ID, "userEmail").send_keys("shashindravemula@gmail.com")
driver.find_element(By.ID, "userMobile").send_keys("9876543210")
dropdown = Select(driver.find_element(By.CLASS_NAME,"custom-select"))
dropdown.select_by_index(3)
radiobuttons = driver.find_elements(By.CLASS_NAME,"mt-3")
radiobuttons[0].click()
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Shashi@24")
driver.find_element(By.ID,"confirmPassword").send_keys("Shashi@24")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.ID,"login").click()


assert radiobuttons[0].is_selected()

