import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_page_title(setup):
    driver = setup
    driver.get("https://www.google.com/")

    assert driver.title == "Google"