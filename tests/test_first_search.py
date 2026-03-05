from playwright.sync_api import expect
import pytest
from login_page.login_page import LoginPage

def test_item(logged_in_page):
    page = logged_in_page
    page.get_by_role("link", name="Sauce Labs Bike Light").nth(1).click()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Bike Light")

def test_hamburger_menu(logged_in_page):
    page = logged_in_page
    page.get_by_role("button", name="Open Menu").click()
    expect(page.get_by_role("link", name="About")).to_be_visible()

@pytest.mark.smoke
def test_logout_is_visible(logged_in_page):
    page = logged_in_page
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()


def test_not_possible_log_invalid_pass(page, credentials):
    page.goto("/")
    login_page = LoginPage(page)
    login_page.login(
        credentials["username"],
        'some_wrong_password'
    )
    received_error_text = (page.locator('#login_button_container > div > form > div.error-message-container.error > h3')).inner_text()
    expected_error_text = 'Epic sadface: Username and password do not match any user in this service'
    assert received_error_text == expected_error_text
