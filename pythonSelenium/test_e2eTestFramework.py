import json
import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage
test_data_path = "/home/kondas/PycharmProjects/selenium-practice/data/test_e2eTestFramework.json"
with open (test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_listItem", test_list)
def test_e2e(browserInstance, test_listItem):
    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopPage = loginPage.login(test_listItem["userEmail"], test_listItem["userPassword"])
    shopPage.add_to_cart(test_listItem["productName"])
    print(shopPage.getTitle())
    checkout_confirmation = shopPage.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.delivery_address("ind")
    checkout_confirmation.validation()


    # regular expressions customized in XPATH and CSS SELECTOR:
    # CSS = a[href* = 'shop']
    # XPATH = //a[contains(@href,'shop')]

