import datetime
from pathlib import Path

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


def pytest_html_report_title(report):
    report.title = "Building Ecosystem tests"


def pytest_configure(config):
    main_dir: Path = Path(__file__).parent.parent
    report_dir: Path = main_dir.joinpath('Reports')
    if not report_dir.exists():
        report_dir.mkdir()
    report_path: Path = report_dir.joinpath(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}')
    report_path.mkdir()
    config.option.htmlpath = report_path.joinpath('Report.html')
