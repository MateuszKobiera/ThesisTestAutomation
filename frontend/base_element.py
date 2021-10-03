from selenium import webdriver


class BaseElement:

    def __init__(self, driver: webdriver, element_type, xpath):
        """
        :param driver:
        """
        self.driver = driver
        self.element_type = element_type
        self.xpath = xpath
