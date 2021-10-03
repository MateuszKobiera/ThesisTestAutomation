from pytest_bdd import given, scenario, when, then
from frontend.Locators.login_page import LoginPageLocators
from frontend.Pages.login_page import LoginPage


@scenario("logowanie.feature", "Logowanie się bez zainicjowanego użytkownika")
def test_argumenty():
    pass


@given("Jestem na stronie logowania")
def otworz_przegladarke(login_page: LoginPage):
    login_page.wait_for_element(LoginPageLocators.login_button)
    assert login_page.login_url == 'http://localhost:3000/#/auth'
    # browser.find_element_by_xpath(LoginPageLocators.login_button).click()


@when('Wpisuje poprawne dane logowania')
def logowanie(login_page: LoginPage):
    login_page.get_element(LoginPageLocators.username_input).send_keys('Admin')
    login_page.get_element(LoginPageLocators.password_input).send_keys('Smartspaces1!')
    login_page.get_element(LoginPageLocators.login_button).click()


@then('Przekierowano na stronę zasad i warunków')
def logowanie():
    pass
