from pytest_bdd import given, scenario, when, then
from frontend.Locators.login_page import LoginPageLocators
from frontend.Pages.login_page import LoginPage


@scenario("logowanie.feature", "Logowanie się bez zainicjowanego użytkownika")
def test_argumenty():
    pass


@given("Jestem na stronie logowania")
def open_browser(login_page):
    login_page.wait_for_element(LoginPageLocators.login_button)
    assert login_page.login_url == login_page.driver.current_url
    dropdown = login_page.get_element(LoginPageLocators.tool_dropdown)
    dropdown.choose_option('Operation')
    login_page.get_element(LoginPageLocators.login_button).click()


@when('Wpisuje poprawne dane logowania')
def logowanie(login_page):
    username = login_page.get_element(LoginPageLocators.username_input)
    username.set_input('Admin')
    password = login_page.get_element(LoginPageLocators.password_input)
    password.set_input('Smartspaces1!')
    login_page.get_element(LoginPageLocators.login_button).click()


@then('Przekierowano na stronę zasad i warunków')
def logowanie():
    pass
