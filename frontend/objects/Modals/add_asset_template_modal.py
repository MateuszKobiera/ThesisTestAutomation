from selenium import webdriver

from frontend.Locators.Modals.add_asset_template_modal_locators import AddAssetTemplateLocators
from frontend.components.icons import Icons
from frontend.components.tags import Tags
from frontend.objects.Modals.base_modal import BaseModal


class AddAssetTemplateModal(BaseModal):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait_for_element(AddAssetTemplateLocators.template_name_input)

    @property
    def tags(self) -> Tags:
        return self.get_component(AddAssetTemplateLocators.tags_component)

    @property
    def icons(self) -> Icons:
        return self.get_component(AddAssetTemplateLocators.icons_component)

    def set_template_name(self, template_name: str) -> None:
        self.get_element(AddAssetTemplateLocators.template_name_input).set_value(template_name)

    def set_template_type(self, template_type: str) -> None:
        self.get_element(AddAssetTemplateLocators.template_type_dropdown).choose_option(template_type)

