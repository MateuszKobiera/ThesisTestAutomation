import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

from frontend.locators.Modals.add_datapoint_property_modal_locators import AddDatapointPropertyLocators
from frontend.objects.Modals.base_modal import BaseModal


class AddDatapointPropertyModal(BaseModal):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.datapoint_types = ['Command', 'Feedback', 'Command And Feedback', 'Configuration']
        self.properties_types = ['Read and write', 'Read only']

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

    # def get_datapoint_names(self) -> list:
    #     datapoint_names = []
    #     for expander in self.driver.find_elements_by_xpath(AddDatapointPropertyLocators.expander_datapoints[0]):
    #         expander.click()
    #         time.sleep(0.1)
    #     for datapoint in range(1, len(self.driver.find_elements_by_xpath(AddDatapointPropertyLocators.datapoint_names[0]))):
    #         datapoint_names.append(self.driver.find_elements_by_xpath(AddDatapointPropertyLocators.datapoint_names[0])[datapoint].text)
    #     return datapoint_names

    def get_datapoint_names(self) -> dict:
        datapoint_names = {}
        depth0 = "//div[contains(@class, 'depth0')]/span/span[contains(@class, 'Collapsible__title')]"
        depth1 = "//*[text()='{}']/../..//div[contains(@class, 'depth1')]/span/span[contains(@class, 'Collapsible__title')]"
        depth2 = "//*[text()='{}']/../..//*[text()='{}']/../..//div[contains(@class, 'depth2')]/span/span[contains(@class, 'Collapsible__title')]"
        for x in range(0, len(self.get_multiple_elements(depth0))):
            self.get_multiple_elements(depth0)[x].click()
            time.sleep(0.2)
            datapoint_names[self.get_multiple_elements(depth0)[x].text] = {}
            # datapoint_names[self.get_multiple_elements(depth0)[x].text]['element'] = self.get_multiple_elements(depth0)[x]
        for point in datapoint_names:
            for y in range(0, len(self.get_multiple_elements(depth1.format(point)))):
                self.get_multiple_elements(depth1.format(point))[y].click()
                time.sleep(0.2)
                datapoint_names[point][self.get_multiple_elements(depth1.format(point))[y].text] = []
                # datapoint_names[point][self.get_multiple_elements(depth1.format(point))[y].text]['element'] = self.get_multiple_elements(depth1.format(point))[y]
                # if 'hasChildern' in datapoint_names[point]['element'].get_attribute('class'):
                #     datapoint_names[point]['element'].click()
                #     time.sleep(0.2)
        for point1 in datapoint_names:
            for point2 in datapoint_names[point1]:
                # if 'hasChildern' in datapoint_names[point1][point2]['element'].get_attribute('class'):
                #     datapoint_names[point1][point2].click()
                #     time.sleep(0.2)
                    for z in range(0, len(self.get_multiple_elements(depth2.format(point1, point2)))):
                        datapoint_names[point1][point2].append(self.get_multiple_elements(depth2.format(point1, point2))[z].text)
                        # datapoint_names[point1][point2][self.get_multiple_elements(depth2.format(point1, point2))[z].text]['element'] = self.get_multiple_elements(depth2.format(point1, point2))[z]
        datapoint_names.pop('Custom')
        return datapoint_names

    def get_type(self) -> str:
        return self.get_element(AddDatapointPropertyLocators.format_dropdown).get_text()

    def get_name(self) -> str:
        return self.get_element(AddDatapointPropertyLocators.name_input).get_value()

    def click_choose_datapoint(self, category: str, subcategory: str = '', datapoint: str = '') -> None:
        """

        :param category:
        :param datapoint:
        :param subcategory:
        :return:
        """
        category_xpath = f"//*[@class='ReactModalPortal']//*[text()='{category}']"
        self.get_element((category_xpath, "Expandable")).expand()
        subcategory_xpath = f"/../..//*[text()='{subcategory}']"
        datapoint_xpath = f"/../..//*[contains(@class,'depth2')]//*[text()='{datapoint}']"
        if datapoint != '':
            xpath = category_xpath + subcategory_xpath + datapoint_xpath
            self.get_element((category_xpath + subcategory_xpath, "Expandable")).expand()
        else:
            xpath = category_xpath + subcategory_xpath
        self.get_element((xpath, "Base")).click()
