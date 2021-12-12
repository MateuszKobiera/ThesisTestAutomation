from selenium import webdriver

from frontend.elements.button import Button


class Switcher(Button):
    """
    Switcher (Toggle) element
    """
    def __init__(self, driver: webdriver, xpath: str):
        super().__init__(driver, xpath)

    def is_checked(self) -> bool:
        """
        Checks if switcher is active
        :return: True if active
        """
        checkbox_class = self.get_base_element(self.xpath).driver.get_attribute('class')
        if 'switchedOn' in checkbox_class:
            return True
        else:
            return False
