import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
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
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):
    userName = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    # logging Page
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage=loginPage.login(userName, password)

    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    orderHistoryPage = orderHistoryPage.selectOrder(orderId)
    orderHistoryPage.verifyOrderMessage()
    # context.close()



