import pytest
from pytest_bdd import given, scenario, when, then

from frontend.Locators.menu_locators import MenuLocators


# @pytest.mark.NoInit
# @scenario("login.feature", "Wyświetlanie błędów podczas inicjacji bez danych")
# def test_login_no_data():
#     pass


@pytest.mark.NoInit
@scenario("login.feature", "Logowanie się bez zainicjowanego użytkownika")
def test_login_user_no_initialized():
    pass


@scenario("login.feature", "Otwieranie strony logowania z zainicjowanym użytkownikiem")
def test_login_with_init():
    pass


@pytest.mark.NoInit
@scenario("login.feature", "Zatwierdzanie Zasad i warunków")
def test_accept_terms_policy():
    pass


@pytest.mark.NoInit
@scenario("login.feature", "Inicjacja Admina po logowaniu")
def test_account_init():
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


@given('Jestem na stronie zasad i warunków')
def step_impl(log_in, terms_page):
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


@given('Jestem na stronie inicjacji danych')
# Terms and conditions should be accepted already
def step_impl(log_in, account_init_page):
    assert account_init_page.url == account_init_page.driver.current_url


@when("Wpisuje poprawne dane inicjacji")
def step_impl(account_init_page):
    account_init_page.set_company('ABB')
    account_init_page.set_first_name('John')
    account_init_page.set_last_name('Smith')
    account_init_page.set_initials('JS')
    account_init_page.set_email('john.smith@abc.asd')
    account_init_page.set_phone('123123123')
    account_init_page.save()  # bug? different modal


@then("Przekierowano na stronę główną")
def step_impl(menu_page):
    assert menu_page.url == menu_page.driver.current_url


@then('Kafelki są wyszarzone oprócz My Property i Edge Device Configuration')
def step_impl(menu_page):
    menu_page.check_enabled_widgets((MenuLocators.my_property_widget, MenuLocators.edge_device_configuration_widget))


@given('Użytkownik jest zainicjowany')
def step_impl(login_page, login_api):
    assert login_api.get_init_done()


# @when("Nie wpisuje danych")
# def step_impl(login_page):
#     login_page.login()


# @given("Wyświetlono błędy z informacją o wymaganych danych logowania")
# def step_impl(login_page):
#     assert login_page.get_username_validation() == 'Username is required'  # bug Username is not displayed
#     assert login_page.get_password_validation() == 'Password is required'

@given('"Admin" ma ustawione tylko hasło')
def step_impl(login_api):
    assert login_api.get_initialization_status() == 'PasswordSet'


@given("Zasady i warunki zostały potwierdzone")
def step_impl(login_api):
    assert login_api.get_initialization_status() == 'CoreInitializationDone'
