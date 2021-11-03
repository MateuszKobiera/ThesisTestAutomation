import pytest
from selenium import webdriver

from frontend.objects.Pages.asset_templates_page import AssetTemplatesPage


@pytest.fixture
def asset_templates_page(browser: webdriver) -> AssetTemplatesPage:
    return AssetTemplatesPage(browser)
