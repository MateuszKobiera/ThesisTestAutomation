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
        input_xpath = self.xpath + '//input'
        self.get_element()