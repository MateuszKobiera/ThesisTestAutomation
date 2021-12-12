import pytest

from frontend.objects.Pages.account_initalization_page import AccountInitializationPage
from frontend.objects.Pages.menu_page import MenuPage
from frontend.objects.Pages.terms_and_conditions_page import TermsAndConditionsPage
from tests.Initialization_tests.conftest import PASSWORD_VALIDATION


@pytest.mark.order(2)
def test_pierwsze_logowanie_administratora(setup_admin_password, login_page, browser):
    """
    Pierwsze logowanie administratora.
    Druga część inicjacji, gdzie potwierdza się zgody użytkownika i wpisuje dane użytkownika 'Admin'.
    WARUNKI WSTĘPNE:
        - Ustawiono hasło dla użytkownika 'Admin' (zależne od test_inicjacja_zakonczona_sukcesem)
    OPIS KROKU:
        1. Przejdź do aplikacji wpisując adres IP urządzenia brzegowego w pole adresu przeglądarki.
        2. Wpisz poprawne hasło i użytkownika, wybierz narzędzie jako 'Configuration'.
        3. Sprawdź zawartość panelu
        4. Kliknij przycisk 'Decline'
        5. Zaloguj się ponownie. Wpisz poprawne hasło i użytkownika, wybierz narzędzie jako 'Configuration'.
        6. Kliknij na 'ABB Ability Marketplace - Privacy policy'
        7. Wróć do aplikacji. Przesuń na sam dół tekst 'Terms & Conditions' i 'Privacy policy'
        8. Zaznacz pola 'I accept the Terms & Conditions' i 'I accept the Privacy policy'
        9. Kliknij przycisk 'Accept'
        10. Kliknij przycisk 'Save'
        11. Sprawdź czy są dostępne wymagane pola
        12. Wpisz dane w każde z pól
        13. Wpisz poprawne dane dla każdego z pól i kliknij przycisk Save
    OCZEKIWANY REZULTAT:
        1. Panel logowania został wyświetlony.
        2. Przekierowano do panelu zatwierdzania Zasad i warunków, a także polityki prywatności.
        3. Wyświetlone są dwa przewijane teksty: Terms & Conditions i Privacy policy.
        Wyświetlone są dwa pola wyboru i przycisk 'Accept', które nie są dostępne i przycisk 'Decline', \
        który jest dostępny.
        4. Przekierowano na stronę logowania.
        5. Przekierowano do panelu zatwierdzania Zasad i warunków, a także polityki prywatności.
        6. Przekierowano na stronę z polityką prywatności ABB Ability Marketplace
        7. Po przesunięciu tekstu 'Terms & Conditions' na sam koniec pole wyboru 'I accept the Terms & Conditions'
        stało się dostępne. Po przesunięciu tekstu 'Privacy policy' na sam koniec pole wyboru
        'I accept the Privacy policy' stało się dostępne.
        8. Przycisk 'Accept' stał się dostępny
        9. Przekierowano do panelu inicjacji danych użytkownika.
        10. Zapisanie danych nie jest możliwe. Wyświetlono komunikaty z informacją, że należy wypełnić każde z pól.
        11. Pola są dostępne.
        12. Poprawnie wpisano dane dla pól: First name, Last name, Company.
        Dla pozostałych pól wyświetlono komunikaty z informacją na temat walidacji:
        Dla pola Initials można wpisać maksymalnie 3 znaki, Dla pola E-mail wpisano niepoprawne dane,
        Dla pola Phone wpisano niepoprawne dane
        13. Dane zostały poprawnie zapisane. Przekierowano na stronę główną aplikacji,
        gdzie wszystkie pola są wyszarzone oprócz My Property i Edge Device Configuration.
    """
    # Preconditions

    # Step 1
    assert login_page.driver.current_url == login_page.url

    # Step 2
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.choose_mode('Configuration')
    login_page.click_login()
    terms_page = TermsAndConditionsPage(browser)
    terms_page.wait_for_loading_indicator()
    assert terms_page.driver.current_url == terms_page.url

    # Step 3
    assert terms_page.terms_condition_textbox.is_element_visible()
    assert terms_page.privacy_policy_textbox.is_element_visible()
    assert terms_page.terms_condition_checkbox.is_active() is False
    assert terms_page.privacy_policy_checkbox.is_active() is False
    assert terms_page.save_button.is_active() is False
    assert terms_page.cancel_button.is_active()

    # Step 4
    terms_page.cancel_button.click()

    # Step 5
    login_page.set_username('Admin')
    login_page.set_password('Smartspaces1!')
    login_page.choose_mode('Configuration')
    login_page.click_login()
    terms_page.wait_for_loading_indicator()
    assert terms_page.driver.current_url == terms_page.url

    # Step 6
    terms_page.click_download_policy_privacy()  # bug - element is not clickable
    terms_page.driver.switch_to.window(terms_page.driver.window_handles[1])
    assert terms_page.driver.current_url == 'https://library.e.abb.com/public/5bf1010ad6d14991bf347fe5669678fe/GTC%20for%20ABB%20Ability%20Marketplace%20(US).pdf'
    terms_page.driver.switch_to.window(terms_page.driver.window_handles[0])

    # Step 7
    terms_page.scroll_terms_and_policy()
    assert terms_page.terms_condition_checkbox.is_active()
    assert terms_page.privacy_policy_checkbox.is_active()

    # Step 8
    terms_page.accept_terms_and_policy()
    assert terms_page.save_button.is_active()

    # Step 9
    terms_page.save()
    terms_page.launch_initialization()

    # Step 10
    account_init_page = AccountInitializationPage(browser)
    assert account_init_page.driver.current_url == account_init_page.url
    account_init_page.save()
    assert account_init_page.driver.current_url == account_init_page.url
    assert account_init_page.company_input.get_validation() == 'Company is required'
    assert account_init_page.first_name_input.get_validation() == 'First name is required'
    assert account_init_page.last_name_input.get_validation() == 'Last name is required'
    assert account_init_page.email_input.get_validation() == 'Email is required'
    assert account_init_page.phone_input.get_validation() == 'Phone is required'

    # Step 11
    assert account_init_page.company_input.is_active()
    assert account_init_page.role_input.is_active() is False
    assert account_init_page.first_name_input.is_active()
    assert account_init_page.last_name_input.is_active()
    assert account_init_page.email_input.is_active()
    assert account_init_page.phone_input.is_active()

    # Step 12
    account_init_page.set_first_name('Adam')
    account_init_page.set_last_name('Nowak')
    account_init_page.set_company('ABB')
    account_init_page.set_initials('ABCD')
    account_init_page.set_email('ABCD')
    account_init_page.set_phone('ABCD')
    assert account_init_page.last_name_input.get_validation() == 'Initials must be less than 3 characters'
    assert account_init_page.email_input.get_validation() == 'Email is not valid'
    assert account_init_page.phone_input.get_validation() == 'Phone number is not valid'

    # Step 13
    account_init_page.set_initials('AN')
    account_init_page.set_email('adam.nowak12121212@mail.com')
    account_init_page.set_phone('123456789')
    account_init_page.save()
    account_init_page.wait_for_loading_indicator()
    menu_page = MenuPage(browser)
    assert menu_page.driver.current_url == menu_page.url


@pytest.mark.order(3)
def test_pierwsze_logowanie_dla_uzytkownikow_innych_niz_admin(setup_admin_user, setup_building, setup_another_user,
                                                              login_page, login_api, my_property_api, browser):
    """
    Pierwsze logowanie dla użytkowników innych niż 'Admin'
    WARUNKI WSTĘPNE:
        - Admin jest zainicjowany
        - Budynek jest zainicjowany
        - Użytkownik inny niż Admin jest stworzony
    OPIS KROKU:
        1. Przejdź do aplikacji wpisując adres IP urządzenia brzegowego w pole adresu przeglądarki.
        2. Zaloguj się po raz pierwszy jako nowy użytkownik, wybierz narzędzie jako 'Configuration'
        3. Przesuń na sam dół tekst 'Terms & Conditions' i 'Privacy policy'
        4. Zaznacz pola 'I accept the Terms & Conditions' i 'I accept the Privacy policy'
        5. Kliknij przycisk 'Accept'
        6. Kliknij przycisk 'Save'
        7. Sprawdź czy są dostępne wymagane pola
        8. Wpisz dane dla każdego z pól i kliknij przycisk Save
        9. Wpisz dane dla każdego z pól i kliknij przycisk Save
        10. Wpisz dane dla każdego z pól i kliknij przycisk Save
        11. Wpisz poprawne dane dla każdego z pól i kliknij przycisk Save
    OCZEKIWANY REZULTAT:
        1. Panel logowania został wyświetlony.
        2. Przekierowano do panelu zatwierdzania Zasad i warunków, a także polityki prywatności.
        3. Po przesunięciu tekstu 'Terms & Conditions' na sam koniec pole wyboru
        'I accept the Terms & Conditions' stało się dostępne. Po przesunięciu tekstu 'Privacy policy' na sam koniec
        pole wyboru 'I accept the Privacy policy' stało się dostępne.
        4. Przycisk 'Accept' stał się dostępny
        5. Przekierowano do panelu inicjacji danych użytkownika.
        6. Zapisanie danych nie jest możliwe. Wyświetlono komunikaty z informacją, że należy wypełnić każde z pól.
        7. Pola są dostępne.
        8. Możemy wprowadzić dane wejściowe. Zapisanie danych się nie powiodło.
        Wyświetla się podpowiedź walidacji przy wprowadzaniu hasła
        9. Możemy wprowadzić dane wejściowe. Zapisanie danych się nie powiodło.
        Wyświetla się podpowiedź walidacji przy wprowadzaniu hasła informująca, że:Hasło musi być inne od obecnego hasła
        10. Możemy wprowadzić dane wejściowe. Zapisanie danych się nie powiodło.
        Wyświetla się podpowiedź walidacji przy wprowadzaniu hasła informująca, że:
        Pole Confirm new password różni się od hasła wpisanego w pole 'Enter new password'
        11. Dane zostały poprawnie zapisane. Przekierowano na stronę główną aplikacji, gdzie wszystkie pola są dostępne.
    """
    # Preconditions done as fixtures

    # Step 1
    assert login_page.driver.current_url == login_page.url

    # Step 2
    login_page.set_username('User')
    login_page.set_password('Smartspaces2!')
    login_page.choose_mode('Configuration')
    login_page.click_login()
    terms_page = TermsAndConditionsPage(browser)
    terms_page.wait_for_loading_indicator()
    assert terms_page.driver.current_url == terms_page.url  # bug - for user there are not displayed terms and acc data

    # Step 3
    terms_page.scroll_terms_and_policy()
    assert terms_page.terms_condition_checkbox.is_active()
    assert terms_page.privacy_policy_checkbox.is_active()

    # Step 4
    terms_page.accept_terms_and_policy()
    assert terms_page.save_button.is_active()

    # Step 5
    terms_page.save()
    terms_page.launch_initialization()

    # Step 6
    account_init_page = AccountInitializationPage(browser)
    assert account_init_page.driver.current_url == account_init_page.url
    account_init_page.save()
    assert account_init_page.driver.current_url == account_init_page.url
    assert account_init_page.company_input.get_validation() == 'Company is required'
    assert account_init_page.first_name_input.get_validation() == 'First name is required'
    assert account_init_page.last_name_input.get_validation() == 'Last name is required'
    assert account_init_page.email_input.get_validation() == 'Email is required'
    assert account_init_page.phone_input.get_validation() == 'Phone is required'

    # Step 7
    assert account_init_page.company_input.is_active()
    assert account_init_page.role_input.is_active() is False
    assert account_init_page.first_name_input.is_active()
    assert account_init_page.last_name_input.is_active()
    assert account_init_page.email_input.is_active()
    assert account_init_page.phone_input.is_active()
    assert account_init_page.password_input.is_active()
    assert account_init_page.password_confirmation_input.is_active()

    # Step 8
    account_init_page.set_first_name('Filip')
    account_init_page.set_last_name('Kowalski')
    account_init_page.set_company('ABB')
    account_init_page.set_initials('FK')
    account_init_page.set_email('filip.kowalski121212@mail.com')
    account_init_page.set_phone('987654321')
    for password in PASSWORD_VALIDATION:
        account_init_page.password_input.set_value(password)
        account_init_page.password_confirmation_input.set_value(password)
        assert account_init_page.password_input.get_validation() == PASSWORD_VALIDATION[password]

    # Step 9
    account_init_page.password_input.set_value('Smartspaces2!')
    account_init_page.password_confirmation_input.set_value('Smartspaces2!')
    assert account_init_page.password_input.get_validation() == 'Password must be different from actual password.'

    # Step 10
    account_init_page.password_input.set_value('Smartspaces3!')
    account_init_page.password_confirmation_input.set_value('Smartspaces4!')
    assert account_init_page.password_confirmation_input.get_validation() == 'Passwords must be the same.'

    # Step 11
    account_init_page.password_input.set_value('Smartspaces3!')
    account_init_page.password_confirmation_input.set_value('Smartspaces3!')
    account_init_page.save()
    account_init_page.wait_for_loading_indicator()
    menu_page = MenuPage(browser)
    assert menu_page.driver.current_url == menu_page.url

