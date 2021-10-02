#from behave import *
from pytest_bdd import given, scenario
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from Locators.basepage import BasePageLocators
from Pages.basepage import BasePage


@scenario("login.feature", "Otwieranie strony logowania")
def test_arguments():
    pass


@given('Przeglądarka jest otworzona')
def step_impl():
    driver = webdriver.Chrome()
    page = BasePage(driver)
    driver.get(page.url)
    WebDriverWait(driver, 5, 0.1).until(visibility_of_element_located((By.XPATH, BasePageLocators.login_button)))
    # the same as driver.implicitly_wait(10) ??
    driver.find_element_by_xpath(BasePageLocators.login_button).click()
    driver.quit()
