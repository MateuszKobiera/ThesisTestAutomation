import pytest
from pytest_bdd import given, scenario, when, then, scenarios

from backend.mocked_data.user import another_user, admin_account_init
from frontend.locators.Pages.menu_locators import MenuLocators

CONVERTERS = {
    'login': str,
    'haslo': str,
    'blad_nazwy_uzytkownika': str,
    'blad_hasla': str,
    'blad_ogolny': str,
}
CONVERTERS2 = {
    'haslo': str,
    'potwierdzenie_hasla': str,
    'blad_hasla': str,
    'blad_potwierdzenia_hasla': str,
}


@pytest.mark.order(7)
@scenario("login.feature", "Wyświetlanie błędów podczas logowania", example_converters=CONVERTERS)
def test_login_validation():
    pass


@pytest.mark.order(8)
@scenario("login.feature", "Logowanie się bez zainicjowanego użytkownika")
def test_login_user_no_initialized():
    pass


@pytest.mark.order(9)
@scenario("login.feature", "Zatwierdzanie Zasad i warunków")
def test_accept_terms_policy():
    pass


@pytest.mark.order(10)
@scenario("login.feature", "Wyświetlanie błędów podczas inicjacji bez danych")
def test_account_init_validation_no_data():
    pass


@pytest.mark.order(11)
@scenario("login.feature", "Inicjacja Admina po logowaniu")
def test_account_init():
    pass


@pytest.mark.order(12)
@scenario("login.feature", "Otwieranie strony logowania z zainicjowanym użytkownikiem")
def test_login_with_init():
    """Struktura wywołania testu"""
    pass


@pytest.mark.order(13)
@scenario("login.feature", "Wyświetlanie błędów podczas inicjacji konta innego niż Admin", example_converters=CONVERTERS2)
def test_account_user_init():
    pass

# scenarios('login.feature')


@given("Jestem na stronie logowania")
def open_browser(login_page) -> None:
    """
    Otwieranie strony logowania i sprawdzenie jej url
    :param login_page: struktura obsługująca przeglądarkę i otwierająca stronę logowania
    :return: nic nie zwraca
    """
    assert login_page.url == login_page.driver.current_url


@when('Wpisuje poprawne dane logowania')
def logowanie(login_page):
    """
    Wpisanie danych i zatwierdzenie logowania
    :param login_page: struktura obsługująca przeglądarkę i otwierająca stronę logowania
    :return: nic nie zwraca
    """
    login_page.choose_mode('Configuration')
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.click_login()
    login_page.wait_for_loading_indicator()


@then('Przekierowano na stronę zasad i warunków')
def step_impl(terms_page):
    """
    Sprawdzenie poprawności przekierowania przez url
    :param terms_page: struktura obsługująca przeglądarkę na stronie zasad i warunków
    :return: nic nie zwraca
    """
    assert terms_page.url == terms_page.driver.current_url


@given('Jestem na stronie zasad i warunków')
def step_impl(log_in, terms_page):
    terms_page.wait_for_loading_indicator()
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
@then("Przekierowano na stronę inicjacji danych")
# Terms and conditions should be accepted already
def step_impl(log_in, account_init_page):
    assert account_init_page.url == account_init_page.driver.current_url


@given('Jestem na stronie inicjacji danych jako User')
# Terms and conditions should be accepted already
def step_impl(log_in_as_user, setup_another_user, account_init_page):
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
def assert_main_page_url(menu_page):
    """
    Sprawdzenie poprawności przekierowania przez url
    :param menu_page: struktura obsługująca przeglądarkę na stronie głównej
    :return: nic nie zwraca
    """
    assert menu_page.url == menu_page.driver.current_url


@then('Kafelki są wyszarzone oprócz My Property i Edge Device Configuration')
def step_impl(menu_page):
    menu_page.check_enabled_widgets((MenuLocators.my_property_widget, MenuLocators.edge_device_configuration_widget))


@given('Użytkownik Admin jest zainicjowany')
def admin_initialized(login_page, login_api):
    """
    Sprawdzenie czy użytkownik 'Admin' jest zainicjowany
    :param login_page: struktura obsługująca przeglądarkę na stronie logowania
    :param login_api: struktura obsługująca API dla strony logowania
    :return: nic nie zwraca
    """
    if login_api.get_init_done() is False:
        login_api.put_initialize_account_data('Admin', admin_account_init())


@when("Nie wpisuje danych konta")
def step_impl(account_init_page):
    account_init_page.save()


@then("Wyświetlono błędy z informacją o wymaganych danych logowania")
def step_impl(account_init_page):
    assert account_init_page.company_input.get_validation() == 'Required'
    assert account_init_page.first_name_input.get_validation() == 'Required'
    assert account_init_page.last_name_input.get_validation() == 'Required'
    assert account_init_page.email_input.get_validation() == 'Required'
    assert account_init_page.phone_input.get_validation() == 'Required'


@given('"Admin" ma ustawione tylko hasło')
def step_impl(login_api):
    assert login_api.get_initialization_status() == 'PasswordSet'


@given("Zasady i warunki zostały potwierdzone")
def step_impl(login_api):
    assert login_api.get_initialization_status() == 'CoreInitializationDone'

# @then("Przekierowano na stronę inicjacji danych")
# def step_impl():
#     raise NotImplementedError(u'STEP: Then Przekierowano na stronę inicjacji danych')


@when('Wpisuje niepoprawne dane logowania "<login>" i "<haslo>"')
def step_impl(login_page, login, haslo):
    login_page.set_username(login)
    login_page.set_password(haslo)
    login_page.click_login()


@then('Wyświetlono "<blad_nazwy_uzytkownika>" i "<blad_hasla>" i "<blad_ogolny>" podczas logowania')
def step_impl(login_page, blad_nazwy_uzytkownika, blad_hasla, blad_ogolny):
    if blad_nazwy_uzytkownika != '':
        assert login_page.get_username_validation() == blad_nazwy_uzytkownika
    if blad_hasla != '':
        assert login_page.get_password_validation() == blad_hasla
    if blad_ogolny != '':
        assert login_page.get_general_validation() == blad_ogolny


@then("Przekierowano na stronę logowania")
def step_impl(login_page):
    assert login_page.url == login_page.driver.current_url


@given("Użytkownik User jest stworzony, nie zainicjowany")
def step_impl(login_page, login_api):
    assert login_page.url == login_page.driver.current_url


@when('Wpisuje niepoprawne dane inicjacji "<haslo>", "<potwierdzenie_hasla>"')
def step_impl(account_init_page, haslo, potwierdzenie_hasla):
    assert account_init_page.password_input.set_value(haslo)  # bug - not implemented inputs
    assert account_init_page.password_confirmation_input.set_value(potwierdzenie_hasla)


@given('Wyświetlono "<blad_hasla>" i "<blad_potwierdzenia_hasla>" podczas inicjacji')
def step_impl(account_init_page, blad_hasla, blad_potwierdzenia_hasla):
    assert account_init_page.password_input.get_validation() == blad_hasla  # bug - not implemented inputs
    assert account_init_page.password_confirmation_input.get_validation() == blad_potwierdzenia_hasla
