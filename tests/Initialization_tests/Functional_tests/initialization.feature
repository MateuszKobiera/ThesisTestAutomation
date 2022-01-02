# Created by mateu at 09.10.2021
Feature: Inicjacja Admina
  # Sprawdzenia procesu inicjacji hasła dla użytkownika początkowego - Admin

  Scenario: Poprawna Inicjacja
    Given Jestem na stronie inicjacji
    When Wpisuje poprawne dane inicjacji hasła
    Then Przekierowano na stronę logowania

#  Scenario: Walidacja podczas Inicjacji
#    Given Jestem na stronie inicjacji
#    When Wpisuje niepoprawne dane inicjacji
#    Then Nie przekierowano strony inicjacji
#    And Wyświetlono błędy z informacją o wymaganych danych inicjacji hasła
