from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from frontend.test_logger import get_logger


class ElementWaiting:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def wait_for_element(self, locator: (tuple, str), timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na widoczność elementu
        :param locator: xpath i typ elementu, do oczekiwania
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        :return:
        """
        self.logger.info(f'Waiting for element {locator} with poll frequency {poll_frequency}s and timeout {timeout}s')
        locator_xpath = locator if type(locator) == str else locator[0]
        WebDriverWait(self.driver, timeout, poll_frequency).until(
            visibility_of_element_located((By.XPATH, locator_xpath)),
            message=f'Element not found in {timeout}s. Check correctness of the xpath provided or extend timeout.')
        self.logger.info(f'Element {locator} found.')

    def wait_for_element_to_disappear(self, locator: (tuple, str), timeout: int = 5, poll_frequency: float = 0.1) -> None:
        """
        Oczekiwanie na zniknięcie elementu
        :param locator: xpath i typ elementu, do oczekiwania
        :param timeout: maksymalny czas czekania na element
        :param poll_frequency: czas próbkowania co jaki jest sprawdzana widoczność elementu
        """
        self.logger.info(f'Waiting for element to disappear {locator} with poll frequency {poll_frequency} and timeout {timeout}')
        WebDriverWait(self.driver, timeout, poll_frequency).until(
            invisibility_of_element_located((By.XPATH, locator[0])),
            message=f'Element is still visible in timeout {timeout}s.')
        self.logger.info(f'Element {locator} disappeared.')

    def check_is_element_visible(self, locator: (tuple, str), timeout: int = 1) -> bool:
        """
        Sprawdzenie czy dany element jest widoczny
        :param locator: xpath i typ elementu
        :param timeout: maksymalny czas czekania na element
        :return: True jeśli jest widoczny False jeśli nie znaleziono elementu w ciągu timeoutu
        """
        try:
            self.wait_for_element(locator, timeout)
            self.logger.info(f'Element {locator} was found.')
            return True
        except TimeoutException:
            self.logger.info(f'Element {locator} was not found - it was not visible in {timeout}s')
            return False

    def wait_for_loading_indicator(self, time_to_wait: int = 5, timeout: int = 15,
                                   polling_frequency: float = 0.5) -> None:
        """
        Wait for loading indicator to be present on page
        :return:
        """
        loading_indicator = "//div[contains(@class,'LoadingIndicator')]"
        try:
            self.wait_for_element(loading_indicator, time_to_wait)
            self.wait_for_element_to_disappear(loading_indicator, timeout, polling_frequency)
        except TimeoutException:
            pass


