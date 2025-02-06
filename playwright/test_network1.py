from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

# api call from browser -> api call contact server return back response to browser -> browser use response to generate html data
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

# Intercepting the response and replacing it with the fake data to see, how page would respond if there are no orders
def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)