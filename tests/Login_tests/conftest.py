import pytest
from selenium import webdriver

from backend.login_api import LoginAPI
from backend.mocked_data.property import property_data, building_data, floor_data
from backend.mocked_data.user import admin_account_init, another_user
from backend.my_property_api import MyPropertyAPI
from frontend.objects.Pages.account_initalization_page import AccountInitializationPage
from frontend.objects.Pages.terms_and_conditions_page import TermsAndConditionsPage


@pytest.fixture
def terms_page(browser: webdriver):
    return TermsAndConditionsPage(browser, wait=False)


@pytest.fixture
def account_init_page(browser: webdriver):
    return AccountInitializationPage(browser)


@pytest.fixture
def accept_terms_conditions(login_page):
    login_page.choose_mode('Configuration')
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.click_login()


@pytest.fixture
def login_api():
    return LoginAPI()


@pytest.fixture
def my_property_api():
    return MyPropertyAPI()


@pytest.fixture
def setup_admin_user(login_api):
    if login_api.get_initialization_status() not in ['CoreInitializationDone', 'StructureInitializationDone']:
        login_api.put_initialize_account_data('Admin', admin_account_init())
        login_api.post_core_init()


@pytest.fixture
def setup_building(my_property_api):
    if len(my_property_api.get_zone_instances()) < 3:
        my_property_api.post_property(property_data())
        my_property_api.post_property(building_data())
        my_property_api.post_property(floor_data())


@pytest.fixture
def setup_another_user(login_api):
    if not len(login_api.get_all_users()) > 1:
        login_api.post_create_user(another_user())


@pytest.fixture
def setup_admin_password(login_api, browser):
    if login_api.get_initialization_status() != 'NotDone':
        browser.get('http://192.168.1.254/')
    else:
        ValueError('Init not done')


@pytest.fixture
def log_in_as_user(login_page):
    login_page.choose_mode('Configuration')
    login_page.set_username('User')
    login_page.set_password('Smartspaces2!')
    login_page.click_login()

