import datetime
import os
from pathlib import Path

import pytest
import pytest_html
from pytest_html import extras
from selenium import webdriver

from frontend.objects.Pages.base_page import BasePage
from frontend.objects.Pages.login_page import LoginPage
from frontend.objects.Pages.menu_page import MenuPage
from frontend.test_logger import get_logger


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
    reports_dir: Path = main_dir.joinpath('reports')
    if not reports_dir.exists():
        reports_dir.mkdir()
    config.option.session_report_dir = reports_dir.joinpath(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}')
    config.option.session_report_dir.mkdir()
    config.option.htmlpath = config.option.session_report_dir.joinpath('Report.html')
    config.option.screenshots_dir = config.option.session_report_dir.joinpath('screenshots')
    config.option.screenshots_dir.mkdir()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == 'call' and rep.failed:
        extra = getattr(rep, 'extra', [])
        filename = f'screenshots/{item.name}.png'
        extra.append(extras.html(f"<div class='image'><a target='_blank' href='{filename}'><img src='{filename}'></a></div>"))


@pytest.fixture(autouse=True)
def screenshot_on_fail(request, browser: webdriver, test_logger, extra):
    """
    Save screen on test failure
    :param request:
    :param browser:
    :param test_logger:
    :param extra:
    :return:
    """
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed or request.node.rep_setup.failed:
        if '\\' in r"%r" % request.node.name:
            request.node.name = ''.join(ch for ch in request.node.name if ch != '\\')
        filename = f'{request.node.name}.png'
        if browser.save_screenshot(str(request.config.option.screenshots_dir.joinpath(filename))):
            test_logger.info(f'Screenshot saved: {request.config.option.screenshots_dir.joinpath(filename)}')
            extra.append(pytest_html.extras.png(os.sep.join(('screenshots', filename))))
        else:
            test_logger.warning(f'Screenshot save failed')


@pytest.fixture
def test_logger():
    return get_logger('Test Logger')

