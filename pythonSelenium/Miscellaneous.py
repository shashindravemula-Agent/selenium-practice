import time

from selenium import webdriver

#we can run headless mode (ex - without opening the browser for testing on back)
#headmode - as usual we test by automating the browser by opening.
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
#headless mode
#driver = webdriver.Chrome(options = chrome_options)

#if we see any popups like safety protection etc. we can automate that also before going to actual site.
#chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#we are invoking 'JAVASCRIPT' By using selenium in python:

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
time.sleep(2)