import pytest
from selenium import webdriver

from frontend.Pages.account_initalization_page import AccountInitializationPage
from frontend.Pages.terms_and_conditions_page import TermsAndConditionsPage


@pytest.fixture
def terms_page(browser: webdriver):
    return TermsAndConditionsPage(browser)


@pytest.fixture
def logowanie(login_page):
    login_page.choose_mode('Configuration')
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.login()


@pytest.fixture
def account_init_page(browser: webdriver):
    return AccountInitializationPage(browser)
