import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

# showing the path to our file with data
with open('data/credentials.json') as f:
    #storing data from file into variable
    test_data = json.load(f)
    print(test_data)
    # accessing certain array from the test data
    user_credentials_list = test_data['user_credentials']

# using pytest annotation to pass the list of credentials data 'user_credentials' is just the name we made up
# It will grab the first set of data from the list, and then it will check is there are the next one and start over with the next set
@pytest.mark.parametrize('user_credentials', user_credentials_list)
# 'user_credentials' in here is a fixture, that has to be executed first. It will first check local file, then check global file
def test_e2e_web_api(playwright:Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    # logging in
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()


    # time.sleep(2)

