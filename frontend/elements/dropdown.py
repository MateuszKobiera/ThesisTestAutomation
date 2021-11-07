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
        self.wait_for_element((option_xpath, 'Base'))
        self.driver.parent.execute_script('return arguments[0].scrollIntoView(false);', self.driver)
        self.get_base_element(option_xpath).click()

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
