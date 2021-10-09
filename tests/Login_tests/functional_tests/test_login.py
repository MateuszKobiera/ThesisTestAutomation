import pytest
from pytest_bdd import given, scenario, when, then


@pytest.mark.NoInit
@scenario("login.feature", "Logowanie się bez zainicjowanego użytkownika")
def test_impl():
    pass


@given("Jestem na stronie logowania")
def open_browser(login_page):
    assert login_page.url == login_page.driver.current_url


@when('Wpisuje poprawne dane logowania')
def logowanie(login_page):
    login_page.choose_mode('Configuration')
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.login()


@then('Przekierowano na stronę zasad i warunków')
def logowanie(login_page):
    assert login_page.terms_url == login_page.driver.current_url
