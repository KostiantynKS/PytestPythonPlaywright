import time

from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign in").click()
    # page.locator will serch the whole page
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    # by limiting the search to this iphoneProduct we are limiting the search to one particular locator
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    # page.locator('//a[contains(text(), "Checkout")]').click()  optional. do the same
    # nice assertion to check the amount of elements
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(10)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # we are telling driver that there will be another window opened
    # all window child operations should be within this popup closure
    # as soon as we get out we will have to create a new one
    with page.expect_popup() as newPage_info: # saving the new page object
        page.locator(".blinkingText").get_by_text("Free Access").click() #will be on a new page
        childPage = newPage_info.value  # assigning the name to the new page object
        text = childPage.locator(".red").text_content()
        email = ""
        words=text.split() # splitting strings by empty space
        for word in words:
            if "@" in word:
                email=word
        # expect is Plywright specific function for locators and responces
        # For plain string comparisons, use PyTest's built-in assert
        assert email == 'mentor@rahulshettyacademy.com'

