import time

from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


# api call from browser -> api call contact server return back response to browser -> browser use response to generate html data
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details/6711e249ae2afd4c0b9f6fb0")


# in this scenario we are intercepting the request call, and telling the test to continue with different url instead of the one that we had
# here we put order id from the different account to see how it will work
def test_Network_2(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    time.sleep(2)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message=page.locator(".blink_me").text_content()
    print(message)
    time.sleep(5)

# The scenario how to do manipulations with the page without logging every time and just by passing token
# In devtools, near Network, there is Application. In there you can get a Local storage (on the left)
# There will be stored token after we logged in. It will disappear after logging out or the token expired
# While the token is there, all manipulations will be identified as that user. So no need to login all the time

def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    getToken=api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Script to inject token in session local storage
    page.add_init_script(F"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()