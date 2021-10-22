import logging

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from frontend.components.table import Table
from frontend.elements.base_element import BaseElement
from frontend.elements.button import Button
from frontend.elements.dropdown import Dropdown
from frontend.elements.input import Input
from frontend.test_logger import get_logger


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = 'http://192.168.1.10/'
        self.logger = get_logger(self.__class__.__name__)

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

    def wait_for_element(self, locator: tuple, timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na widoczność elementu
        :param locator: xpath i typ elementu, do oczekiwania
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        :return:
        """
        self.logger.info(f'Waiting for element {locator} with poll frequency {poll_frequency}s and timeout {timeout}s')
        WebDriverWait(self.driver, timeout, poll_frequency).until(visibility_of_element_located((By.XPATH, locator[0])))

    def wait_for_element_to_disappear(self, locator: tuple, timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na zniknięcie elementu
        :param locator: xpath i typ elementu, do oczekiwania
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        """
        self.logger.info(f'Waiting for element to disappear {locator} with poll frequency {poll_frequency} and timeout {timeout}')
        WebDriverWait(self.driver, timeout, poll_frequency).until(invisibility_of_element_located((By.XPATH, locator[0])))

    def check_is_element_visible(self, locator: tuple, timeout: int = 1) -> bool:
        """
        Sprawdzenie czy dany element jest widoczny
        :param locator: xpath i typ elementu
        :param timeout: maksymalny czas czekania na element
        :return: True jeśli jest widoczny False jeśli nie znaleziono elementu w ciągu timeoutu
        """
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            self.logger.info(f'Element {locator} was not found - it was not visible in {timeout}s')
            return False

    def open_tab(self, tab_name:str) -> None:
        """
        Zmiana zakładki
        :param tab_name: Nazwa zakładki, którą chcemy otworzyć
        :return:
        """
        tab_element = f"//a[text()='{tab_name}']//ancestor::li", "Base"
        self.get_element(tab_element).click()
