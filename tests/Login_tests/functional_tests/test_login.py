import pytest
from pytest_bdd import given, scenario, when, then

from frontend.Locators.menu_locators import MenuLocators


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


@pytest.mark.NoInit
@scenario("login.feature", "Inicjacja użytkownika po logowaniu")
def test_account_init():
    pass


@given('Jestem na stronie inicjacji danych')
# Terms and conditions should be accepted already
def step_impl(logowanie, account_init_page):
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
