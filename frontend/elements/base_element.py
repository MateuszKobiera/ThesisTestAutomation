from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from frontend.test_logger import get_logger


class BaseElement:
    """
    Podstawowy element, którego metody są uniwersalne
    """
    def __init__(self, driver: webdriver, xpath: str):
        """
        Podstawowy element
        :param driver:
        :param xpath:
        """
        self.driver = driver
        self.xpath = xpath
        self.logger = get_logger(self.__class__.__name__)

    def click(self) -> None:
        """
        Click on a element
        :return:
        """
        self.logger.info(f'Trying to click element with xpath {self.xpath}')
        try:
            self.driver.click()
        except StaleElementReferenceException:
            self.logger.warn('StaleElementReferenceException occurred. Trying to refresh driver.')
            self.driver.refresh()
            self.driver.click()
        self.logger.info(f'Element with xpath {self.xpath} was clicked')

    def get_text(self) -> str:
        """
        Get available text for an element
        :return:
        """
        return self.driver.text

    def wait_for_element(self, locator: str, timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na widoczność elementu
        :param locator: xpath i typ elementu, do oczekiwania
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        :return:
        """
        WebDriverWait(self.driver, timeout, poll_frequency).until(visibility_of_element_located((By.XPATH, locator)))

    def get_base_element(self, locator: str) -> webdriver:
        """
        Wybranie elementu
        :param locator: xpath i typ elementu do znalezienia
        :return: sterownik elementu
        """
        return BaseElement(self.driver.find_element_by_xpath(locator), locator)

    def check_is_element_visible(self, locator: tuple, timeout: int = 1, poll_frequency: float = 0.1) -> bool:
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(visibility_of_element_located((By.XPATH, locator[0])))
            return True
        except TimeoutException:
            return False
