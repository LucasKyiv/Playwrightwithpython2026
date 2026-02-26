from playwright.sync_api import expect
from login_page.login_page import LoginPage

def test_item(page, credentials):
    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com/")
    login_page.login(
        credentials["username"],
        credentials["password"]
    )
    page.get_by_role("link", name="Sauce Labs Bike Light").nth(1).click()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Bike Light")
