from selenium import webdriver

from frontend.components.table import Table
from frontend.element_waiting import ElementWaiting
from frontend.elements.base_element import BaseElement
from frontend.elements.button import Button
from frontend.elements.dropdown import Dropdown
from frontend.elements.input import Input


class BasePage(ElementWaiting):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = 'http://192.168.1.10/'

    def get_element(self, locator: tuple) -> webdriver:
        """
        Wybranie elementu
        :param locator: xpath i typ elementu do znalezienia
        :return: sterownik elementu
        """

        self.logger.info(f'Trying to find element {locator}')
        if locator[1] == 'Button':
            element = Button(self.driver.find_element_by_xpath(locator[0]), locator[0])
        elif locator[1] == 'Input':
            element = Input(self.driver.find_element_by_xpath(locator[0]), locator[0])
        elif locator[1] == 'Dropdown':
            element = Dropdown(self.driver.find_element_by_xpath(locator[0]), locator[0])
        else:
            element = BaseElement(self.driver.find_element_by_xpath(locator[0]), locator[0])
        self.logger.info(f'Found element {locator}')
        return element

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
        else:
            self.logger.error(f'Component {locator} not found')
            raise ValueError('Nie ma takiego komponentu')
        return component

    def open_tab(self, tab_name:str) -> None:
        """
        Zmiana zakładki
        :param tab_name: Nazwa zakładki, którą chcemy otworzyć
        :return:
        """
        tab_element = f"//a[text()='{tab_name}']//ancestor::li", "Base"
        self.get_element(tab_element).click()
