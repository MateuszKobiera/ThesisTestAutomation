from selenium import webdriver

from frontend.element_waiting import ElementWaiting
from frontend.elements.base_element import BaseElement
from frontend.elements.button import Button
from frontend.elements.dropdown import Dropdown
from frontend.elements.input import Input


class ElementCreation(ElementWaiting):
    def __init__(self, driver: webdriver):
        """
        Podstawowy element
        :param driver:
        """
        super().__init__(driver)

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
