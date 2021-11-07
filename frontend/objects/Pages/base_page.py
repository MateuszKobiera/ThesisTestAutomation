from typing import Union

from selenium import webdriver

from frontend.components.table import Table
from frontend.components.tags import Tags
from frontend.element_creation import ElementCreation
from frontend.elements.base_element import BaseElement
from frontend.elements.button import Button
from frontend.elements.dropdown import Dropdown
from frontend.elements.input import Input


class BasePage(ElementCreation):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = 'http://192.168.1.254/'

    def get_element_with_format(self, locator: tuple, *args) -> Union[Dropdown, Input, Button, BaseElement]:
        """
        Get element when format of element is needed
        :param locator: locator of element
        :param args: data for formatting the element
        :return: element driver
        """
        self.logger.info(f'Trying to format the element {locator} with data {args}')
        return self.get_element((locator[0].format(*args), locator[1]))

    def get_component(self, locator: tuple) -> webdriver:
        """
        Wybranie komponentu
        :param locator: xpath i typ elementu do znalezienia
        :return: sterownik komponentu
        """
        self.logger.info(f'Trying to find component {locator}')
        if locator[1] == 'Table':
            component = Table(self.driver.find_element_by_xpath(locator[0]), locator[0])
            self.logger.info(f'Found component {locator}')
        elif locator[1] == 'Tags':
            component = Tags(self.driver.find_element_by_xpath(locator[0]), locator[0])
            self.logger.info(f'Found component {locator}')
        else:
            self.logger.error(f'Component {locator} not found')
            raise ValueError('Nie ma takiego komponentu')
        return component

    def open_tab(self, tab_name: str) -> None:
        """
        Zmiana zakładki
        :param tab_name: Nazwa zakładki, którą chcemy otworzyć
        :return:
        """
        tab_element = f"//a[text()='{tab_name}']//ancestor::li", "Base"
        self.get_element(tab_element).click()
