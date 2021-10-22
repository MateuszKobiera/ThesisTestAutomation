from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

from frontend.element_waiting import ElementWaiting


class BaseElement(ElementWaiting):
    """
    Podstawowy element, którego metody są uniwersalne
    """
    def __init__(self, driver: webdriver, xpath: str):
        """
        Podstawowy element
        :param driver:
        :param xpath:
        """
        super().__init__(driver)
        self.driver = driver
        self.xpath = xpath

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

    def get_base_element(self, locator: str) -> webdriver:
        """
        Wybranie elementu
        :param locator: xpath i typ elementu do znalezienia
        :return: sterownik elementu
        """
        self.logger.info(f'Trying to get base element with xpath {self.xpath}')
        return BaseElement(self.driver.find_element_by_xpath(locator), locator)

