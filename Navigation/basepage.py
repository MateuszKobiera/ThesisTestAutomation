import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.basepage import BasePage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
    # page = BasePage(driver)
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.page = BasePage(self.driver)


def get_element(element_locator):
    return NavBasePage.driver.find_element(By.XPATH, element_locator)


@pytest.fixture
def open_browser():
    return NavBasePage.driver.get(NavBasePage.page.url)


