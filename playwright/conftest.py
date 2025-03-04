import pytest

def pytest_adoption(parser):
    parser.adoption("--browser_name", action="store", default="chrome", help="browser selection")
    parser.addoption("--url_name", action="store", default="https://rahulshettyacademy.com/client", help="server selection")

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name=="chrome":
        browser=playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # here we should put the url if we have just one url for the application in our project
    # self.page.goto(url_name)
    yield  page
    context.close()
    browser.close()