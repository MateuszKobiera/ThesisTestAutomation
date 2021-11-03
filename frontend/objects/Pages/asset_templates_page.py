from selenium import webdriver

from frontend.objects.Pages.base_page import BasePage


class AssetTemplatesPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
