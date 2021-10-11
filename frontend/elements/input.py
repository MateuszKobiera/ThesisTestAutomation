from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from frontend.elements.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, driver: webdriver, xpath: str):
        super().__init__(driver, xpath)

    def get_label(self) -> str:
        """
        Pobranie etykiety nad listą rozwijaną
        :return:
        """
        label_xpath = self.xpath + '/div[contains(@class,"label")]'
        return self.get_base_element(label_xpath).get_text()

    def get_validation(self) -> str:
        """
        Pobranie wiadomości walidacyjnej pod listą rozwijaną
        :return:
        """
        validation_xpath = self.xpath + '/div[contains(@class,"validation")]'
        return self.get_base_element(validation_xpath).get_text()

    def set_value(self, input_text: str, clear_input_before: bool = True) -> None:
        """
        Ustawienie wartości do pola tekstowego
        :param input_text:
        :param clear_input_before: wyczyszczenie wartości pola tekstowego przed wpisaniem wartości, standardowo włączone
        :return:
        """
        input_xpath = self.xpath + '//input'
        if clear_input_before:
            self.get_base_element(input_xpath).driver.send_keys(Keys.CONTROL + "a")
            self.get_base_element(input_xpath).driver.send_keys(Keys.DELETE)
        self.get_base_element(input_xpath).driver.send_keys(input_text)
