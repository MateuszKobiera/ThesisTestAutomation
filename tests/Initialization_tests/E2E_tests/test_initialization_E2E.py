import pytest

from tests.Initialization_tests.conftest import PASSWORD_VALIDATION


@pytest.mark.order(1)
def test_inicjacja_zakonczona_sukcesem(initialization_page):
    """
    Testuje walidacje i dane strony inicjacji
    WARUNKI WSTĘPNE:
        - Użytkownik nie jest zainicjowany
    OPIS KROKU:
        1. Otwórz przeglądarkę internetową w aplikacji.
        2. Sprawdź, czy jest tytuł 'Building Ecosystem'
        3. Sprawdź, czy są 2 pola do wprowadzenia danych dla użytkownika „Admin”.
        4. Kliknij przycisk 'Change password'
        5. Wpisz hasło do pierwszego pola do wprowadzenia danych
        6. W przypadku pierwszego hasła należy wprowadzić poprawne dane. Dla drugiego wejścia uzupełnij poprawne dane,
            ale inne niż dla pierwszego wejścia.
        7. Wypełnij oba wejścia poprawnym hasłem i kliknij przycisk 'Confirm password'
    OCZEKIWANY REZULTAT:
        1. Pojawiła się strona inicjacji.
        2. Tytuł jest widoczny.
        3. Istnieje jedno pole do wprowadzenia danych dla użytkownika „Admin”.
            Istnieje drugie pole do potwierdzenia hasła dla użytkownika „Admin”.
        4. Nie możemy zapisać hasła administratora z pustymi danymi wejściowymi.
        Pokazała się wskazówka sprawdzania poprawności informująca, że wymagane są hasła dla obu pól.
        5. Możemy wprowadzić dane wejściowe. Wyświetla się podpowiedź walidacji przy wprowadzaniu haseł
        6. Wyświetlił się komunikat walidacji sprawdzania poprawności, który informuje, że hasła nie są zgodne.
        7. Hasło zostało zapisane. Przekierowano na stronę logowania.
    """
    # step 1
    assert initialization_page.driver.current_url == initialization_page.url

    # step 2
    assert initialization_page.get_title() == initialization_page.title

    # step 3
    assert initialization_page.password_input.is_element_visible()
    assert initialization_page.password_input.get_label() == 'Enter password of the “Admin” account'
    assert initialization_page.password_confirmation_input.is_element_visible()
    assert initialization_page.password_confirmation_input.get_label() == 'Confirm password of the “Admin” account'

    # step 4
    for password in PASSWORD_VALIDATION:
        initialization_page.set_passwords(password, password)
        assert initialization_page.password_input.get_validation() == PASSWORD_VALIDATION[password]

