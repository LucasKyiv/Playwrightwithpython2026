import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }