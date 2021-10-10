import pytest
from pytest_bdd import scenario, given, when, then


@pytest.mark.NoInit
@scenario("initialization.feature", "Poprawna Inicjacja")
def test_password_init():
    pass


@given("Jestem na stronie inicjacji")
def step_impl(initialization_page):
    assert initialization_page.url == initialization_page.driver.current_url


@when("Wpisuje poprawne dane inicjacji hasła")
def step_impl(initialization_page):
    initialization_page.set_passwords('Smartspaces1!', 'Smartspaces1!')
    initialization_page.change_password()


@then("Przekierowano na stronę logowania")
def step_impl(login_page):
    assert login_page.url == login_page.driver.current_url
