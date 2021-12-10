from pytest_bdd import scenario, given, then, when


@scenario("property_overview.feature", "Ustawienie poprawnych danych nieruchomości")
def test_add_property():
    pass


@given('Jestem na stronie My Property')
def step_impl(log_in, my_property_page):
    assert my_property_page.url == my_property_page.driver.current_url


@when('Wpisuje poprawne dane nieruchomości')
def step_impl(my_property_page):
    my_property_page.set_property_name('Sukiennice')
    my_property_page.set_address('Rynek główny')
    my_property_page.set_zip_code('30-011')
    my_property_page.set_town('Kraków')
    my_property_page.set_country('Poland')
    my_property_page.set_gps_latitude('21.57')
    my_property_page.set_gps_longitude('12.12')
    my_property_page.set_property_type('Industrial')
    my_property_page.set_main_usage('Casino')
    my_property_page.set_gross_surface('1234')
    my_property_page.set_people('1234')
    my_property_page.save()


@then('Dane zostały poprawnie zapisane')
def step_impl(my_property_page):
    assert my_property_page.get_country() == 'Poland'
    assert my_property_page.get_property_name() == 'Sukiennice'
    assert my_property_page.get_address() == 'Rynek główny'
    assert my_property_page.get_zip_code() == '30-011'
    assert my_property_page.get_town() == 'Kraków'
    assert my_property_page.get_country() == 'Poland'
    assert my_property_page.get_gps_latitude() == '21.57'
    assert my_property_page.get_gps_longitude() == '12.12'
    assert my_property_page.get_property_type() == 'Industrial'
    assert my_property_page.get_main_usage() == 'Casino'
    assert my_property_page.get_gross_surface() == '1234'
    assert my_property_page.get_people() == '1234'


@then('Zakładka Structure została odblokowana')
def step_impl(my_property_page):
    my_property_page.open_tab('Structure')


@when("Nie wpisano danych nieruchomości")
def step_impl(my_property_page):
    my_property_page.save()