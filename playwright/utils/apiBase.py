from playwright.sync_api import Playwright
ordersPayload= {"orders":[{"country":"Pakistan","productOrderedId":"6581cade9fd99c85e8ee7ff5"}]}
tokenPayloadData={"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}


class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/auth/login",
                                 data=tokenPayloadData)
        assert response.ok
        print(response.json())
        responseBody=response.json()
        return responseBody["token"]


    def createOrder(self, playwright:Playwright):
        # to call the method within class we are using self
        token=self.getToken(playwright)
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