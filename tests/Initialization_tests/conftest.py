import pytest
from selenium import webdriver

from frontend.objects.Pages.initialization_page import InitializationPage

PASSWORD_VALIDATION = {
    'a': 'Password must have at least 10 characters',
    'abcdefghij': 'Password must have at least one upper case letter',
    'ABCDEFGHIJ': 'Password must have at least one lower case letter',
    'Abcdefghij': 'Password must have at least one digit',
    'Abcdefghij1': 'Password must have at least one special character',
    'Abcdefghij1ą': 'Password must only contain alphanumerical characters'}


@pytest.fixture
def initialization_page(browser: webdriver):
    return InitializationPage(browser)
