from pytest_bdd import scenario, given, then, when

from frontend.Locators.my_property_locators import MyPropertyLocators


@scenario("property_structure.feature", "Wyświetlanie okna dialogowego dla budynku")
def test_impl():
    pass


@given('Jestem na stronie My property - Structure')
def step_impl(log_in, my_property_page):
    my_property_page.open_tab('Structure')
    my_property_page.wait_for_element(MyPropertyLocators.structure_table)
    assert my_property_page.url == my_property_page.driver.current_url


@given('Nie dodano budynku')
def step_impl(my_property_page):
    my_property_page.get_structure_table()


@when('Kliknę w przycisk "Add structure"')
def step_impl(my_property_page):
    assert my_property_page.get_country() == 'Poland'


@then('Pokazuje się okno dialogowe dla dodania budynku')
def step_impl(my_property_page):
    pass
