# Created by mateu at 10.10.2021
Feature: My Property tests - set overview data
  # Set overview data for property

  Scenario: Ustawienie poprawnych danych nieruchomości
    Given Jestem na stronie My Property
    When Wpisuje poprawne dane nieruchomości
    Then Dane zostały poprawnie zapisane
    And Zakładka Structure została odblokowana

  Scenario: Nieustawienie danych nieruchomości
    Given Jestem na stronie My Property
    When Nie wpisano danych nieruchomości
    Then Dane nie zostały zapisane
    And Zakładka Structure nie została odblokowana
    And Wyświetlono błędy z informacją o braku danych nieruchomości

  Scenario: Ustawienie niepoprawnych danych nieruchomości
    Given Jestem na stronie My Property
    When Wpisuje niepoprawne dane nieruchomości
    Then Dane nie zostały zapisane
    And Zakładka Structure nie została odblokowana
    And Wyświetlono błędy z informacją o niepoprawnych danych nieruchomości