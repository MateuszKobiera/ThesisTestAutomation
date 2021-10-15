import pytest
from selenium import webdriver

from frontend.objects.Pages.base_page import BasePage
from frontend.objects.Pages.login_page import LoginPage
from frontend.objects.Pages.menu_page import MenuPage


@pytest.fixture
def browser() -> webdriver:
    driver = webdriver.Chrome()
    page = BasePage(driver)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(page.base_url)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(browser: webdriver):
    return LoginPage(browser)


@pytest.fixture
def log_in(login_page):
    login_page.choose_mode('Configuration')
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.login()


@pytest.fixture
def menu_page(browser: webdriver):
    return MenuPage(browser)
