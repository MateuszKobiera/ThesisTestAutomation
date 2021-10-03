import pytest
from selenium import webdriver

from frontend.Pages.base_page import BasePage


@pytest.fixture
def browser() -> webdriver:
    driver = webdriver.Chrome()
    page = BasePage(driver)
    driver.maximize_window()
    driver.get(page.base_url)
    yield driver
    driver.quit()

