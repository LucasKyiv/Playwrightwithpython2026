import os
import pytest
from dotenv import load_dotenv
from login_page.login_page import LoginPage
from playwright.sync_api import expect

load_dotenv()

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("SAUCE_USERNAME"),
        "password": os.getenv("SAUCE_PASSWORD")
    }


@pytest.fixture
def logged_in_page(page, credentials, base_url):
    page.goto("/")

    login_page = LoginPage(page)
    login_page.login(
        credentials["username"],
        credentials["password"]
    )
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()
    return page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig):
    return {
        **browser_context_args,
        "base_url": pytestconfig.getini("base_url"),
        "viewport": None
    }