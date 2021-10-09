# Created by mateu at 09.10.2021
Feature: Inicjacja Admina
  # Enter feature description here

  Scenario: Poprawna Inicjacja
    Given Jestem na stronie inicjacji
    When Wpisuje poprawne dane inicjacji hasła
    Then Przekierowano na stronę logowania

  Scenario: Walidacja podczas Inicjacji
    Given Jestem na stronie inicjacji
    When Wpisuje niepoprawne dane inicjacji
    Then Jestem na stronie inicjacji
    And Wyświetlono błędy z informacją o wymaganych danych
