from selenium import webdriver

from frontend.Locators.Pages.menu_locators import MenuLocators
from frontend.objects.Pages.base_page import BasePage


class MenuPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/app/apps'
        self.wait_for_element(MenuLocators.my_property_widget, timeout=15)

    def check_enabled_widgets(self, widgets: tuple):
        for widget in MenuLocators.all_main_widgets:
            if widget in widgets:
                assert self.check_is_element_visible(widget) is True
            else:
                assert self.check_is_element_visible(widget) is False

    def go_to_my_property(self) -> None:
        """Opens My property widget by clicking on it"""
        self.get_element(MenuLocators.my_property_widget).click()

    def go_to_asset_templates(self) -> None:
        """Opens Asset templates widget by clicking on it"""
        self.get_element(MenuLocators.asset_templates_widget).click()
