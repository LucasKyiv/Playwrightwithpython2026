from playwright.sync_api import Page, expect

def test_example_login(page: Page) -> None:
    # Go to https://www.saucedemo.com/
    page.goto("https://www.saucedemo.com/")

    # Click [data-test="login-button"]
    page.locator("[data-test=\"login-button\"]").click()
    error_text = page.locator("//h3[@data-test='error']").text_content()
    assert error_text == 'Epic sadface: Username is required'

