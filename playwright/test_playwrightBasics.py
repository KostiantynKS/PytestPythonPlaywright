import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)  # with headless =False we will see the actual opening of the browser
    # context is not mandatory, but better to have for multiple page testing
    context = browser.new_context()   # will execute the code in the new incognito window. Helpful when we need to test with different users
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

# shortcut that will work only in chromium headless mode, 1 single contest, not allowing customization
# We can right click on the green arrow, and modify run configuration. In Additional Arguments provide --headed and it will open the browser
# we can also add --headed at the end of command in terminal to run it in headed mode
def testPlaywrightShortCutPage(page:Page): # page:Page fixture is reference to the import above. Not mandatory, but allow us to see the page. method suggestions
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    # time.sleep(25)
    # should be unique
    page.get_by_role("combobox").select_option("teach")
    page.locator( "#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign in").click()
    time.sleep(15)  # Similarly to Thread.sleep telling code to wait so we can see the result

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("ololo")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign in").click()
    # checking the error message
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefoxBrowser(playwright:Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    # we doesn't use context because all test happens within the one page only
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator( "#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign in").click()

    # For the CSS reminder
 #   #id   example:  page.locator(#terms").click()
 #   .class

    # to use get_by_label an element obviously should have the label tag, and the input should be inside the label
    # OR label for="" is matching with id that is outside