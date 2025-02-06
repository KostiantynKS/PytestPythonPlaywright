from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Hide/display and placeholder

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    # to filter regular locators we are using method chaining
    # to filter within get_by we should do it inside parentheses
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    # Mouse Hover
    page.locator("mousehover").hover()
    page.get_by_role("link", name="Top").click()

    # Frame handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

    #Table handling
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index
            # whenever we have f at the beginning everything inside {} will be treated as variable and will be executed at runtime
            print(f"Price column value is {priceColValue}")
            break

    riceRow = page.locator("tbody").locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_contain_text("37")
