from selenium import webdriver

from frontend.Locators.Pages.asset_templates_locators import AssetTemplatesLocators
from frontend.objects.Pages.base_page import BasePage


class AssetTemplatesPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait_for_element(AssetTemplatesLocators.add_template[0].format('Central'))

    def click_add_button(self, table_name: str) -> None:
        """
        Clicks on a Add button name for a specific table
        :param table_name:
        :return:
        """
        if self.check_is_element_visible(AssetTemplatesLocators.add_template[0].format('Central')):
            self.get_element_with_format(AssetTemplatesLocators.add_template, table_name).click()
        else:
            self.logger(f"Change tab to the correct one or check correctness of the table_name {table_name}")
