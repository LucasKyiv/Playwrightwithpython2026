from playwright.sync_api import expect
import pytest
import os
from login_page.login_page import LoginPage

def test_item(logged_in_page_admin):
    page = logged_in_page_admin
    page.get_by_role("link", name="Sauce Labs Bike Light").nth(1).click()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Bike Light")

def test_hamburger_menu(logged_in_page_admin):
    page = logged_in_page_admin
    page.get_by_role("button", name="Open Menu").click()
    expect(page.get_by_role("link", name="About")).to_be_visible()

@pytest.mark.smoke
def test_logout_is_visible(logged_in_page_admin):
    page = logged_in_page_admin
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()


def test_not_possible_admin_log_invalid_pass(page, credentials):
    page.goto("/")
    login_page = LoginPage(page)
    login_page.login(
        credentials["username"],
        'some_wrong_password'
    )
    received_error_text = (page.locator('#login_button_container > div > form > div.error-message-container.error > h3')).inner_text()
    expected_error_text = 'Epic sadface: Username and password do not match any user in this service'
    assert received_error_text == expected_error_text

@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        {
            "username": os.getenv("SAUCE_USERNAME"),
            "password": os.getenv("SAUCE_PASSWORD"),
            "expected_result": "success",
        },
        {
            "username": os.getenv("LOCKED_USERNAME"),
            "password": os.getenv("LOCKED_PASSWORD"),
            "expected_result": "locked_out",
        },
    ],
)
def test_login_with_different_users(page, username, password, expected_result):
    page.goto("/")
    login_page = LoginPage(page)
    login_page.login(
        username,
        password
    )
    if expected_result == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    elif expected_result == "locked_out":
        received_error_text = (
            page.locator('#login_button_container > div > form > div.error-message-container.error > h3')).inner_text()
        expected_error_text = 'Epic sadface: Sorry, this user has been locked out.'
        assert received_error_text == expected_error_text