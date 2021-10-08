from selenium import webdriver

from frontend.elements.input import Input


class Dropdown(Input):
    def __init__(self, driver: webdriver, xpath: str):
        super().__init__(driver, xpath)

    def choose_option(self, option: str) -> None:
        """
        Wybieranie opcji z listy rozwijanej
        :param option: nazwa opcji z listy
        :return:
        """
        option_xpath = f'//div[contains(@class,"menu")]//span[text()="{option}"]/..'
        self.click()
        self.wait_for_element(option_xpath)
        self.get_base_element(option_xpath).click()

    def get_placeholder(self) -> str:
        """
        #TODO change name to value from placeholder
        Pobranie tekstu wewnątrz listy rozwijanej
        :return:
        """
        validation_xpath = self.xpath + '/div[contains(@class,"comp")]'
        return self.get_base_element(validation_xpath).get_text()
