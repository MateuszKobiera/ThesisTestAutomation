import random

import pytest

from frontend.objects.Modals.add_datapoint_property_modal import AddDatapointPropertyModal
from tests.Asset_Template_tests.conftest import TEMPLATE_FUNCTIONAL_TESTS
from utils.string_editor import create_random_string


@pytest.mark.order(18)
def test_add_datapoints(asset_templates_page):
    """ Test dodający wszystkie standardowe datapointy
    WARUNKI WSTĘPNE:
        - Jestem na stronie Asset templates
        - Dodano Asset template
        - Jestem w trybie edycji Asset template'u"
    OPIS KROKU:
        1. Kliknij przycisk 'Add datapoint'
        2. Wybierz każdy standardowy datapoint, poddaj edycji i zapisz
    OCZEKIWANY REZULTAT:
        1. Okno dialogowe dla dodania datapointu zostało wyświetlone
        2. Dodano wszystkie standardowe datapointy
    """
    # Preconditions
    # assert asset_templates_page.url == asset_templates_page.driver.current_url
    # template_table = asset_templates_page.template_table(table_name='Central').get_table(
    #     unique_column_name='TEMPLATE NAME')
    # assert template_table[TEMPLATE_FUNCTIONAL_TESTS]['TEMPLATE NAME'] == TEMPLATE_FUNCTIONAL_TESTS
    # asset_templates_page.template_table('Central').edit_row(unique_column_name='TEMPLATE NAME',
    #                                                         row_name=TEMPLATE_FUNCTIONAL_TESTS)
    add_template_modal = asset_templates_page.click_add_button('Central')
    template_name = f'{create_random_string(5)} {create_random_string(5)}'
    add_template_modal.set_template_name(template_name)
    add_template_modal.set_template_type('Boiler')
    add_template_modal.save()
    asset_templates_page.template_table('Central').edit_row(unique_column_name='TEMPLATE NAME',
                                                            row_name=template_name)

    # step 1
    asset_templates_page.open_tab('Points')
    datapoint_modal = asset_templates_page.click_add_datapoint()
    datapoint_names_and_categories = datapoint_modal.get_datapoint_names()
    datapoint_modal.close()

    # step 2
    datpoint_names = []
    failing_datapoints = []

    for category in datapoint_names_and_categories:
        for subcategory in datapoint_names_and_categories[category]:
            if len(datapoint_names_and_categories[category][subcategory]) > 0:
                for datapoint in datapoint_names_and_categories[category][subcategory]:
                    asset_templates_page.click_add_datapoint()
                    datapoint_modal.click_choose_datapoint(category=category, subcategory=subcategory, datapoint=datapoint)
                    datapoint_name = f'{category}-{subcategory}-{datapoint}'
                    datapoint_name = datapoint_name[0:30]+create_random_string(2)
                    datpoint_names.append(datapoint_name)
                    datapoint_modal.set_name(datapoint_name)
                    datapoint_modal.set_type(datapoint_modal.datapoint_types[random.randint(0, 3)])
                    datapoint_modal.tags.set_new_tag(create_random_string(5))
                    try:
                        datapoint_modal.save()
                    except:
                        failing_datapoints.append(datapoint_modal.get_name())
                        datapoint_modal.cancel()
            else:
                asset_templates_page.click_add_datapoint()
                datapoint_modal.click_choose_datapoint(category=category, subcategory=subcategory)
                datapoint_name = f'{category}-{subcategory}'
                datapoint_name = datapoint_name[0:30] + create_random_string(2)
                datpoint_names.append(datapoint_name)
                datapoint_modal.set_name(datapoint_name)
                datapoint_modal.set_type(datapoint_modal.datapoint_types[random.randint(0, 3)])
                datapoint_modal.tags.set_new_tag(create_random_string(5))
                try:
                    datapoint_modal.save()
                except:
                    failing_datapoints.append(datapoint_modal.get_name())
                    datapoint_modal.cancel()

    if len(failing_datapoints) != 0:
        raise ValueError(f'Not working datapoints: \n {failing_datapoints}')

    points_table = asset_templates_page.points_properties_table.get_table(unique_column_name='POINT')
    for datapoint_name in datpoint_names:
        assert datapoint_name in points_table.keys()


@pytest.mark.order(19)
def test_edit_datapoints(asset_templates_page):
    """ Test edytujące wszystkie dostępne datapointy
    WARUNKI WSTĘPNE:
        - Jestem na stronie Asset templates
        - Dodano Asset template
        - Jestem w trybie edycji Asset template'u"
    OPIS KROKU:
        1. Przejdź do zakładki 'Points'
        2. Kliknij edycję każdego datapointu, zmień nazwę, typ, dodaj tag i zapisz
    OCZEKIWANY REZULTAT:
        1. Lista datapointów jest wyświetlona
        2. Każdy datapoint został poprawnie poddany edycji i zapisany
    """
    # Preconditions
    assert asset_templates_page.url == asset_templates_page.driver.current_url
    template_table = asset_templates_page.template_table(table_name='Central').get_table(
        unique_column_name='TEMPLATE NAME')
    assert template_table[TEMPLATE_FUNCTIONAL_TESTS]['TEMPLATE NAME'] == TEMPLATE_FUNCTIONAL_TESTS
    asset_templates_page.template_table('Central').edit_row(unique_column_name='TEMPLATE NAME',
                                                            row_name=TEMPLATE_FUNCTIONAL_TESTS)

    # step 1
    asset_templates_page.open_tab('Points')
    points_table = asset_templates_page.points_properties_table.get_table(unique_column_name='POINT')

    # step 2
    datapoint_names = []
    failing_datapoints = []
    for point_id in range(1, len(points_table)):
        asset_templates_page.points_properties_table.edit_row(row_id=point_id)
        edit_point_modal = AddDatapointPropertyModal(asset_templates_page.driver)
        datapoint_name = edit_point_modal.get_name()
        datapoint_name = datapoint_name[0:24] + create_random_string(2) + '_edit'
        datapoint_names.append(datapoint_name)
        edit_point_modal.set_name(datapoint_name)
        edit_point_modal.set_type(edit_point_modal.datapoint_types[random.randint(0, 3)])
        edit_point_modal.tags.set_new_tag('edit')
        try:
            edit_point_modal.save()
        except:
            failing_datapoints.append(edit_point_modal.get_name())
            edit_point_modal.cancel()

    if len(failing_datapoints) != 0:
        raise ValueError(f'Not working datapoints: \n {failing_datapoints}')

    points_table = asset_templates_page.points_properties_table.get_table(unique_column_name='POINT')
    for datapoint_name in datapoint_names:
        assert datapoint_name in points_table.keys()
        

@pytest.mark.order(20)
def test_add_properties(asset_templates_page):
    """ Test do dodania wszystkich standardowych properties
    WARUNKI WSTĘPNE:
        - Jestem na stronie Asset templates
        - Dodano Asset template
        - Jestem w trybie edycji Asset template'u"
    OPIS KROKU:
        1. Kliknij przycisk 'Add property'
        2. Wybierz każdy standardowy datapoint, poddaj edycji i zapisz
    OCZEKIWANY REZULTAT:
        1. Okno dialogowe dla dodania datapointu zostało wyświetlone
        2. Dodano wszystkie standardowe datapointy
    """
    # Preconditions
    # assert asset_templates_page.url == asset_templates_page.driver.current_url
    # template_table = asset_templates_page.template_table(table_name='Central').get_table(
    #     unique_column_name='TEMPLATE NAME')
    # assert template_table[TEMPLATE_FUNCTIONAL_TESTS]['TEMPLATE NAME'] == TEMPLATE_FUNCTIONAL_TESTS
    # asset_templates_page.template_table('Central').edit_row(unique_column_name='TEMPLATE NAME',
    #                                                         row_name=TEMPLATE_FUNCTIONAL_TESTS)
    add_template_modal = asset_templates_page.click_add_button('Central')
    template_name = f'{create_random_string(5)} {create_random_string(5)}'
    add_template_modal.set_template_name(template_name)
    add_template_modal.set_template_type('Boiler')
    add_template_modal.save()
    asset_templates_page.template_table('Central').edit_row(unique_column_name='TEMPLATE NAME',
                                                            row_name=template_name)

    # step 1
    asset_templates_page.open_tab('Properties')
    datapoint_modal = asset_templates_page.click_add_property()
    datapoint_names_and_categories = datapoint_modal.get_datapoint_names()
    datapoint_modal.close()

    # step 2
    datpoint_names = []
    failing_datapoints = []

    for category in datapoint_names_and_categories:
        for subcategory in datapoint_names_and_categories[category]:
            if len(datapoint_names_and_categories[category][subcategory]) > 0:
                for datapoint in datapoint_names_and_categories[category][subcategory]:
                    asset_templates_page.click_add_property()
                    datapoint_modal.click_choose_datapoint(category=category, subcategory=subcategory,
                                                           datapoint=datapoint)
                    datapoint_name = f'{category}-{subcategory}-{datapoint}'
                    datapoint_name = datapoint_name[0:30] + create_random_string(2)
                    datpoint_names.append(datapoint_name)
                    datapoint_modal.set_name(datapoint_name)
                    datapoint_modal.set_type(datapoint_modal.properties_types[random.randint(0, 1)])
                    datapoint_modal.tags.set_new_tag(create_random_string(5))
                    try:
                        datapoint_modal.save()
                    except:
                        failing_datapoints.append(datapoint_modal.get_name())
                        datapoint_modal.cancel()
            else:
                asset_templates_page.click_add_property()
                datapoint_modal.click_choose_datapoint(category=category, subcategory=subcategory)
                datapoint_name = f'{category}-{subcategory}'
                datapoint_name = datapoint_name[0:30] + create_random_string(2)
                datpoint_names.append(datapoint_name)
                datapoint_modal.set_name(datapoint_name)
                datapoint_modal.set_type(datapoint_modal.properties_types[random.randint(0, 1)])
                datapoint_modal.tags.set_new_tag(create_random_string(5))
                #TODO add value
                try:
                    datapoint_modal.save()
                except:
                    failing_datapoints.append(datapoint_modal.get_name())
                    datapoint_modal.cancel()

    if len(failing_datapoints) != 0:
        raise ValueError(f'Not working properties: \n {failing_datapoints}')

    points_table = asset_templates_page.points_properties_table.get_table(unique_column_name='POINT')
    for datapoint_name in datpoint_names:
        assert datapoint_name in points_table.keys()


@pytest.mark.order(21)
def test_edit_properties(asset_templates_page):
    """
    WARUNKI WSTĘPNE:
        - Jestem na stronie Asset templates
        - Dodano Asset template
        - Jestem w trybie edycji Asset template'u"
    OPIS KROKU:
        1.
    OCZEKIWANY REZULTAT:
        1.
    """
    assert asset_templates_page.url == asset_templates_page.driver.current_url
    template_table = asset_templates_page.template_table(table_name='Central').get_table(
        unique_column_name='TEMPLATE NAME')
    assert template_table[TEMPLATE_FUNCTIONAL_TESTS]['TEMPLATE NAME'] == TEMPLATE_FUNCTIONAL_TESTS
    asset_templates_page.template_table('Central').edit_row(unique_column_name='TEMPLATE NAME',
                                                            row_name=TEMPLATE_FUNCTIONAL_TESTS)

    # step 1
    asset_templates_page.open_tab('Properties')
    points_table = asset_templates_page.points_properties_table.get_table(unique_column_name='PROPERTY')

    # step 2
    property_names = []
    failing_propertys = []
    for point_id in range(1, len(points_table)):
        asset_templates_page.points_properties_table.edit_row(row_id=point_id)
        edit_point_modal = AddDatapointPropertyModal(asset_templates_page.driver)
        property_name = edit_point_modal.get_name()
        property_name = property_name[0:24] + create_random_string(2) + '_edit'
        property_names.append(property_name)
        edit_point_modal.set_name(property_name)
        edit_point_modal.set_type(edit_point_modal.properties_types[random.randint(0, 1)])
        edit_point_modal.tags.set_new_tag('edit')
        try:
            edit_point_modal.save()
        except:
            failing_propertys.append(edit_point_modal.get_name())
            edit_point_modal.cancel()

    if len(failing_propertys) != 0:
        raise ValueError(f'Not working propertys: \n {failing_propertys}')

    points_table = asset_templates_page.points_properties_table.get_table(unique_column_name='PROPERTY')
    for property_name in property_names:
        assert property_name in points_table.keys()

