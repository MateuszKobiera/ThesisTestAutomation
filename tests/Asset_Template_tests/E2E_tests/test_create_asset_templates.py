from frontend.objects.Pages.asset_templates_page import AssetTemplatesPage


def test_create_asset_template(asset_templates_page):
    """
    WARUNKI WSTĘPNE:
        - Użytkownik Admin jest zalogowany
        - Budynek jest dodany
    OPIS KROKU:
        1. Przejdź do widżetu 'Asset templates'
        2. Dla zakładki 'Sensors' dla tabeli 'Sensors' kliknij przycisk 'Add template'
        3. Uzupełnij nazwę, typ, tag i ikonę wraz z tłem dla Assetu
        4. Kliknij przycisk 'Save'
        5. Kliknij na ikonkę edycji przy nowo powstałym Assecie
        6. Ustaw 'Master/Slave support in a space' i kliknij ikonkę 'Save'
        7. Przejdź do zakładki 'Points' i kliknij 'Add datapoint'
        8. Wybierz opcję 'Custom' i dodaj nazwę, typ, format, jednostkę, wartość minimalną, maksymalną,
            jednostkę wyświetlaną i tag
        9. Kliknij przycisk 'Save'
        10. Powtórz kroki 7-9 dla kolejnych typów datapointów
        11. Powtórz kroki 7-9 dla properties z zakładki 'Properties'
    OCZEKIWANY REZULTAT:
        1. Strona 'Asset templates' została wyświetlona
        2. Okno dialogowe dla dodania assetu zostało wyświetlone
        3. Wszystkie dane zostały poprawnie wprowadzone
        4. Nowy Asset template został wyświetlony w tabeli 'Sensors' z danymi dodanymi w oknie dialogowym
        5. W zakładce 'General' pojwiły się dane asset template'u z możliwością ich edycji (oprócz Quntity of instances)
        6. Dane zostały zapisane
        7. Okno dialogowe dla dodania Datapointów
        8. Dane zostały poprawnie ustawione
        9. Okno dialogowe zostało zamknięte a datapoint jest widoczny a zakładce 'Points' z nazwą i typem,
            możliwością edycji i usunięcia
        10. Datapointy zostały dodane i są wyświetlane w zakładce 'Points'
        11. Properties zostały dodane i są wyświetlane w zakładce 'Properties' z możliwością edycji i ich usunięcia
            z nazwą i wartością początkową
    """
