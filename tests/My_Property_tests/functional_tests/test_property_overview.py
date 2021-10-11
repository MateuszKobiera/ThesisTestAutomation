from pytest_bdd import scenario, given, then, when


@scenario("property_overview.feature", "Ustawienie poprawnych danych nieruchomości")
def test_impl():
    pass


@given('Jestem na stronie My Property')
def step_impl(log_in, my_property_page):
    assert my_property_page.url == my_property_page.driver.current_url


@when('Wpisuje poprawne dane nieruchomości')
def step_impl(my_property_page):
    my_property_page.set_country('Poland')


@then('Dane zostały poprawnie zapisane')
def step_impl(my_property_page):
    assert my_property_page.get_country() == 'Poland'


@then('Zakładka Structure została odblokowana')
def step_impl(my_property_page):
    pass
