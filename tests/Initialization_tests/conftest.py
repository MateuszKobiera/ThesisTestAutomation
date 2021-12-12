import time

import pytest
from selenium import webdriver

from backend.login_api import LoginAPI
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


@pytest.fixture
def initialization_page_no_wait(browser: webdriver):
    return InitializationPage(browser, wait=False)


@pytest.fixture
def login_api():
    try:
        return LoginAPI()
    except KeyError:
        print('Device is not initialized yet.')


@pytest.fixture
def factory_reset(login_api, initialization_page_no_wait, browser):
    if login_api:
        login_api.post_factory_rest()
        time.sleep(50)
        for tries in range(0, 100):
            try:
                login_api.get_initialization_status()
                break
            except (ValueError, ConnectionError):
                tries += 1
                time.sleep(5)
        time.sleep(10)
        browser.get('http://192.168.1.254/')
        initialization_page_no_wait.wait_for_loading_indicator()
        assert initialization_page_no_wait.url == initialization_page_no_wait.driver.current_url

