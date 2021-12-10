import random

from frontend.locators.Modals.add_datapoint_property_modal_locators import AddDatapointPropertyLocators
from utils.string_editor import create_random_string


def test_add_datapoints(asset_templates_page):
    """
    WARUNKI WSTĘPNE:
        - Jestem na stronie Asset templates
        - Dodano Asset template
        - Jestem w trybie edycji Asset template'u"
    OPIS KROKU:
        1. Kliknij przycisk 'Add datapoint'
        2. Wybierz każdy standardowy datapoint, zedytuj i zapisz
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


def test_edit_datapoints():
    pass


def test_add_properties(asset_templates_page):
    """
    WARUNKI WSTĘPNE:
        - Jestem na stronie Asset templates
        - Dodano Asset template
        - Jestem w trybie edycji Asset template'u"
    OPIS KROKU:
        1. Kliknij przycisk 'Add datapoint'
        2. Wybierz każdy standardowy datapoint, zedytuj i zapisz
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


def test_edit_properties():
    pass


# @when("Kliknę przycisk 'Add property'", target_fixture='property_modal')
# def property_modal(asset_templates_page):
#     asset_templates_page.open_tab('Properties')
#     return asset_templates_page.click_add_property()
