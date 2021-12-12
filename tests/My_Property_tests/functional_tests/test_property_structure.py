import pytest
from pytest_bdd import scenario, given, then, when

from frontend.locators.Pages.my_property_locators import MyPropertyLocators


@pytest.mark.order(15)
@scenario("property_structure.feature", "Wyświetlanie okna dialogowego dla budynku")
def test_dialog_opened():
    pass


@pytest.mark.order(16)
@scenario("property_structure.feature", "Dodanie pierwszego budynku")
def test_add_building():
    pass


@pytest.mark.order(17)
@scenario("property_structure.feature", "Dodanie piętra dla budynku")
def test_add_floor():
    pass


@given('Jestem na stronie My property - Structure')
def step_impl(log_in, my_property_page):
    my_property_page.open_tab('Structure')
    my_property_page.get_element(MyPropertyLocators.structure_table).wait_for_element()
    assert my_property_page.url == my_property_page.driver.current_url


@given('Nie dodano budynku')
def step_impl(my_property_page):
    assert my_property_page.get_structure_table(empty_table=True)[0]['ELEMENT TYPE'] == \
           'No element - Click on \'Add to structure\' to insert first structural element'


@when('Kliknę w przycisk "Add structure"', target_fixture='add_structure_modal')
def add_structure_modal(my_property_page):
    return my_property_page.add_new_structure()


@given("Wyświetlono okno dialogowe dla dodania budynku", target_fixture='add_structure_modal')
def step_impl(my_property_page):
    modal = my_property_page.add_new_structure()
    assert modal.get_title() == 'Add new structure element'
    return modal


@then("Wyświetlono okno dialogowe dla dodania budynku")
def step_impl(add_structure_modal):
    assert add_structure_modal.get_title() == 'Add new structure element'


@when("Uzupełniam poprawne dane dla budynku")
def step_impl(add_structure_modal):
    add_structure_modal.set_name('Empire State Building')
    add_structure_modal.set_usage('Museum')
    add_structure_modal.set_people_quantity('1231')
    add_structure_modal.set_gross_surface('1232')
    add_structure_modal.set_net_surface('1233')
    add_structure_modal.save()


@then("Dodano nowy budynek")
def step_impl(my_property_page):
    assert my_property_page.get_structure_table()['Empire State Building']['ELEMENT TYPE'] == 'Building'
    assert my_property_page.get_structure_table()['Empire State Building']['LEVEL TO GROUND'] == ''
    assert my_property_page.get_structure_table()['Empire State Building']['NAME'] == 'Empire State Building'
    assert my_property_page.get_structure_table()['Empire State Building']['USAGE'] == 'Museum'
    assert my_property_page.get_structure_table()['Empire State Building']['PEOPLE QUANTITY'] == '1231'
    assert my_property_page.get_structure_table()['Empire State Building']['GROSS SURFACE'] == '1232'
    assert my_property_page.get_structure_table()['Empire State Building']['NET SURFACE'] == '1233'


@given("Dodano budynek")
def step_impl(my_property_page):
    assert my_property_page.get_structure_table()['Empire State Building']['ELEMENT TYPE'] == 'Building'


@when("Uzupełniam poprawne dane dla piętra")
def step_impl(add_structure_modal):
    add_structure_modal.set_element_type('Floor')
    add_structure_modal.set_element_in_building('Empire State Building')
    add_structure_modal.set_name('Glass restaurant')
    add_structure_modal.set_level_to_ground('1')
    add_structure_modal.set_usage('Bar')
    add_structure_modal.set_people_quantity('111')
    add_structure_modal.set_gross_surface('112')
    add_structure_modal.set_net_surface('113')
    add_structure_modal.save()


@then("Dodano piętro do budynku")
def step_impl(my_property_page):
    assert my_property_page.get_structure_table()['Glass restaurant']['ELEMENT TYPE'] == 'Floor'
    assert my_property_page.get_structure_table()['Glass restaurant']['LEVEL TO GROUND'] == '1'
    assert my_property_page.get_structure_table()['Glass restaurant']['NAME'] == 'Glass restaurant'
    assert my_property_page.get_structure_table()['Glass restaurant']['USAGE'] == 'Bar'
    assert my_property_page.get_structure_table()['Glass restaurant']['PEOPLE QUANTITY'] == '111'
    assert my_property_page.get_structure_table()['Glass restaurant']['GROSS SURFACE'] == '112'
    assert my_property_page.get_structure_table()['Glass restaurant']['NET SURFACE'] == '113'
