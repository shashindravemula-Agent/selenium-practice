from selenium.webdriver.common.by import By

def test_sort(browserInstance):
    driver = browserInstance
    BrowserSortedVeggies = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Click on column header
    driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
    # collect all the veggie names -> BrowserSortedVeggiesList
    VeggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for ele in VeggieWebElements:
        BrowserSortedVeggies.append(ele.text)
    OriginalBrowserSortedList = BrowserSortedVeggies.copy()

    # Sort this BrowserSortedVeggieList ==> newSortedVeggieList
    BrowserSortedVeggies.sort()

    # veggieList == newSortedVeggieList
    assert OriginalBrowserSortedList == BrowserSortedVeggies