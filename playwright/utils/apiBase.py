from playwright.sync_api import Playwright
ordersPayload= {"orders":[{"country":"Belarus","productOrderedId":"67a31f69e2b5443b1f483c21"}]}


class APIUtils:

    def getToken(self, playwright: Playwright, user_credentials):
        # extracting data from user_credentials and placing them into the variables
        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": user_email,"userPassword":user_password})
        assert response.ok
        print(response.json())
        responseBody=response.json()
        return responseBody["token"]


    def createOrder(self, playwright:Playwright, user_credentials):
        # to call the method within class we are using self
        token=self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                data=ordersPayload,
                                headers={"Authorization":token,
                                         "Content-Type":"application/json"
                                         })
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId