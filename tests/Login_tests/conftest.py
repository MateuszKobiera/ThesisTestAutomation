import pytest
from selenium import webdriver

from backend.login_api import LoginAPI
from frontend.objects.Pages.account_initalization_page import AccountInitializationPage
from frontend.objects.Pages.terms_and_conditions_page import TermsAndConditionsPage


@pytest.fixture
def terms_page(browser: webdriver):
    return TermsAndConditionsPage(browser)


@pytest.fixture
def account_init_page(browser: webdriver):
    return AccountInitializationPage(browser)


@pytest.fixture
def accept_terms_conditions(login_page):
    login_page.choose_mode('Configuration')
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.login()


@pytest.fixture
def login_api():
    return LoginAPI()
