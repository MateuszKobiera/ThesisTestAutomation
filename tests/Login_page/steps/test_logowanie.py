from pytest_bdd import given, scenario

from frontend.Locators.login_page import LoginPageLocators
from frontend.czekanie import wait_for_element


@scenario("logowanie.feature", "Otwieranie strony logowania")
def test_argumenty():
    pass


@given('Przeglądarka jest otworzona')
def otworz_przegladarke(browser):
    wait_for_element(browser, LoginPageLocators.login_button)
    browser.find_element_by_xpath(LoginPageLocators.login_button).click()

