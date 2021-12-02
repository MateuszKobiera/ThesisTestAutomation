import pytest

from frontend.objects.Pages.my_property_page import MyPropertyPage


@pytest.fixture
def my_property_page(browser, menu_page):
    menu_page.go_to_my_property()
    return MyPropertyPage(browser)

