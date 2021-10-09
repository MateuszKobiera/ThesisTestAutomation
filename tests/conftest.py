import pytest
from selenium import webdriver

from frontend.Pages.base_page import BasePage
from frontend.Pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser() -> webdriver:
    driver = webdriver.Chrome()
    page = BasePage(driver)
    driver.maximize_window()
    driver.get(page.base_url)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login_page(browser: webdriver):
    return LoginPage(browser)

