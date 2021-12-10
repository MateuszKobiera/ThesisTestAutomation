from selenium import webdriver

from frontend.elements.button import Button


class Expandable(Button):
    def __init__(self, driver: webdriver, xpath: str):
        super().__init__(driver, xpath)

    def is_expanded(self) -> bool:
        expandable_element = self.get_base_element(self.xpath+'/..')
        if 'Expanded' in expandable_element.driver.get_attribute('class'):
            return True
        else:
            return False

    def expand(self) -> None:
        if self.is_expanded() is False:
            self.click()
