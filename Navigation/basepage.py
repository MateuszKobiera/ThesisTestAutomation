import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import given

from Locators.basepage import BasePageLocators
from Pages.basepage import BasePage


class NavBasePage:
    driver = webdriver.Chrome()
    page = BasePage(driver)
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.page = BasePage(self.driver)


def get_element(element_locator):
    return NavBasePage.driver.find_element(By.XPATH, element_locator)


@pytest.fixture
def open_browser():
    return NavBasePage.driver.get(NavBasePage.page.url)


@given("I opened browser", target_fixture=open_browser)
def click_login():
    return get_element(BasePageLocators.login_button).click()
