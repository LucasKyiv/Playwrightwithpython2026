import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("SAUCE_USERNAME"),
        "password": os.getenv("SAUCE_PASSWORD")
    }