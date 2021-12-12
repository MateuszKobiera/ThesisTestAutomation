import pytest
from pytest_bdd import scenario, given, when, then

from frontend.locators.Pages.initialization_locators import InitializationLocators


# @pytest.mark.order(5)
# @scenario("initialization.feature", "Walidacja podczas Inicjacji")
# def test_password_init_validation(factory_reset):
#     pass


@pytest.mark.order(6)
@scenario("initialization.feature", "Poprawna Inicjacja")
def test_password_init(factory_reset):
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
    assert login_page.url == login_page.driver.current_url  # bug - too many urls with redirection to the same page


# @when("Wpisuje niepoprawne dane inicjacji")
# def step_impl(initialization_page):
#     # TODO Check more cases
#     initialization_page.set_passwords('a', 'a')
#     initialization_page.get_element(InitializationLocators.change_password_button).click()
#
#
# @then("Wyświetlono błędy z informacją o wymaganych danych inicjacji hasła")
# def step_impl(initialization_page):
#     # TODO Check more cases
#     assert initialization_page.get_first_password_validation() == 'Password must have at least 10 characters'
#
#
# @then("Nie przekierowano strony inicjacji")
# def step_impl(initialization_page):
#     assert initialization_page.url == initialization_page.driver.current_url
