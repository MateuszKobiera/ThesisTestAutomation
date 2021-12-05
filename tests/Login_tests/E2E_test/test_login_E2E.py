import pytest


@pytest.mark.order(2)
def test_pierwsze_logowanie_administratora(login_page, terms_page):
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
    terms_page.wait_for_loading_indicator()
    assert terms_page.driver.current_url == terms_page.url

    # Step 3

    # Step 4

    # Step 5

    # Step 6

    # Step 7

    # Step 8

    # Step 9

    # Step 10

    # Step 11

    # Step 12

    # Step 13


@pytest.mark.order(3)
def test_pierwsze_logowanie_dla_uzytkownikow_innych_niz_admin(setup_admin_user, setup_building, setup_another_user,
                                                              login_page, login_api, my_property_api):
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
    # Preconditions

    # Step 1

    # Step 2

    # Step 3

    # Step 4

    # Step 5

    # Step 6

    # Step 7

    # Step 8

    # Step 9

    # Step 10

    # Step 11
