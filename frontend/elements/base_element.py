from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located
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
        self.wait_for_element()

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
        self.logger.info(f'Trying to get text of element with xpath {self.xpath}')
        return self.driver.text

    def get_base_element(self, locator_xpath: str) -> webdriver:
        """
        Wybranie elementu
        :param locator_xpath: xpath i typ elementu do znalezienia
        :return: sterownik elementu
        """
        self.logger.info(f'Trying to get base element with xpath {self.xpath}')
        return BaseElement(self.driver.find_element_by_xpath(locator_xpath), locator_xpath)

    def wait_for_element(self, timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na widoczność elementu
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        :return:
        """
        self.logger.info(f'Waiting for element {self.xpath} with poll frequency {poll_frequency}s and timeout {timeout}s')
        WebDriverWait(self.driver, timeout, poll_frequency).until(
            visibility_of_element_located((By.XPATH, self.xpath)),
            message=f'Element not found in {timeout}s. Check correctness of the xpath provided or extend timeout.')
        self.logger.info(f'Element {self.xpath} found.')

    def wait_for_element_to_disappear(self, timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na zniknięcie elementu
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        """
        self.logger.info(f'Waiting for element to disappear {self.xpath} with poll frequency {poll_frequency} and timeout {timeout}')
        WebDriverWait(self.driver, timeout, poll_frequency).until(
            invisibility_of_element_located((By.XPATH, self.xpath)),
            message=f'Element is still visible in timeout {timeout}s.')
        self.logger.info(f'Element {self.xpath} disappeared.')

    def is_element_visible(self, timeout: int = 1) -> bool:
        """
        Sprawdzenie czy dany element jest widoczny
        :param timeout: maksymalny czas czekania na element
        :return: True jeśli jest widoczny False jeśli nie znaleziono elementu w ciągu timeoutu
        """
        try:
            self.wait_for_element(timeout)
            self.logger.info(f'Element {self.xpath} was found.')
            return True
        except TimeoutException:
            self.logger.info(f'Element {self.xpath} was not found - it was not visible in {timeout}s')
            return False
