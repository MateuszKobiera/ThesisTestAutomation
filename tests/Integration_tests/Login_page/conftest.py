import pytest
from selenium import webdriver

from frontend.Pages.login_page import LoginPage


@pytest.fixture
def login_page(browser: webdriver):
    return LoginPage(browser)
