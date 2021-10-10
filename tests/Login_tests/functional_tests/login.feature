Feature: Test login page
  Jako użytkownik chcę zarejestrować i zalogować się do aplikacji

  @pierwszy @nieZainicjowany
  Scenario: Logowanie się bez zainicjowanego użytkownika
    Given Jestem na stronie logowania
    # And Użytkownik nie jest zainicjowany
    When Wpisuje poprawne dane logowania
    Then Przekierowano na stronę zasad i warunków


  Scenario: Zatwierdzanie Zasad i warunków
    Given Jestem na stronie zasad i warunków
    When Przeczytam i potwierdzę zasady i warunki
    Then Przekierowano na stronę inicjacji


  Scenario: Wyświetlanie błędów podczas inicjacji bez danych
    Given Jestem na stronie inicjacji
    When Nie wpisuje danych
    Then Przekierowano na stronę inicjacji
    And Wyświetlono błędy z informacją o wymaganych danych


  Scenario: Inicjacja użytkownika po logowaniu
    Given Jestem na stronie inicjacji danych
    When Wpisuje poprawne dane inicjacji
    Then Przekierowano na stronę główną
    And Kafelki są wyszarzone oprócz My Property i Edge Device Configuration


  Scenario: Otwieranie strony logowania z zainicjowanym użytkownikiem
    Given Jestem na stronie logowania
    # And Użytkownik jest zainicjowany
    When Wpisuje poprawne dane logowania
    Then Przekierowano na stronę główną

 @AutomationOnly @ManualE2E
  Scenario Outline: Wyświetlanie błędów podczas logowania
    Given Jestem na stronie logowania
    When Wpisuje niepoprawne dane logowania "<login>" i "<haslo>"
    Then Przekierowano na stronę logowania
    And Wyświetlono "<blad_nazwy_uzytkownika>" i "<blad_hasla>" i "<blad_ogolny>" podczas logowania

    Examples: Login i hasło
      | login | haslo         | blad_nazwy_uzytkownika | blad_hasla                                           | blad_ogolny       |
      |       |               | Username is required   | Password is required                                 |                   |
      | Admin | a             |                        | Password must have at least 10 characters            |                   |
      | Admin | abcdefghij    |                        | Password must have at least one upper case letter    |                   |
      | Admin | ABCDEFGHIJ    |                        | Password must have at least one lower case letter    |                   |
      | Admin | Abcdefghij    |                        | Password must have at least one digit                |                   |
      | Admin | Abcdefghij1   |                        | Password must have at least one special character    |                   |
      | Admin | Abcdefghij1ą  |                        | Password must only contain alphanumerical characters |                   |
      | AA    | Smartspaces1! |                        |                                                      |Invalid credentials|

  @AutomationOnly @ManualE2E
  Scenario Outline: Wyświetlanie błędów podczas inicjacji
    Given Jestem na stronie inicjacji
    And Użytkownik Admin jest zainicjowany, użytkownik User1 jest stworzony, nie zainicjowany
    When Wpisuje niepoprawne dane inicjacji "<haslo>", "<potwierdzenie_hasla>"
    Then Przekierowano na stronę inicjacji
    And Wyświetlono "<blad_hasla>" i "<blad_potwierdzenia_hasla>" podczas inicjacji

    Examples: Hasło i potwierdzenia hasła
      | haslo         | potwierdzenie_hasla | blad_hasla                                           | blad_potwierdzenia_hasla                             |
      | a             | a                   | Password must have at least 10 characters            | Password must have at least 10 characters            |
      | abcdefghij    | abcdefghij          | Password must have at least one upper case letter    | Password must have at least one upper case letter    |
      | ABCDEFGHIJ    | ABCDEFGHIJ          | Password must have at least one lower case letter    | Password must have at least one lower case letter    |
      | Abcdefghij    | Abcdefghij          | Password must have at least one digit                | Password must have at least one digit                |
      | Abcdefghij1   | Abcdefghij1         | Password must have at least one special character    | Password must have at least one special character    |
      | Abcdefghij1ą  | Abcdefghij1ą        | Password must only contain alphanumerical characters | Password must only contain alphanumerical characters |
      | Smartspaces1! | Smartspaces2!       |                                                      | Passwords do not match                               |

