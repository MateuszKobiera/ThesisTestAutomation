from random import randint

from utils.string_editor import create_random_string


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
    # step 1
    asset_templates_page.open_tab('Sensors')

    # step 2
    add_template_modal = asset_templates_page.click_add_button('Sensors')

    # step 3
    template_name = f'{create_random_string(5)} {create_random_string(5)}'
    template_type = 'UV Sensor'
    add_template_modal.set_template_name(template_name)
    add_template_modal.set_template_type(template_type)
    add_template_modal.tags.set_new_tag('ABC')
    all_tags = add_template_modal.tags.get_tags()
    add_template_modal.icons.set_icon(randint(1, 826))
    color_set = (randint(0, 255), randint(0, 255), randint(0, 255))
    add_template_modal.icons.set_background(color_type='rgb', color=color_set)
    background_color = add_template_modal.icons.get_background_color()
    assert color_set == background_color

    # step 4
    add_template_modal.save()
    template_table = asset_templates_page.template_table(table_name='Sensors').get_table(unique_column_name='TEMPLATE NAME')
    assert template_table[template_name]['TEMPLATE NAME'] == template_name
    assert template_table[template_name]['TYPE'] == template_type
    assert template_table[template_name]['INSTANCES'] == '0'

    # step 5
    asset_templates_page.template_table('Sensors').edit_row(unique_column_name='TEMPLATE NAME', row_name=template_name)

    # step 6
    asset_templates_page.set_master_slave()
    asset_templates_page.save()
    assert asset_templates_page.template_tags.get_tags() == all_tags

    # step 7 & 8 & 9 & 10
    asset_templates_page.open_tab('Points')
    data: dict = {}
    for point_format in ['Float', 'Integer', 'Boolean', 'Enum']:
        data[point_format] = {'format': point_format, 'name': f'{point_format}',
                              'type': 'Command And Feedback', 'tag': f'{create_random_string(5)}'}
        datapoint_modal = asset_templates_page.click_add_datapoint()
        # noinspection DuplicatedCode
        datapoint_modal.click_custom_datapoint()
        datapoint_modal.set_name(data[point_format]['name'])
        datapoint_modal.set_type(data[point_format]['type'])
        datapoint_modal.set_format(data[point_format]['format'])
        if point_format == 'Integer' or point_format == 'Float':
            data[point_format]['unit'] = 'Degrees - deg'
            data[point_format]['display_unit'] = 'Radians - rad'
            data[point_format]['min_value'] = 0
            data[point_format]['max_value'] = 100000
            datapoint_modal.set_unit(data[point_format]['unit'])
            datapoint_modal.set_min_value(data[point_format]['min_value'])
            datapoint_modal.set_max_value(data[point_format]['max_value'])
            datapoint_modal.set_display_unit(data[point_format]['display_unit'])
        datapoint_modal.tags.set_new_tag(data[point_format]['tag'])
        datapoint_modal.save()

    datapoints_table = asset_templates_page.points_properties_table.get_table(unique_column_name='POINT')
    for point_format in ['Float', 'Integer', 'Boolean', 'Enum']:
        assert datapoints_table[point_format]['POINT'] == data[point_format]['format']
        assert datapoints_table[point_format]['DIRECTION'] == data[point_format]['type']

    # step 7 & 8 & 9 & 11
    asset_templates_page.open_tab('properties')
    properties_data: dict = {}
    for point_format in ['String', 'Float', 'Integer', 'Boolean', 'Enum']:
        properties_data[point_format] = {'format': point_format, 'name': f'{point_format}',
                                         'type': 'Command And Feedback', 'tag': f'{create_random_string(5)}'}
        datapoint_modal = asset_templates_page.click_add_property()
        # noinspection DuplicatedCode
        datapoint_modal.click_custom_datapoint()
        datapoint_modal.set_name(properties_data[point_format]['name'])
        datapoint_modal.set_type(properties_data[point_format]['type'])
        datapoint_modal.set_format(properties_data[point_format]['format'])
        if point_format == 'Integer' or point_format == 'Float':
            properties_data[point_format]['unit'] = 'Degrees - deg'
            properties_data[point_format]['display_unit'] = 'Radians - rad'
            properties_data[point_format]['min_value'] = 0
            properties_data[point_format]['max_value'] = 100000
            datapoint_modal.set_unit(properties_data[point_format]['unit'])
            datapoint_modal.set_min_value(properties_data[point_format]['min_value'])
            datapoint_modal.set_max_value(properties_data[point_format]['max_value'])
            datapoint_modal.set_display_unit(properties_data[point_format]['display_unit'])
        datapoint_modal.tags.set_new_tag(properties_data[point_format]['tag'])
        datapoint_modal.save()

    properties_table = asset_templates_page.points_properties_table.get_table(unique_column_name='PROPERTY')
    for point_format in ['String', 'Float', 'Integer', 'Boolean', 'Enum']:
        assert properties_table[point_format]['PROPERTY'] == properties_data[point_format]['format']
        assert properties_table[point_format]['VALUE'] == properties_data[point_format]['type']
