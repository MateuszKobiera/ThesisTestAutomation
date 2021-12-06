# Created by mateu at 06.12.2021
Feature: Sprawdza dodanie i edycję wszystkich standardowych datapointów i properties

  Scenario: Dodanie wszystkich datapointów
    Given Jestem na stronie Asset templates
    And Dodano Asset template
    And Jestem w trybie edycji Asset template'u
    When Kliknę przycisk 'Add datapoint'
    And Wypełnie wymagane dane
    And Kliknę przycisk Save
    Then Dodano nowy datapoint
    # Należy powtórzyć dla każdego typu standardowego datapointu

  Scenario: Edycja wszystkich datapointów
    Given Jestem na stronie Asset templates
    And Dodano Asset template
    And Jestem w trybie edycji Asset template'u
    When Kliknę na przycisk edycji datapointu
    And Dokonam edycji danych dla datapointu
    And Kliknę przycisk Save
    Then Nowe dane dla datapointu zostały zapisane
    # Należy powtórzyć dla każdego typu standardowego datapointu

  Scenario: Dodanie wszystkich properties
    Given Jestem na stronie Asset templates
    And Dodano Asset template
    And Jestem w trybie edycji Asset template'u
    When Kliknę przycisk 'Add property'
    And Wypełnie wymagane dane
    And Kliknę przycisk Save
    Then Dodano nowy property
    # Należy powtórzyć dla każdego typu standardowego property

  Scenario: Edycja wszystkich properties
    Given Jestem na stronie Asset templates
    And Dodano Asset template
    And Jestem w trybie edycji Asset template'u
    When Kliknę na przycisk edycji property
    And Dokonam edycji danych dla property
    And Kliknę przycisk Save
    Then Nowe dane dla property zostały zapisane