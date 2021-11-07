from selenium import webdriver

from frontend.components.base_component import BaseComponent


class Tags(BaseComponent):
    def __init__(self, driver: webdriver, xpath: str):
        """
        Podstawowy element
        :param driver:
        :param xpath:
        """
        super().__init__(driver)
        self.xpath = xpath

    def set_new_tag(self, tag_name: str) -> None:
        """
        Sets new tag for tag component
        :param tag_name:
        :return:
        """
        add_button = self.xpath + '//button'
        self.get_element((self.xpath, "Input")).set_value(tag_name)
        self.get_element((add_button, "Button")).click()

    def get_tags(self) -> list:
        """
        Get all tags names in tags component
        :return: list of tag names
        """
        tags_list_xpath = self.xpath + "//div[contains(@style, 'wrap')]"
        tags_list: list = []
        for element in self.get_multiple_elements(tags_list_xpath):
            tags_list.append(element.text)
        return tags_list
