import pytest

from frontend.Pages.login_page import LoginPage


@pytest.fixture
def login_page(browser):
    yield LoginPage(browser)
