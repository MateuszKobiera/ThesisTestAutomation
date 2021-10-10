import pytest
from selenium import webdriver

from frontend.Pages.initialization_page import InitializationPage


@pytest.fixture
def initialization_page(browser: webdriver):
    return InitializationPage(browser)
