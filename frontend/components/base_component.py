from selenium import webdriver

from frontend.element_creation import ElementCreation


class BaseComponent(ElementCreation):
    def __init__(self, driver: webdriver):
        """
        Podstawowy element
        :param driver:
        """
        super().__init__(driver)
