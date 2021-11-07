from selenium import webdriver

from frontend.Locators.Modals.add_asset_template_modal_locators import AddAssetTemplateLocators
from frontend.components.tags import Tags
from frontend.objects.Modals.base_modal import BaseModal


class AddAssetTemplateModal(BaseModal):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait_for_element(AddAssetTemplateLocators.template_name_input)

    @property
    def tags(self) -> Tags:
        return self.get_component(AddAssetTemplateLocators.tags_component)

