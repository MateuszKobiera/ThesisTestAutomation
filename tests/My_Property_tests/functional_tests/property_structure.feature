# Created by mateu at 10.10.2021
Feature: My Property - structure tab
  # Set structure of buildings and floors

  Scenario: Wyświetlanie okna dialogowego dla budynku
    Given Jestem na stronie My property - Structure
    And Nie dodano budynku
    When Kliknę w przycisk "Add structure"
    Then Wyświetlono okno dialogowe dla dodania budynku

  Scenario: Dodanie pierwszego budynku
    Given Jestem na stronie My property - Structure
    And Nie dodano budynku
    And Wyświetlono okno dialogowe dla dodania budynku
    When Uzupełniam poprawne dane dla budynku
    Then Dodano nowy budynek

  Scenario: Dodanie piętra dla budynku
    Given Jestem na stronie My property - Structure
    And Dodano budynek
    And Wyświetlono okno dialogowe dla dodania budynku
    When Uzupełniam poprawne dane dla piętra
    Then Dodano piętro do budynku

  Scenario: Anulowanie dodawania struktury
    Given Jestem na stronie My property - Structure
    And Wyświetlono okno dialogowe dla dodania budynku
    When Klikam przycisk Cancel
    Then Zamknięto okno dialogowe bez dodania struktury