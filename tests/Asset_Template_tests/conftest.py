import pytest
from selenium import webdriver

from frontend.objects.Pages.asset_templates_page import AssetTemplatesPage

TEMPLATE_FUNCTIONAL_TESTS = 'RTU'


@pytest.fixture
def asset_templates_page(browser: webdriver, log_in, menu_page) -> AssetTemplatesPage:
    menu_page.go_to_asset_templates()
    return AssetTemplatesPage(browser)
