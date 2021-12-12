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
        option_xpath = f'//span[text()="{option}"]/..'
        self.click()
        option_element = self.get_base_element(option_xpath)
        self.driver.parent.execute_script('return arguments[0].scrollIntoView(false);', self.driver)
        option_element.click()

    def choose_option_with_input(self, option: str) -> None:
        """
        Wybieranie opcji z listy rozwijanej
        :param option: nazwa opcji z listy
        :return:
        """
        option_xpath = f'//span[text()="{option}"]/..'
        collapsable = self.xpath + '//div[contains(@class,"undefined")]'
        self.click()
        self.set_value(option)
        if self.get_base_element(collapsable):
            self.get_base_element(collapsable).click()
        self.driver.parent.execute_script('return arguments[0].scrollIntoView(false);', self.driver)
        self.get_base_element(option_xpath).click()

    def get_value(self) -> str:
        """
        Pobranie tekstu wewnątrz listy rozwijanej
        :return:
        """
        validation_xpath = self.xpath + '/div[contains(@class,"comp")]'
        return self.get_base_element(validation_xpath).get_text()

    def get_all_options(self) -> list:
        """

        :return:
        """
        all_options_xpath = "//*[contains(@id,'option')]"
        all_options_elements = self.driver.find_elements_by_xpath(all_options_xpath)
        all_options_text = []
        for element in all_options_elements:
            all_options_text.append(element.driver.text)
        return all_options_text
