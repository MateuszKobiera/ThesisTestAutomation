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
def step_impl(terms_page):
    assert terms_page.url == terms_page.driver.current_url


@pytest.mark.NoInit
@scenario("login.feature", "Zatwierdzanie Zasad i warunków")
def test_accept_terms_policy():
    pass


@given('Jestem na stronie zasad i warunków')
def step_impl(logowanie, terms_page):
    assert terms_page.url == terms_page.driver.current_url


@when("Przeczytam i potwierdzę zasady i warunki")
def step_impl(terms_page):
    terms_page.scroll_terms_and_policy()
    terms_page.accept_terms_and_policy()
    terms_page.save()
    terms_page.launch_initialization()


@then("Przekierowano na stronę inicjacji")
def step_impl(account_init_page):
    assert account_init_page.url == account_init_page.driver.current_url
