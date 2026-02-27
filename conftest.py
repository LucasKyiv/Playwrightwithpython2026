import os
import pytest
from dotenv import load_dotenv
from login_page.login_page import LoginPage

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

    return page