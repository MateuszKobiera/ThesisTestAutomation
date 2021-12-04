from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from frontend.elements.base_element import BaseElement
from frontend.elements.button import Button
from frontend.elements.dropdown import Dropdown
from frontend.elements.input import Input
from frontend.elements.switcher import Switcher
from frontend.test_logger import get_logger


class ElementCreation:
    def __init__(self, driver: webdriver):
        """
        Podstawowy element
        :param driver:
        """
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def __wait_for_element(self, xpath: str, timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na widoczność elementu
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        :return:
        """
        self.logger.info(f'Waiting for element {xpath} with poll frequency {poll_frequency}s and timeout {timeout}s')
        WebDriverWait(self.driver, timeout, poll_frequency).until(
            visibility_of_element_located((By.XPATH, xpath)),
            message=f'Element not found in {timeout}s. Check correctness of the xpath provided or extend timeout.')
        self.logger.info(f'Element {xpath} found.')

    def get_element(self, locator: tuple) -> webdriver:
        """
        Wybranie elementu
        :param locator: xpath i typ elementu do znalezienia
        :return: sterownik elementu
        """

        self.logger.info(f'Trying to find element {locator}')
        self.__wait_for_element(locator[0], timeout=15)

        if locator[1] == 'Button':
            element = Button(self.driver.find_element_by_xpath(locator[0]), locator[0])
        elif locator[1] == 'Input':
            element = Input(self.driver.find_element_by_xpath(locator[0]), locator[0])
        elif locator[1] == 'Dropdown':
            element = Dropdown(self.driver.find_element_by_xpath(locator[0]), locator[0])
        elif locator[1] == 'Switcher':
            element = Switcher(self.driver.find_element_by_xpath(locator[0]), locator[0])
        else:
            element = BaseElement(self.driver.find_element_by_xpath(locator[0]), locator[0])
        self.logger.info(f'Found element {locator}')
        return element

    def get_multiple_elements(self, locator_xpath: str) -> list:
        """
        Get multiple elements
        :param locator_xpath:
        :return: list of webdrivers
        """
        return self.driver.find_elements_by_xpath(locator_xpath)
