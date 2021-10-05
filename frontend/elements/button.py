from selenium import webdriver

from frontend.elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, driver: webdriver, xpath: str):
        super().__init__(driver, xpath)

