from selenium import webdriver

from frontend.Locators.Pages.asset_templates_locators import AssetTemplatesLocators
from frontend.objects.Modals.add_asset_template_modal import AddAssetTemplateModal
from frontend.objects.Modals.add_datapoint_property_modal import AddDatapointPropertyModal
from frontend.objects.Pages.base_page import BasePage


class AssetTemplatesPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait_for_element(AssetTemplatesLocators.add_template[0].format('Central'), timeout=8)

    def click_add_button(self, table_name: str) -> AddAssetTemplateModal:
        """
        Clicks on a Add button name for a specific table
        :param table_name:
        :return:
        """
        if self.check_is_element_visible(AssetTemplatesLocators.add_template[0].format(table_name)):
            self.get_element_with_format(AssetTemplatesLocators.add_template, table_name).click()
        else:
            raise NameError(f"Change tab to the correct one or check correctness of the table_name {table_name}")
        return AddAssetTemplateModal(self.driver)

    def template_table(self, table_name: str):
        return self.get_component_with_format(AssetTemplatesLocators.template_table, table_name)

    def set_master_slave(self):
        if not self.get_element(AssetTemplatesLocators.master_slave_switcher).is_active():
            self.get_element(AssetTemplatesLocators.master_slave_switcher).click()

    def click_add_datapoint(self) -> AddDatapointPropertyModal:
        self.get_element(AssetTemplatesLocators.add_datapoint_button).click()
        return AddDatapointPropertyModal(self.driver)

    def click_add_property(self) -> AddDatapointPropertyModal:
        self.get_element(AssetTemplatesLocators.add_property_button).click()
        return AddDatapointPropertyModal(self.driver)

    @property
    def points_properties_table(self):
        return self.get_component(AssetTemplatesLocators.point_properties_table)

    @property
    def template_tags(self):
        return self.get_component(AssetTemplatesLocators.tags_component)
