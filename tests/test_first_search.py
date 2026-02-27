from playwright.sync_api import expect

def test_item(logged_in_page):
    page = logged_in_page
    page.get_by_role("link", name="Sauce Labs Bike Light").nth(1).click()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Bike Light")

def test_hamburger_menu(logged_in_page):
    page = logged_in_page
    page.get_by_role("button", name="Open Menu").click()
    expect(page.get_by_role("link", name="About")).to_be_visible()

