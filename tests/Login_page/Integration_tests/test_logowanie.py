from pytest_bdd import given, scenario, when, then

from frontend.Locators.login_page import LoginPageLocators
from frontend.czekanie import wait_for_element


@scenario("logowanie.feature", "Logowanie się bez zainicjowanego użytkownika")
def test_argumenty():
    pass


@given("Jestem na stronie logowania")
def otworz_przegladarke(browser):
    wait_for_element(browser, LoginPageLocators.login_button)
    assert browser.current_url == 'http://localhost:3000/#/auth'
    # browser.find_element_by_xpath(LoginPageLocators.login_button).click()


@when('Wpisuje poprawne dane logowania')
def logowanie():
    pass


@then('Przekierowano na stronę zasad i warunków')
def logowanie():
    pass
