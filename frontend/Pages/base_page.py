from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from frontend.elements.base_element import BaseElement
from frontend.elements.button import Button
from frontend.elements.dropdown import Dropdown
from frontend.elements.input import Input


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = 'http://192.168.1.254/'

    def get_element(self, locator: tuple) -> webdriver:
        """
        Wybranie elementu
        :param locator: xpath i typ elementu do znalezienia
        :return: sterownik elementu
        """
        if locator[1] == 'Button':
            element = Button(self.driver.find_element_by_xpath(locator[0]), locator[0])
        elif locator[1] == 'Input':
            element = Input(self.driver.find_element_by_xpath(locator[0]), locator[0])
        elif locator[1] == 'Dropdown':
            element = Dropdown(self.driver.find_element_by_xpath(locator[0]), locator[0])
        else:
            element = BaseElement(self.driver.find_element_by_xpath(locator[0]), locator[0])
        return element

    def wait_for_element(self, locator: tuple, timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na widoczność elementu
        :param locator: xpath i typ elementu, do oczekiwania
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        :return:
        """
        WebDriverWait(self.driver, timeout, poll_frequency).until(visibility_of_element_located((By.XPATH, locator[0])))
