from selenium import webdriver

from frontend.Locators.Modals.add_datapoint_property_modal_locators import AddDatapointPropertyLocators
from frontend.objects.Modals.base_modal import BaseModal


class AddDatapointPropertyModal(BaseModal):
    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def click_custom_datapoint(self) -> None:
        self.get_element(AddDatapointPropertyLocators.custom_datapoint).click()
        
    def set_name(self, point_name: str) -> None:
        self.get_element(AddDatapointPropertyLocators.name_input).set_value(point_name)
        
    def set_type(self, point_type: str) -> None:
        self.get_element(AddDatapointPropertyLocators.type_dropdown).choose_option(point_type)
        
    def set_format(self, point_format: str) -> None:
        self.get_element(AddDatapointPropertyLocators.format_dropdown).choose_option(point_format)
        
    def set_unit(self, point_unit: str) -> None:
        self.get_element(AddDatapointPropertyLocators.unit_dropdown).choose_option_with_input(point_unit)
        
    def set_min_value(self, point_min_value: str) -> None:
        self.get_element(AddDatapointPropertyLocators.min_value_input).set_value(point_min_value)
        
    def set_max_value(self, point_max_value: str) -> None:
        self.get_element(AddDatapointPropertyLocators.max_value_input).set_value(point_max_value)
        
    def set_display_unit(self, point_display_unit: str) -> None:
        self.get_element(AddDatapointPropertyLocators.display_unit_dropdown).choose_option(point_display_unit)

    @property
    def tags(self):
        return self.get_component(AddDatapointPropertyLocators.tags_component)
